# ============================================
# config/constants.py
# Constantes e Branding
# Sistema de Triagem Canabinoide TEA
# Data: 27 de março de 2026
# ============================================

from typing import Dict, List

# PROFISSIONAL
PROFISSIONAL_NOME = "Dr. Ticiano Sampaio"
PROFISSIONAL_CRM = "CRM-CE 20130"
PROFISSIONAL_ESPECIALIDADES = "Medicina de Família | Terapia Canabinoide"
PROFISSIONAL_WEBSITE = "https://drticianosampaio.com.br/"
PROFISSIONAL_INSTAGRAM = "https://www.instagram.com/drticianosampaio?igsh=MW50b3gzcm16OXA0dg=="
PROFISSIONAL_EMAIL = "drticianosampaio@gmail.com"
PROFISSIONAL_WHATSAPP = "+55 85 92003-8130"
PROFISSIONAL_WHATSAPP_LINK = "https://wa.me/5585920038130?text=Gostaria%20de%20agendar%20uma%20consulta."

# CORES (Dark Theme Verde Escuro)
CORES = {
    'fundo': '#0D2818',           # Dark green escuro (fundo principal)
    'fundo_secundario': '#1a3a2e', # Dark green médio (sidebar)
    'texto': '#E8E8E8',           # Cinza claro (texto principal)
    'texto_secundario': '#D4C5B9', # Bege claro (texto secundário)
    'primaria': '#2D5A3D',        # Green médio (botões)
    'secundaria': '#3D7A4D',      # Green claro (hover)
    'sucesso': '#52B788',         # Green success
    'erro': '#D62828',            # Red error
    'aviso': '#F77F00',           # Orange warning
    'borda': '#3D5A3D',           # Green escuro (bordas)
    'caixa_texto': '#1a3a2e',     # Dark green (inputs)
}

# PÁGINA
PAGE_CONFIG = {
    "page_title": "Triagem Canabinoide TEA",
    "page_icon": "🧠",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# FOOTER
FOOTER_COPYRIGHT = f"© 2026 {PROFISSIONAL_NOME}. Copyleft."
FOOTER_VERSAO = "Versão 2.0"

# OPÇÕES DE FORMULÁRIO
TERAPIA_OPTIONS = [
    "Fonoaudiologia",
    "Terapia Ocupacional",
    "Psicologia/ABA",
    "Psicomotricidade",
    "Musicoterapia",
    "Nutrição",
    "Neuropediatria",
    "Outro"
]

NIVEL_SUPORTE_OPTIONS = {
    1: "Nível 1 - Suporte Mínimo",
    2: "Nível 2 - Suporte Moderado",
    3: "Nível 3 - Suporte Muito Substancial"
}

TIPO_PARTO_OPTIONS = ["Vaginal", "Cesárea", "Fórceps", "Vácuo", "Desconhecido"]

FREQUENCIA_MELTDOWNS_OPTIONS = [
    "Raramente (menos de 1x por semana)",
    "Ocasionalmente (1-2x por semana)",
    "Frequentemente (3-5x por semana)",
    "Muito frequentemente (diariamente)",
    "Constantemente (múltiplas vezes ao dia)"
]

DURACAO_MELTDOWNS_OPTIONS = [
    "Menos de 5 minutos",
    "5-15 minutos",
    "15-30 minutos",
    "30-60 minutos",
    "Mais de 1 hora"
]

DESENVOLVIMENTO_FALA_OPTIONS = [
    "Não verbal",
    "Palavras soltas",
    "Frases simples",
    "Frases complexas",
    "Linguagem fluente",
    "Houve regressão de linguagem"
]

PADRAO_SONO_OPTIONS = [
    "Normal (dorme bem)",
    "Demora a pegar no sono",
    "Acorda frequentemente à noite",
    "Acorda muito cedo",
    "Sono muito agitado",
    "Múltiplas dificuldades"
]

ALIMENTACAO_SELETIVIDADE_OPTIONS = [
    "Sem seletividade",
    "Leve seletividade",
    "Moderada seletividade",
    "Severa seletividade",
    "Muito severa (poucos alimentos aceitos)"
]

FUNCAO_INTESTINAL_OPTIONS = [
    "Normal",
    "Constipação ocasional",
    "Constipação frequente",
    "Diarreia ocasional",
    "Diarreia frequente",
    "Alternância entre constipação e diarreia",
    "Gases/inchaço frequente"
]

IMUNIDADE_OPTIONS = [
    "Normal (adoece raramente)",
    "Adoece ocasionalmente",
    "Adoece frequentemente",
    "Histórico de otites de repetição",
    "Histórico de amigdalites de repetição",
    "Múltiplas infecções recorrentes"
]

EXPERIENCIA_CANNABIS_OPTIONS = [
    "Sem experiência prévia",
    "Experiência prévia com resultado positivo",
    "Experiência prévia com resultado negativo",
    "Experiência prévia com resultado misto",
    "Desconhecido"
]

# MENSAGENS
MENSAGENS = {
    "sucesso_triagem": "✅ Triagem registrada com sucesso!",
    "sucesso_relatorio": "✅ Relatório enviado com sucesso!",
    "erro_validacao": "❌ Erro na validação. Verifique os campos obrigatórios.",
    "erro_arquivo": "❌ Erro ao processar o arquivo. Tente novamente.",
    "erro_banco": "❌ Erro ao conectar com o banco de dados.",
    "campo_obrigatorio": "Este campo é obrigatório.",
    "arquivo_muito_grande": "Arquivo muito grande. Máximo: 10MB",
    "consentimento_obrigatorio": "Você deve aceitar os termos de consentimento para continuar."
}

# CAMPOS OBRIGATÓRIOS
CAMPOS_OBRIGATORIOS_BASELINE = [
    "nome_paciente",
    "data_nascimento",
    "cuidador_nome",
    "cuidador_parentesco",
    "queixa_principal",
    "idade_diagnostico_tea",
    "nivel_suporte",
    "profissional_diagnostico",
    "objetivo_terapia_canabinoide",
    "consentimento_assinado"
]

# STORAGE
STORAGE_BUCKET_NAME = "relatorios-terapeuticos"
MAX_ARQUIVO_SIZE_MB = 10
MAX_ARQUIVO_SIZE_BYTES = MAX_ARQUIVO_SIZE_MB * 1024 * 1024
TIPOS_ARQUIVO_PERMITIDOS = [".pdf"]

# VALIDAÇÃO
CPF_DIGITOS = 11
IDADE_MINIMA_PACIENTE = 0
IDADE_MAXIMA_PACIENTE = 18
IDADE_GESTACIONAL_MINIMA = 20
IDADE_GESTACIONAL_MAXIMA = 42

# FORMATO
FORMATO_DATA = "%d/%m/%Y"
FORMATO_DATA_ISO = "%Y-%m-%d"