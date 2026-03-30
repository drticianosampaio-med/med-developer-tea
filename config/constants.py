# 
# config/constants.py
# Constantes e Enumerações do Sistema
# Data: 30 de março de 2026
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
# INFORMAÇÕES DO PROFISSIONAL
# 

PROFISSIONAL_NOME = "Dr. Ticiano Sampaio"
PROFISSIONAL_CRM = "CRM-CE 20130"
PROFISSIONAL_ESPECIALIDADES = "Medicina de Família • Terapia Canabinoide"

# 
# FOOTER
# 

FOOTER_COPYRIGHT = "© 2026 Dr. Ticiano Sampaio. Todos os direitos reservados."
FOOTER_VERSAO = "Versão 1.1 — Sistema de Triagem TEA com Terapia Canabinoide"

# 
# OPÇÕES DE FORMULÁRIO — PROFISSIONAL DIAGNÓSTICO
# 

PROFISSIONAIS_DIAGNOSTICO = [
    "Neuropediatra",
    "Psiquiatra",
    "Pediatra com especialização em desenvolvimento",
    "Psicólogo clínico",
    "Fonoaudiólogo",
    "Terapeuta ocupacional",
    "Outro profissional legalmente habilitado"
]

# 
# OPÇÕES DE FORMULÁRIO — TIPO DE PARTO
# 

TIPO_PARTO_OPTIONS = [
    "Parto normal",
    "Cesariana programada",
    "Cesariana de urgência",
    "Não informado"
]

# 
# OPÇÕES DE FORMULÁRIO — DESENVOLVIMENTO FALA
# 

DESENVOLVIMENTO_FALA_OPTIONS = [
    "Sem fala funcional",
    "Palavras isoladas",
    "Frases simples (2-3 palavras)",
    "Frases complexas",
    "Conversa fluente com dificuldades pragmáticas",
    "Conversa fluente típica"
]

# 
# OPÇÕES DE FORMULÁRIO — NÍVEL DE SUPORTE
# 

NIVEL_SUPORTE_OPTIONS = [
    "Nível 1 — Suporte necessário",
    "Nível 2 — Suporte substancial necessário",
    "Nível 3 — Suporte muito substancial necessário"
]

# 
# OPÇÕES DE FORMULÁRIO — FREQUÊNCIA MELTDOWNS
# 

FREQUENCIA_MELTDOWNS_OPTIONS = [
    "Raramente (menos de 1x por semana)",
    "Ocasionalmente (1-3x por semana)",
    "Frequentemente (4-6x por semana)",
    "Muito frequentemente (diariamente)"
]

# 
# OPÇÕES DE FORMULÁRIO — DURAÇÃO MELTDOWNS
# 

DURACAO_MELTDOWNS_OPTIONS = [
    "Menos de 5 minutos",
    "5-15 minutos",
    "15-30 minutos",
    "Mais de 30 minutos"
]

# 
# OPÇÕES DE FORMULÁRIO — GATILHOS DE MELTDOWNS
# 

GATILHOS_MELTDOWNS = [
    "Mudanças de rotina",
    "Barulhos altos/sensibilidade auditiva",
    "Aglomerações/ambientes lotados",
    "Transições entre atividades",
    "Frustração/não conseguir o que quer",
    "Contato físico não desejado",
    "Demandas sociais",
    "Fadiga/cansaço",
    "Fome/desconforto físico",
    "Estímulos visuais intensos",
    "Outros"
]

# 
# OPÇÕES DE FORMULÁRIO — ESTEREOTIPIAS
# 

ESTEREOTIPIAS_OPTIONS = [
    "Balanceio do corpo",
    "Movimento repetitivo de mãos/dedos",
    "Girar objetos",
    "Alinhamento de objetos",
    "Movimentos de dedos na frente dos olhos",
    "Vocalizações repetitivas",
    "Ecolalia (repetição de palavras/frases)",
    "Interesse restrito em objetos específicos",
    "Padrões de movimento repetitivos",
    "Outros"
]

# 
# OPÇÕES DE FORMULÁRIO — PADRÃO DE SONO
# 

PADRAO_SONO_OPTIONS = [
    "Dificuldade para adormecer",
    "Despertares noturnos frequentes",
    "Despertar muito cedo",
    "Sono excessivo",
    "Pesadelos/terrores noturnos",
    "Sonambulismo",
    "Padrão normal"
]

# 
# OPÇÕES DE FORMULÁRIO — ALIMENTAÇÃO
# 

ALIMENTACAO_SELETIVIDADE_OPTIONS = [
    "Muito seletivo (poucos alimentos)",
    "Moderadamente seletivo",
    "Pouco seletivo (come a maioria dos alimentos)",
    "Não seletivo"
]

# 
# OPÇÕES DE FORMULÁRIO — FUNÇÃO INTESTINAL
# 

FUNCAO_INTESTINAL_OPTIONS = [
    "Constipação",
    "Diarreia",
    "Alternância constipação/diarreia",
    "Normal",
    "Incontinência fecal"
]

# 
# OPÇÕES DE FORMULÁRIO — IMUNIDADE
# 

IMUNIDADE_OPTIONS = [
    "Infecções frequentes",
    "Infecções ocasionais",
    "Sem infecções recentes",
    "Não informado"
]

# 
# OPÇÕES DE FORMULÁRIO — EXPERIÊNCIA CANNABIS
# 

EXPERIENCIA_CANNABIS_OPTIONS = [
    "Nenhuma experiência prévia",
    "Experiência prévia com CBD isolado",
    "Experiência prévia com THC:CBD",
    "Experiência prévia com outros canabinoides",
    "Não informado"
]

# 
# OPÇÕES DE FORMULÁRIO — TERAPIA
# 

TERAPIA_OPTIONS = [
    "Triagem Inicial",
    "Monitoramento Semanal",
    "Monitoramento Mensal",
    "Avaliação de Escalas",
    "Outro"
]

# 
# MODALIDADES SENSORIAIS
# 

MODALIDADES_SENSORIAIS = [
    "Auditiva",
    "Tátil",
    "Visual",
    "Olfativa",
    "Gustativa",
    "Proprioceptiva",
    "Vestibular"
]

# 
# MENSAGENS DO SISTEMA
# 

MENSAGENS = {
    "sucesso_triagem": "✅ Triagem registrada com sucesso!",
    "sucesso_relatorio": "✅ Relatório enviado com sucesso!",
    "erro_banco": "❌ Erro ao conectar com banco de dados",
    "erro_validacao": "❌ Erro de validação",
    "campo_obrigatorio": "Este campo é obrigatório"
}

# 
# STORAGE
# 

STORAGE_BUCKET_NAME = "relatorios_terapeuticos"

# 
# CAMPOS OBRIGATÓRIOS — BASELINE TEA
# 

CAMPOS_OBRIGATORIOS_BASELINE = [
    "nome_paciente",
    "cpf_paciente",
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