import re
from datetime import date

def validar_cpf(cpf):
    """Valida um número de CPF"""
    cpf = re.sub(r'\D', '', cpf)
    if not cpf or len(cpf) != 11:
        return False, "CPF deve conter 11 dígitos."
    if len(set(cpf)) == 1:
        return False, "CPF inválido: todos os dígitos são iguais."
    
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    digito1 = 0 if resto > 9 else resto
    if int(cpf[9]) != digito1:
        return False, "CPF inválido: primeiro dígito verificador incorreto."
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    digito2 = 0 if resto > 9 else resto
    if int(cpf[10]) != digito2:
        return False, "CPF inválido: segundo dígito verificador incorreto."
    
    return True, "CPF válido."

def gerar_id_paciente(cpf, nome):
    """Gera ID pseudo-anonimizado: INICIAIS + ÚLTIMOS 3 DÍGITOS CPF"""
    if not cpf or not nome:
        return False, "CPF e Nome são obrigatórios.", None
    
    cpf_numerico = re.sub(r'\D', '', cpf)
    if len(cpf_numerico) < 3:
        return False, "CPF deve ter pelo menos 3 dígitos.", None
    
    ultimos_3_cpf = cpf_numerico[-3:]
    partes_nome = nome.upper().split()
    
    if len(partes_nome) >= 2:
        iniciais = partes_nome[0][0] + partes_nome[-1][0]
    elif len(partes_nome) == 1:
        iniciais = partes_nome[0][0]
    else:
        iniciais = "XX"
    
    paciente_id = f"{iniciais}{ultimos_3_cpf}"
    return True, "ID do paciente gerado com sucesso.", paciente_id

def calcular_idade(data_nascimento):
    """Calcula idade com precisão, considerando mês e dia"""
    if data_nascimento is None:
        return 0
    
    hoje = date.today()
    idade = hoje.year - data_nascimento.year
    
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    
    return idade

def validar_idade_paciente(data_nascimento):
    """Valida se a idade do paciente é apropriada (até 18 anos)"""
    if data_nascimento is None:
        return False, "Data de nascimento é obrigatória."
    
    idade = calcular_idade(data_nascimento)
    
    if idade < 0:
        return False, "Data de nascimento futura não é permitida."
    elif idade > 18:
        return False, f"O paciente tem {idade} anos. Este formulário é para pacientes até 18 anos."
    
    return True, "Idade do paciente validada."

def validar_arquivo_pdf(arquivo_bytes, nome_arquivo, max_size_mb=10):
    """Valida se o arquivo é um PDF e não excede o tamanho máximo"""
    if not arquivo_bytes:
        return False, "Nenhum arquivo foi carregado."
    
    if not nome_arquivo.lower().endswith('.pdf'):
        return False, "O arquivo deve ser no formato PDF."
    
    tamanho_mb = len(arquivo_bytes) / (1024 * 1024)
    if tamanho_mb > max_size_mb:
        return False, f"O arquivo excede {max_size_mb}MB. Tamanho: {tamanho_mb:.2f}MB."
    
    return True, "Arquivo PDF válido."