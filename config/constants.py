# 
# config/constants.py
# Constantes e Configurações Globais
# Sistema de Triagem Canabinoide TEA
# Data: 31 de março de 2026
# 

# 
# CONFIGURAÇÃO DA PÁGINA
# 

PAGE_CONFIG = {
    "page_title": "🧠 Triagem TEA — Terapia Canabinoide",
    "page_icon": "🧠",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# 
# INFORMAÇÕES PROFISSIONAIS
# 

PROFISSIONAL_NOME = "Dr. Ticiano Sampaio"
PROFISSIONAL_CRM = "CRM-CE 20130"
PROFISSIONAL_ESPECIALIDADES = "Medicina de Família • Terapia Canabinoide"

# 
# FOOTER
# 

FOOTER_COPYRIGHT = "© 2026 Dr. Ticiano Sampaio. Todos os direitos reservados."
FOOTER_VERSAO = "v1.0 — Sistema de Triagem TEA | 31 de março de 2026"

# 
# SUPABASE STORAGE
# 

STORAGE_BUCKET_NAME = "relatorios-tea"
SUPABASE_URL = "https://seu-projeto.supabase.co"
SUPABASE_KEY = "sua-chave-publica"

# 
# OPÇÕES DE FORMULÁRIO
# 

NIVEL_SUPORTE_OPTIONS = [
    "Nível 1 — Suporte necessário",
    "Nível 2 — Suporte substancial necessário",
    "Nível 3 — Suporte muito substancial necessário"
]

PROFISSIONAIS_DIAGNOSTICO = [
    "Neuropediatra",
    "Psiquiatra Infantil",
    "Psicólogo Clínico",
    "Médico Generalista",
    "Fonoaudiólogo",
    "Terapeuta Ocupacional",
    "Outro profissional legalmente habilitado"
]

TIPO_PARTO_OPTIONS = [
    "Parto Normal",
    "Cesárea Programada",
    "Cesárea de Urgência",
    "Não informado"
]

FREQUENCIA_MELTDOWNS_OPTIONS = [
    "Diário",
    "Semanal",
    "Mensal",
    "Raro"
]

DURACAO_MELTDOWNS_OPTIONS = [
    "Menos de 5 minutos",
    "5-15 minutos",
    "15-30 minutos",
    "Mais de 30 minutos"
]

DESENVOLVIMENTO_FALA_OPTIONS = [
    "Sem fala",
    "Ecolalia",
    "Palavras isoladas",
    "Frases simples",
    "Linguagem funcional",
    "Linguagem fluente"
]

GATILHOS_MELTDOWNS = [
    "Mudanças de rotina",
    "Estímulos sensoriais",
    "Frustração",
    "Transições",
    "Ruído alto",
    "Aglomeração",
    "Demandas sociais",
    "Outros"
]

ESTEREOTIPIAS_OPTIONS = [
    "Movimento repetitivo de mãos",
    "Balanceio corporal",
    "Alinhamento de objetos",
    "Girar objetos",
    "Vocalização repetitiva",
    "Interesse restrito intenso",
    "Outros"
]

PADRAO_SONO_OPTIONS = [
    "Normal",
    "Insônia inicial",
    "Insônia de manutenção",
    "Despertar precoce",
    "Hipersonia",
    "Pesadelos/terror noturno"
]

ALIMENTACAO_SELETIVIDADE_OPTIONS = [
    "Não seletivo",
    "Levemente seletivo",
    "Moderadamente seletivo",
    "Altamente seletivo",
    "Muito restritivo"
]

FUNCAO_INTESTINAL_OPTIONS = [
    "Normal",
    "Constipação",
    "Diarreia",
    "Alternância",
    "Incontinência fecal"
]

IMUNIDADE_OPTIONS = [
    "Normal",
    "Imunodeficiência",
    "Infecções recorrentes",
    "Alergia/Intolerância",
    "Não informado"
]

EXPERIENCIA_CANNABIS_OPTIONS = [
    "Nenhuma",
    "Familiar próximo",
    "Pessoal prévia",
    "Não informado"
]

TERAPIA_OPTIONS = [
    "Terapia Ocupacional",
    "Fonoaudiologia",
    "Psicologia",
    "Neuropsicologia",
    "Psicopedagogia",
    "Outra"
]

# 
# MENSAGENS DE VALIDAÇÃO
# 

MENSAGENS = {
    "cpf_invalido": "CPF inválido. Verifique o número digitado.",
    "campo_obrigatorio": "Este campo é obrigatório.",
    "data_futura": "A data não pode ser no futuro.",
    "idade_invalida": "Idade inválida.",
    "profissional_obrigatorio": "Selecione pelo menos um profissional que fez o diagnóstico.",
    "gatilhos_obrigatorio": "Selecione pelo menos um gatilho de meltdowns.",
    "estereotipias_obrigatorio": "Selecione pelo menos uma estereotipia.",
    "consentimento_obrigatorio": "Consentimento e assinatura são obrigatórios.",
}