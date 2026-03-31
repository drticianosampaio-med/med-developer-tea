# 
# utils/db.py
# Funções de Banco de Dados
# Sistema de Triagem Canabinoide TEA
# Data: 31 de março de 2026
# 

import streamlit as st
from datetime import datetime, date
from typing import Tuple
import json
from supabase import create_client, Client

# 
# INICIALIZAÇÃO SUPABASE
# 

def inicializar_supabase() -> Client:
    """Inicializa cliente Supabase com credenciais de st.secrets"""
    try:
        supabase_url = st.secrets["supabase_url"]
        supabase_key = st.secrets["supabase_key"]
        return create_client(supabase_url, supabase_key)
    except Exception as e:
        st.error(f"Erro ao conectar ao Supabase: {e}")
        return None

supabase = inicializar_supabase()

# 
# TESTAR CONEXÃO
# 

def testar_conexao_supabase() -> Tuple[bool, str]:
    """Testa conexão com Supabase"""
    try:
        if supabase is None:
            return False, "Supabase não inicializado"
        
        # Tenta uma query simples
        resultado = supabase.table("baseline_tea").select("id").limit(1).execute()
        return True, "Conexão com Supabase OK"
    except Exception as e:
        return False, f"Erro na conexão: {str(e)}"

# 
# REGISTRAR BASELINE TEA
# 

def registrar_baseline_tea(dados: dict) -> Tuple[bool, str, str]:
    """
    Registra dados de triagem inicial no Supabase
    
    Args:
        dados: Dicionário com todos os campos do formulário
    
    Returns:
        (sucesso, mensagem, id_registro)
    """
    try:
        if supabase is None:
            return False, "Supabase não inicializado", None
        
        # Preparar dados para inserção
        dados_inserir = {
            "paciente_id": dados.get("paciente_id"),
            "nome_paciente": dados.get("nome_paciente"),
            "cpf_paciente": dados.get("cpf_paciente"),
            "data_nascimento": dados.get("data_nascimento"),
            "cuidador_nome": dados.get("cuidador_nome"),
            "cuidador_parentesco": dados.get("cuidador_parentesco"),
            "cuidador_profissao": dados.get("cuidador_profissao"),
            "residencia": dados.get("residencia"),
            "queixa_principal": dados.get("queixa_principal"),
            "idade_diagnostico_tea": dados.get("idade_diagnostico_tea"),
            "nivel_suporte": dados.get("nivel_suporte"),
            "profissional_diagnostico": json.dumps(dados.get("profissional_diagnostico", [])),
            "outros_diagnosticos": dados.get("outros_diagnosticos"),
            "historico_gestacao": dados.get("historico_gestacao"),
            "tipo_parto": dados.get("tipo_parto"),
            "idade_gestacional": dados.get("idade_gestacional"),
            "condicoes_nascer": dados.get("condicoes_nascer"),
            "marco_cabeca": dados.get("marco_cabeca"),
            "marco_locomocao": dados.get("marco_locomocao"),
            "desenvolvimento_fala": dados.get("desenvolvimento_fala"),
            "idade_primeiras_palavras": dados.get("idade_primeiras_palavras"),
            "controle_esfincteriano": dados.get("controle_esfincteriano"),
            "meltdowns_frequencia": dados.get("meltdowns_frequencia"),
            "meltdowns_duracao": dados.get("meltdowns_duracao"),
            "meltdowns_gatilhos": json.dumps(dados.get("meltdowns_gatilhos", [])),
            "agressividade_autoagressao": dados.get("agressividade_autoagressao"),
            "estereotipias": json.dumps(dados.get("estereotipias", [])),
            "hipersensibilidade": dados.get("hipersensibilidade"),
            "rigidez_cognitiva": dados.get("rigidez_cognitiva"),
            "contato_visual": dados.get("contato_visual"),
            "padrao_sono": dados.get("padrao_sono"),
            "alimentacao_seletividade": dados.get("alimentacao_seletividade"),
            "funcao_intestinal": dados.get("funcao_intestinal"),
            "convulsoes_eeg": dados.get("convulsoes_eeg"),
            "alergias": dados.get("alergias"),
            "imunidade": dados.get("imunidade"),
            "medicacoes_atuais": dados.get("medicacoes_atuais"),
            "medicacoes_previas": dados.get("medicacoes_previas"),
            "terapias_atuais": dados.get("terapias_atuais"),
            "objetivo_terapia_canabinoide": dados.get("objetivo_terapia_canabinoide"),
            "experiencia_cannabis_previa": dados.get("experiencia_cannabis_previa"),
            "consentimento_assinado": dados.get("consentimento_assinado"),
            "assinatura_responsavel": dados.get("assinatura_responsavel"),
            "data_consentimento": dados.get("data_consentimento"),
            "data_triagem": dados.get("data_triagem"),
            "data_criacao": datetime.now().isoformat()
        }
        
        # Inserir no Supabase
        resposta = supabase.table("baseline_tea").insert(dados_inserir).execute()
        
        if resposta.data:
            id_registro = resposta.data[0].get("id") if resposta.data else None
            return True, "✅ Triagem registrada com sucesso!", id_registro
        else:
            return False, "Erro ao registrar triagem", None
    
    except Exception as e:
        return False, f"Erro ao registrar: {str(e)}", None

# 
# FAZER UPLOAD DE RELATÓRIO
# 

def fazer_upload_relatorio_criptografado(
    arquivo_bytes: bytes,
    arquivo_nome: str,
    paciente_id: str,
    tipo_terapia: str,
    profissional_nome: str,
    profissional_registro: str,
    data_upload: date
) -> Tuple[bool, str, str]:
    """
    Faz upload de relatório PDF criptografado para Supabase Storage
    
    Args:
        arquivo_bytes: Conteúdo do arquivo em bytes
        arquivo_nome: Nome original do arquivo
        paciente_id: ID do paciente (pseudo-anonimizado)
        tipo_terapia: Tipo de terapia do relatório
        profissional_nome: Nome do profissional
        profissional_registro: Registro profissional
        data_upload: Data do upload
    
    Returns:
        (sucesso, mensagem, relatorio_id)
    """
    try:
        if supabase is None:
            return False, "Supabase não inicializado", None
        
        # Gerar nome único para arquivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        arquivo_nome_unico = f"{paciente_id}_{timestamp}_{arquivo_nome}"
        
        # Fazer upload para Storage
        caminho_storage = f"relatorios-tea/{paciente_id}/{arquivo_nome_unico}"
        
        resposta_upload = supabase.storage.from_("relatorios-tea").upload(
            caminho_storage,
            arquivo_bytes
        )
        
        # Registrar metadados no banco
        dados_relatorio = {
            "paciente_id": paciente_id,
            "arquivo_nome": arquivo_nome,
            "arquivo_caminho": caminho_storage,
            "tipo_terapia": tipo_terapia,
            "profissional_nome": profissional_nome,
            "profissional_registro": profissional_registro,
            "data_upload": data_upload.isoformat(),
            "data_criacao": datetime.now().isoformat()
        }
        
        resposta_db = supabase.table("relatorios_tea").insert(dados_relatorio).execute()
        
        if resposta_db.data:
            relatorio_id = resposta_db.data[0].get("id")
            return True, "✅ Relatório enviado com sucesso!", relatorio_id
        else:
            return False, "Erro ao registrar relatório", None
    
    except Exception as e:
        return False, f"Erro ao fazer upload: {str(e)}", None