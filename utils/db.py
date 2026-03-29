# ============================================
# utils/db.py
# Operações Supabase
# Sistema de Triagem Canabinoide TEA
# Data: 29 de março de 2026
# ============================================

import os
from typing import Tuple, Optional, Dict
from datetime import date
import streamlit as st
from supabase import create_client, Client
from config.constants import (
    STORAGE_BUCKET_NAME,
    CAMPOS_OBRIGATORIOS_BASELINE,
    MENSAGENS
)
from config.security import obter_instancia_criptografia

# ============================================
# FUNÇÃO HELPER — OBTER VARIÁVEIS DE AMBIENTE
# ============================================

def obter_variavel_ambiente(chave: str, fallback_secrets: bool = True) -> Optional[str]:
    """
    Tenta obter o valor de uma variável de ambiente.
    Se não encontrada e fallback_secrets for True, tenta obter de st.secrets.
    
    Args:
        chave: Nome da variável de ambiente
        fallback_secrets: Se True, tenta st.secrets como fallback
        
    Returns:
        Valor da variável ou None se não encontrada
    """
    valor = os.getenv(chave)
    if not valor and fallback_secrets:
        valor = st.secrets.get(chave)
    return valor

# ============================================
# CLIENTE SUPABASE
# ============================================

def obter_cliente_supabase() -> Optional[Client]:
    """Obtém ou cria instância do cliente Supabase"""
    if "supabase_cliente" in st.session_state:
        return st.session_state.supabase_cliente
    try:
        supabase_url = obter_variavel_ambiente("SUPABASE_URL")
        supabase_key = obter_variavel_ambiente("SUPABASE_KEY")
        if not supabase_url or not supabase_key:
            raise ValueError("SUPABASE_URL e SUPABASE_KEY não configuradas")
        cliente = create_client(supabase_url, supabase_key)
        st.session_state.supabase_cliente = cliente
        return cliente
    except Exception as e:
        st.error(f"❌ Erro ao conectar com Supabase: {str(e)}")
        return None

# ============================================
# REGISTRAR BASELINE TEA
# ============================================

def registrar_baseline_tea(dados: Dict) -> Tuple[bool, str, Optional[str]]:
    """Registra triagem inicial no Supabase"""
    try:
        cliente = obter_cliente_supabase()
        if not cliente:
            return False, MENSAGENS["erro_banco"], None
        
        # Valida campos obrigatórios
        campos_faltantes = []
        for campo in CAMPOS_OBRIGATORIOS_BASELINE:
            if campo not in dados or not dados[campo]:
                campos_faltantes.append(campo)
        if campos_faltantes:
            return False, f"Campos obrigatórios faltando: {', '.join(campos_faltantes)}", None
        
        # Prepara dados
        dados_insert = {k: v for k, v in dados.items() if v is not None}
        
        # Insere
        resposta = cliente.table("baseline_tea").insert(dados_insert).execute()
        if resposta.data:
            paciente_id = dados.get("paciente_id")
            return True, MENSAGENS["sucesso_triagem"], paciente_id
        else:
            return False, "Erro ao registrar triagem", None
    except Exception as e:
        return False, f"Erro ao registrar: {str(e)}", None

# ============================================
# UPLOAD DE RELATÓRIO CRIPTOGRAFADO
# ============================================

def fazer_upload_relatorio_criptografado(
    arquivo_bytes: bytes,
    arquivo_nome: str,
    paciente_id: str,
    tipo_terapia: str,
    profissional_nome: str,
    profissional_registro: str,
    data_relatorio: date
) -> Tuple[bool, str, Optional[str]]:
    """Faz upload de PDF criptografado para Storage"""
    try:
        cliente = obter_cliente_supabase()
        if not cliente:
            return False, MENSAGENS["erro_banco"], None
        
        # Criptografa
        criptografia = obter_instancia_criptografia()
        arquivo_criptografado = criptografia.criptografar_arquivo(arquivo_bytes)
        
        # Prepara nome
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        arquivo_nome_storage = f"{paciente_id}/{tipo_terapia}_{timestamp}.pdf.enc"
        
        # Upload
        resposta_upload = cliente.storage.from_(STORAGE_BUCKET_NAME).upload(
            arquivo_nome_storage,
            arquivo_criptografado,
            {"content-type": "application/octet-stream"}
        )
        if not resposta_upload:
            return False, "Erro ao fazer upload do arquivo", None
        
        # Registra metadados
        metadados = {
            "paciente_id": paciente_id,
            "tipo_terapia": tipo_terapia,
            "data_relatorio": data_relatorio.isoformat(),
            "profissional_nome": profissional_nome,
            "profissional_registro": profissional_registro,
            "arquivo_nome": arquivo_nome,
            "arquivo_criptografado": True,
            "tamanho_bytes": len(arquivo_bytes)
        }
        resposta_metadata = cliente.table("relatorios_terapeuticos").insert(metadados).execute()
        if resposta_metadata.data:
            relatorio_id = resposta_metadata.data[0]["id"]
            return True, MENSAGENS["sucesso_relatorio"], relatorio_id
        else:
            return False, "Erro ao registrar metadados", None
    except Exception as e:
        return False, f"Erro ao fazer upload: {str(e)}", None

# ============================================
# TESTAR CONEXÃO SUPABASE
# ============================================

def testar_conexao_supabase() -> Tuple[bool, str]:
    """Testa conexão com Supabase"""
    try:
        cliente = obter_cliente_supabase()
        if not cliente:
            return False, "Falha ao criar cliente Supabase"
        
        # Tenta fazer uma query simples
        resposta = cliente.table("baseline_tea").select("id").limit(1).execute()
        
        # Verifica se a resposta contém dados (sucesso)
        # APIResponse do Supabase v2.10.0 não tem status_code, apenas data
        if resposta.data is not None:
            return True, "✅ Conexão com Supabase funcionando"
        else:
            # Se data é None, significa que não conseguiu conectar
            return False, "Erro na conexão com Supabase"
    except Exception as e:
        return False, f"Erro ao testar conexão: {str(e)}"