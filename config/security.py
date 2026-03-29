# ============================================
# config/security.py
# Criptografia e Segurança
# Sistema de Triagem Canabinoide TEA
# Data: 29 de março de 2026
# ============================================

import os
import streamlit as st
from cryptography.fernet import Fernet, InvalidToken
import hashlib
from typing import Tuple, Optional

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
# CLASSE DE CRIPTOGRAFIA PDF
# ============================================

class CriptografiaPDF:
    """Criptografia Fernet para arquivos PDF"""
    
    def __init__(self):
        try:
            chave_str = obter_variavel_ambiente("ENCRYPTION_KEY")
            if not chave_str:
                raise ValueError("ENCRYPTION_KEY não encontrada em variáveis de ambiente ou st.secrets")
            
            # Converter para bytes se necessário
            if isinstance(chave_str, str):
                chave_bytes = chave_str.encode()
            else:
                chave_bytes = chave_str
            
            self.cipher = Fernet(chave_bytes)
        except Exception as e:
            raise RuntimeError(f"Erro ao inicializar criptografia: {str(e)}")
    
    def criptografar_arquivo(self, arquivo_bytes: bytes) -> bytes:
        """Criptografa arquivo com Fernet"""
        try:
            return self.cipher.encrypt(arquivo_bytes)
        except Exception as e:
            raise RuntimeError(f"Erro ao criptografar: {str(e)}")
    
    def descriptografar_arquivo(self, arquivo_criptografado: bytes) -> bytes:
        """Descriptografa arquivo"""
        try:
            return self.cipher.decrypt(arquivo_criptografado)
        except InvalidToken:
            raise RuntimeError("Arquivo criptografado inválido ou corrompido.")
        except Exception as e:
            raise RuntimeError(f"Erro ao descriptografar: {str(e)}")
    
    def gerar_hash_sha256(self, dados: bytes) -> str:
        """Gera hash SHA-256 para integridade"""
        try:
            return hashlib.sha256(dados).hexdigest()
        except Exception as e:
            raise RuntimeError(f"Erro ao gerar hash: {str(e)}")
    
    def verificar_integridade(self, dados: bytes, hash_esperado: str) -> bool:
        """Verifica integridade do arquivo"""
        return self.gerar_hash_sha256(dados) == hash_esperado

# ============================================
# FUNÇÕES DE GERENCIAMENTO DE CRIPTOGRAFIA
# ============================================

def obter_instancia_criptografia() -> CriptografiaPDF:
    """Retorna instância singleton de criptografia"""
    if "criptografia_instancia" not in st.session_state:
        try:
            st.session_state.criptografia_instancia = CriptografiaPDF()
        except Exception as e:
            st.error(f"❌ Erro ao inicializar segurança: {str(e)}")
            raise
    return st.session_state.criptografia_instancia

def validar_chave_criptografia() -> Tuple[bool, str]:
    """Valida se chave de criptografia está configurada"""
    try:
        chave = obter_variavel_ambiente("ENCRYPTION_KEY")
        if not chave:
            return False, "ENCRYPTION_KEY não configurada em variáveis de ambiente ou st.secrets"
        
        if isinstance(chave, str):
            chave_bytes = chave.encode()
        else:
            chave_bytes = chave
        
        Fernet(chave_bytes)
        return True, "Chave de criptografia válida"
    except Exception as e:
        return False, f"Erro na validação da chave: {str(e)}"

def validar_seguranca_app() -> bool:
    """Valida segurança na inicialização"""
    valido, mensagem = validar_chave_criptografia()
    if not valido:
        st.error(f"❌ Erro de Segurança: {mensagem}")
        return False
    return True