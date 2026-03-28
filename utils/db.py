# ============================================
# utils/db.py
# Operações Supabase
# Sistema de Triagem Canabinoide TEA
# Data: 27 de março de 2026
# ============================================

from typing import Tuple, Optional, Dict
from datetime import date, datetime
import streamlit as st
from supabase import create_client, Client

from config.constants import (
    STORAGE_BUCKET_NAME,
    CAMPOS_OBRIGATORIOS_BASELINE,
    MENSAGENS
)
from config.security import obter_instancia_criptografia

# ============================================
# CLIENTE SUPABASE
# ============================================

def obter_cliente_supabase() -> Optional[Client]:
    """Obtém ou cria instância do cliente Supabase"""
    if "supabase_cliente" in st.session_state:
        return st.session_state.supabase_cliente
    
    try:
        supabase_url = st.secrets.get("SUPABASE_URL")
        supabase_key = st.secrets.get("SUPABASE_KEY")
        
        if not supabase_url or not supabase_key:
            raise ValueError("SUPABASE_URL e SUPABASE_KEY não configuradas")
        
        cliente = create_client(supabase_url, supabase_key)
        st.session_state.supabase_cliente = cliente
        return cliente
    
    except Exception as e:
        st.error(f"❌ Erro ao conectar com Supabase: {str(e)}")
        return None

# ============================================
# REGISTRAR TRIAGEM INICIAL
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
        
        # Insere na tabela
        resposta = cliente.table("baseline_tea").insert(dados_insert).execute()
        
        # Verifica se inserção foi bem-sucedida
        if resposta.data and len(resposta.data) > 0:
            paciente_id = dados.get("paciente_id")
            return True, MENSAGENS["sucesso_triagem"], paciente_id
        else:
            return False, "Erro ao registrar triagem", None
    
    except Exception as e:
        return False, f"Erro ao registrar: {str(e)}", None

# ============================================
# UPLOAD DE RELATÓRIOS CRIPTOGRAFADOS
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
        
        # Criptografa arquivo
        criptografia = obter_instancia_criptografia()
        arquivo_criptografado = criptografia.criptografar_arquivo(arquivo_bytes)
        
        # Prepara nome do arquivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        arquivo_nome_storage = f"{paciente_id}/{tipo_terapia}_{timestamp}.pdf.enc"
        
        # Faz upload para Storage
        resposta_upload = cliente.storage.from_(STORAGE_BUCKET_NAME).upload(
            arquivo_nome_storage,
            arquivo_criptografado,
            {"content-type": "application/octet-stream"}
        )
        
        if not resposta_upload:
            return False, "Erro ao fazer upload do arquivo", None
        
        # Registra metadados na tabela
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
        
        if resposta_metadata.data and len(resposta_metadata.data) > 0:
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
        
        # Verifica se a resposta tem dados (sucesso)
        if resposta.data is not None:
            return True, "✅ Conexão com Supabase funcionando"
        else:
            return False, "Erro na conexão com Supabase"
    
    except Exception as e:
        return False, f"Erro ao testar conexão: {str(e)}"

# ============================================
# BUSCAR DADOS DE PACIENTE
# ============================================

def buscar_paciente(paciente_id: str) -> Tuple[bool, str, Optional[Dict]]:
    """Busca dados de um paciente específico"""
    try:
        cliente = obter_cliente_supabase()
        if not cliente:
            return False, MENSAGENS["erro_banco"], None
        
        resposta = cliente.table("baseline_tea").select("*").eq("paciente_id", paciente_id).execute()
        
        if resposta.data and len(resposta.data) > 0:
            return True, "Paciente encontrado", resposta.data[0]
        else:
            return False, "Paciente não encontrado", None
    
    except Exception as e:
        return False, f"Erro ao buscar paciente: {str(e)}", None

# ============================================
# LISTAR TODOS OS PACIENTES
# ============================================

def listar_pacientes() -> Tuple[bool, str, Optional[list]]:
    """Lista todos os pacientes registrados"""
    try:
        cliente = obter_cliente_supabase()
        if not cliente:
            return False, MENSAGENS["erro_banco"], None
        
        resposta = cliente.table("baseline_tea").select("paciente_id, nome_paciente, data_triagem").order("data_triagem", desc=True).execute()
        
        if resposta.data:
            return True, "Pacientes listados com sucesso", resposta.data
        else:
            return False, "Nenhum paciente encontrado", []
    
    except Exception as e:
        return False, f"Erro ao listar pacientes: {str(e)}", None

# ============================================
# ATUALIZAR DADOS DE PACIENTE
# ============================================

def atualizar_paciente(paciente_id: str, dados: Dict) -> Tuple[bool, str]:
    """Atualiza dados de um paciente"""
    try:
        cliente = obter_cliente_supabase()
        if not cliente:
            return False, MENSAGENS["erro_banco"]
        
        resposta = cliente.table("baseline_tea").update(dados).eq("paciente_id", paciente_id).execute()
        
        if resposta.data:
            return True, "Paciente atualizado com sucesso"
        else:
            return False, "Erro ao atualizar paciente"
    
    except Exception as e:
        return False, f"Erro ao atualizar: {str(e)}"

# ============================================
# DELETAR PACIENTE (DIREITO AO ESQUECIMENTO - LGPD)
# ============================================

def deletar_paciente(paciente_id: str) -> Tuple[bool, str]:
    """Deleta um paciente (Direito ao Esquecimento - LGPD)"""
    try:
        cliente = obter_cliente_supabase()
        if not cliente:
            return False, MENSAGENS["erro_banco"]
        
        # Deleta relatórios associados
        cliente.table("relatorios_terapeuticos").delete().eq("paciente_id", paciente_id).execute()
        
        # Deleta monitoramento associado
        cliente.table("monitoramento_tea").delete().eq("paciente_id", paciente_id).execute()
        
        # Deleta baseline
        resposta = cliente.table("baseline_tea").delete().eq("paciente_id", paciente_id).execute()
        
        if resposta.data is not None or resposta.data == []:
            return True, "Paciente deletado com sucesso (Direito ao Esquecimento)"
        else:
            return False, "Erro ao deletar paciente"
    
    except Exception as e:
        return False, f"Erro ao deletar: {str(e)}"