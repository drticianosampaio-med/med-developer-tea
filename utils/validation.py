# 
# utils/validation.py
# Funções de Validação
# Sistema de Triagem Canabinoide TEA
# Data: 31 de março de 2026
# 

from datetime import date
from typing import Tuple, List
import re

# 
# VALIDAÇÃO DE CPF
# 

def validar_cpf(cpf: str) -> Tuple[bool, str]:
    """Valida CPF brasileiro"""
    if not cpf:
        return False, "CPF é obrigatório"
    
    cpf = re.sub(r'\D', '', cpf)
    
    if len(cpf) != 11:
        return False, "CPF deve ter 11 dígitos"
    
    if cpf == cpf[0] * 11:
        return False, "CPF inválido"
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    if int(cpf[9]) != digito1:
        return False, "CPF inválido"
    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    if int(cpf[10]) != digito2:
        return False, "CPF inválido"
    
    return True, "CPF válido"

# 
# GERAR ID DO PACIENTE
# 

def gerar_id_paciente(cpf: str, nome: str) -> Tuple[bool, str, str]:
    """Gera ID pseudo-anonimizado (INICIAIS + ÚLTIMOS 3 DÍGITOS CPF)"""
    try:
        cpf_limpo = re.sub(r'\D', '', cpf)
        ultimos_3 = cpf_limpo[-3:]
        
        palavras = nome.strip().split()
        iniciais = ''.join([p[0].upper() for p in palavras if p])[:3]
        
        paciente_id = f"{iniciais}{ultimos_3}"
        
        if len(paciente_id) < 4:
            return False, "Nome ou CPF insuficiente para gerar ID", None
        
        return True, "ID gerado com sucesso", paciente_id
    except Exception as e:
        return False, f"Erro ao gerar ID: {str(e)}", None

# 
# CALCULAR IDADE
# 

def calcular_idade(data_nascimento: date) -> int:
    """Calcula idade em anos"""
    hoje = date.today()
    idade = hoje.year - data_nascimento.year
    
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    
    return idade

# 
# VALIDAÇÃO DE ARQUIVO PDF
# 

def validar_arquivo_pdf(arquivo_bytes: bytes, arquivo_nome: str, max_size_mb: int = 10) -> Tuple[bool, str]:
    """Valida arquivo PDF"""
    tamanho_mb = len(arquivo_bytes) / (1024 * 1024)
    if tamanho_mb > max_size_mb:
        return False, f"Arquivo muito grande ({tamanho_mb:.2f}MB). Máximo: {max_size_mb}MB"
    
    if not arquivo_nome.lower().endswith('.pdf'):
        return False, "Apenas arquivos PDF são permitidos"
    
    if not arquivo_bytes.startswith(b'%PDF'):
        return False, "Arquivo não é um PDF válido"
    
    return True, "Arquivo PDF válido"

# 
# VALIDAÇÃO DE IDADE PACIENTE
# 

def validar_idade_paciente(data_nascimento: date) -> Tuple[bool, str]:
    """Valida se a data de nascimento é válida"""
    if data_nascimento is None:
        return False, "Data de nascimento é obrigatória"
    
    idade = calcular_idade(data_nascimento)
    
    if idade < 0:
        return False, "Data de nascimento futura não é permitida"
    
    return True, "Data de nascimento validada"

# 
# VALIDAÇÃO DE PROFISSIONAL DIAGNÓSTICO
# 

def validar_profissional_diagnostico(profissionais: List[str]) -> Tuple[bool, str]:
    """Valida que pelo menos um profissional foi selecionado"""
    if not profissionais or len(profissionais) == 0:
        return False, "Selecione pelo menos um profissional que fez o diagnóstico."
    return True, "Profissional validado."

# 
# VALIDAÇÃO DE GATILHOS
# 

def validar_gatilhos(gatilhos: List[str]) -> Tuple[bool, str]:
    """Valida que pelo menos um gatilho foi selecionado"""
    if not gatilhos or len(gatilhos) == 0:
        return False, "Selecione pelo menos um gatilho de meltdowns."
    return True, "Gatilhos validados."

# 
# VALIDAÇÃO DE ESTEREOTIPIAS
# 

def validar_estereotipias(estereotipias: List[str]) -> Tuple[bool, str]:
    """Valida que pelo menos uma estereotipia foi selecionada"""
    if not estereotipias or len(estereotipias) == 0:
        return False, "Selecione pelo menos uma estereotipia."
    return True, "Estereotipias validadas."