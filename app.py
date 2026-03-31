# 
# app.py — VERSÃO CORRIGIDA (FASE 1)
# Interface Principal do Sistema de Triagem Canabinoide TEA
# Data: 30 de março de 2026
# Correções: Remoção de sliders para Hipersensibilidade e Rigidez Cognitiva,
#            restaurando campos de texto originais.
# 

import streamlit as st
from datetime import datetime, date
import os
import locale
from typing import List

# Importações de configuração
from config.constants import (
    PAGE_CONFIG,
    PROFISSIONAL_NOME,
    PROFISSIONAL_CRM,
    PROFISSIONAL_ESPECIALIDADES,
    FOOTER_COPYRIGHT,
    FOOTER_VERSAO,
    TERAPIA_OPTIONS,
    NIVEL_SUPORTE_OPTIONS,
    FREQUENCIA_MELTDOWNS_OPTIONS,
    DURACAO_MELTDOWNS_OPTIONS,
    DESENVOLVIMENTO_FALA_OPTIONS,
    PADRAO_SONO_OPTIONS,
    ALIMENTACAO_SELETIVIDADE_OPTIONS,
    FUNCAO_INTESTINAL_OPTIONS,
    IMUNIDADE_OPTIONS,
    EXPERIENCIA_CANNABIS_OPTIONS,
    PROFISSIONAIS_DIAGNOSTICO,
    TIPO_PARTO_OPTIONS,
    GATILHOS_MELTDOWNS,
    ESTEREOTIPIAS_OPTIONS,
    MENSAGENS
)
from config.security import validar_seguranca_app
from utils.db import registrar_baseline_tea, fazer_upload_relatorio_criptografado, testar_conexao_supabase
from utils.validation import (
    validar_cpf,
    gerar_id_paciente,
    calcular_idade,
    validar_idade_paciente,
    validar_arquivo_pdf,
    validar_profissional_diagnostico,
    validar_gatilhos,
    validar_estereotipias
)

# 
# CONFIGURAÇÃO DA PÁGINA — CRÍTICO: APENAS UMA CHAMADA E NO TOPO
# 

st.set_page_config(
    page_title=PAGE_CONFIG["page_title"],
    page_icon=PAGE_CONFIG["page_icon"],
    layout=PAGE_CONFIG["layout"],
    initial_sidebar_state=PAGE_CONFIG["initial_sidebar_state"]
)

# 
# CONFIGURAÇÃO DE LOCALIZAÇÃO — FORMATO BRASILEIRO
# 

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR')
    except:
        pass

MESES_PT = {
    'January': 'Janeiro',
    'February': 'Fevereiro',
    'March': 'Março',
    'April': 'Abril',
    'May': 'Maio',
    'June': 'Junho',
    'July': 'Julho',
    'August': 'Agosto',
    'September': 'Setembro',
    'October': 'Outubro',
    'November': 'Novembro',
    'December': 'Dezembro'
}

def formatar_data_br(data_obj):
    """Formata data para português brasileiro"""
    if data_obj:
        data_formatada = data_obj.strftime('%d de %B de %Y')
        for mes_en, mes_pt in MESES_PT.items():
            data_formatada = data_formatada.replace(mes_en, mes_pt)
        return data_formatada
    return None

def converter_data_iso(data_obj):
    """Converte date object para formato ISO"""
    if data_obj:
        return data_obj.isoformat()
    return None

# 
# CORES — Dark Green + Bege/Cinza
# 

CORES = {
    'fundo': '#0D2818',
    'fundo_secundario': '#1a3a2e',
    'texto': '#E8E8E8',
    'texto_secundario': '#D4C5B9',
    'primaria': '#2D5A3D',
    'secundaria': '#3D7A4D',
    'sucesso': '#52B788',
    'erro': '#D62828',
    'aviso': '#F77F00',
    'borda': '#3D5A3D',
    'caixa_texto': '#1a3a2e',
}

# 
# CSS MINIMALISTA
# 

st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-color: {CORES['fundo']};
    }}
    [data-testid="stMainBlockContainer"] {{
        background-color: {CORES['fundo']};
    }}
    [data-testid="stSidebar"] {{
        background-color: {CORES['fundo_secundario']};
    }}
    [data-testid="stHeader"] {{
        background-color: {CORES['fundo']};
    }}
    [data-testid="stDecoration"] {{
        background-color: {CORES['fundo']};
    }}
    [data-testid="stMarkdownContainer"] {{
        color: {CORES['texto']};
    }}
    p, span, label {{
        color: {CORES['texto']} !important;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {CORES['texto_secundario']} !important;
    }}
    .stButton > button {{
        background-color: {CORES['primaria']};
        color: {CORES['texto']};
        border: 1px solid {CORES['secundaria']};
    }}
    .stButton > button:hover {{
        background-color: {CORES['secundaria']};
    }}
    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox select,
    .stNumberInput input,
    .stDateInput input {{
        background-color: {CORES['caixa_texto']} !important;
        color: {CORES['texto']} !important;
        border: 1px solid {CORES['borda']} !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 
# SIDEBAR
# 

with st.sidebar:
    st.markdown("---")
    st.markdown("### PLATAFORMA DE ACOMPANHAMENTO CLÍNICO")
    st.markdown("**Terapia Canabinoide + Dados + Precisão**")
    st.markdown("---")
    st.markdown(f"### {PROFISSIONAL_NOME}")
    st.write(f"**{PROFISSIONAL_CRM}**")
    st.write(PROFISSIONAL_ESPECIALIDADES)
    foto_path = os.path.join(os.path.dirname(__file__), "assets", "foto_ticiano.jpg")
    try:
        if os.path.exists(foto_path):
            st.image(foto_path, width=200, use_container_width=False)
        else:
            st.warning("⚠️ Foto não encontrada.")
    except Exception as e:
        st.error(f"Erro ao carregar foto: {e}")
    st.markdown("---")
    st.write("""
    Este módulo faz parte de um sistema integrado para monitoramento preciso de 
    pacientes em terapia canabinoide operando com coleta estruturada de dados de 
    relevância clínica orientada pela boa semiologia médica. Toda terapia canabinóide 
    é hoje considerada experimental, então a prática clínica deve ser feita com o 
    rigor exigido pela ciência.
    """)
    st.markdown("---")
    st.write("**CONECTE-SE**")
    st.markdown("[🌐 Site: drticianosamapaio.com.br](https://drticianosamapaio.com.br)")
    st.markdown("[📱 Instagram: @drticianosampaio](https://www.instagram.com/drticianosampaio?igsh=MW50b3gzcm16OXA0dg==)")
    st.markdown("[📧 Contato: drticianosamapaio@gmail.com](mailto:drticianosamapaio@gmail.com)")
    st.markdown("[💬 Agende agora: WhatsApp](https://wa.me/5585920038130?text=Gostaria+de+agendar+uma+consulta.)")
    st.markdown("---")
    st.write("**CONFORMIDADE E SEGURANÇA**")
    st.write("🔒 Dados protegidos conforme Lei Geral de Proteção de Dados (LGPD 13.709/2018)")
    st.write("Criptografia em trânsito e em repouso | Pseudo-anonimização | Direito ao esquecimento")
    st.markdown("---")
    st.caption(FOOTER_COPYRIGHT)
    st.caption(FOOTER_VERSAO)

# 
# VALIDAÇÃO INICIAL
# 

if not validar_seguranca_app():
    st.stop()

conexao_ok, msg_conexao = testar_conexao_supabase()
if not conexao_ok:
    st.warning(f"⚠️ {msg_conexao}")

# 
# CABEÇALHO PRINCIPAL
# 

st.title("🧠 Triagem Inicial: Paciente Pediátrico (TEA)")
st.subheader("Formulário para Coleta de Dados Clínicos Iniciais")
st.write(f"**Data:** {formatar_data_br(datetime.now())}")
st.write("""
Este formulário coleta informações detalhadas sobre o histórico clínico e desenvolvimento
do paciente pediátrico com Transtorno do Espectro Autista (TEA). As informações fornecidas 
são cruciais para a elaboração de um plano de tratamento individualizado e eficaz.
""")
st.divider()

# 
# FORMULÁRIO PRINCIPAL
# 

with st.form(key="formulario_triagem", clear_on_submit=False):
    # SEÇÃO 1: IDENTIFICAÇÃO
    st.header("1️⃣ Identificação do Paciente e Cuidadores")
    col1, col2 = st.columns(2)
    with col1:
        nome_paciente = st.text_input("Nome do Paciente *", key="nome_paciente")
        cpf_paciente = st.text_input("CPF do Paciente *", key="cpf_paciente", placeholder="000.000.000-00")
    with col2:
        data_nascimento = st.date_input(
            "Data de Nascimento *", 
            key="data_nascimento", 
            format="DD/MM/YYYY"
        )
        if data_nascimento:
            idade = calcular_idade(data_nascimento)
            st.write(f"Idade atual: **{idade} anos**")
    col3, col4 = st.columns(2)
    with col3:
        cuidador_nome = st.text_input("Nome do Cuidador Principal *", key="cuidador_nome")
        cuidador_parentesco = st.selectbox("Grau de Parentesco *", 
            options=["Mãe", "Pai", "Avó", "Avô", "Tio/Tia", "Outro"],
            key="cuidador_parentesco")
    with col4:
        cuidador_profissao = st.text_input("Profissão do Cuidador", key="cuidador_profissao")
        residencia = st.text_area("Com quem a criança reside?", key="residencia", height=100)
    st.divider()

    # SEÇÃO 2: MOTIVO DA CONSULTA
    st.header("2️⃣ Motivo da Consulta e Diagnóstico")
    queixa_principal = st.text_area("Qual a queixa principal hoje? *", 
        key="queixa_principal", height=100)
    col5, col6 = st.columns(2)
    with col5:
        idade_diagnostico_tea = st.number_input(
            "Idade do diagnóstico de TEA (meses) *",
            min_value=0, max_value=1200, key="idade_diagnostico_tea"
        )
        nivel_suporte = st.selectbox("Nível de Suporte *",
            options=NIVEL_SUPORTE_OPTIONS, key="nivel_suporte")
    with col6:
        profissionais_selecionados = st.multiselect(
            "Profissional(is) que fez(fizeram) o diagnóstico *",
            options=PROFISSIONAIS_DIAGNOSTICO,
            key="profissional_diagnostico_multiselect"
        )
        outro_profissional = ""
        if "Outro profissional legalmente habilitado" in profissionais_selecionados:
            outro_profissional = st.text_input("Especifique o outro profissional", key="outro_profissional_diagnostico")
        
        tipo_parto = st.selectbox("Tipo de Parto",
            options=TIPO_PARTO_OPTIONS, key="tipo_parto")

        outros_diagnosticos = st.text_area("Outros diagnósticos?",
            key="outros_diagnosticos", height=100)
    st.divider()

    # SEÇÃO 3: HISTÓRICO GESTACIONAL
    st.header("3️⃣ Histórico Gestacional e Neonatal")
    col7, col8 = st.columns(2)
    with col7:
        historico_gestacao = st.text_area("Histórico da Gestação",
            key="historico_gestacao", height=100)
    with col8:
        idade_gestacional = st.text_input("Idade Gestacional (semanas)",
            key="idade_gestacional")
        condicoes_nascer = st.text_area("Condições ao Nascer",
            key="condicoes_nascer", height=100)
    st.divider()

    # SEÇÃO 4: DESENVOLVIMENTO
    st.header("4️⃣ Desenvolvimento Neuropsicomotor")
    col9, col10, col11, col12 = st.columns(4)
    with col9:
        marco_cabeca = st.text_input("Controle de Cabeça (idade em meses)", key="marco_cabeca")
    with col10:
        marco_locomocao = st.text_input("Sentou e andou (idade em meses)", key="marco_locomocao")
    with col11:
        desenvolvimento_fala = st.selectbox("Desenvolvimento da fala",
            options=DESENVOLVIMENTO_FALA_OPTIONS, key="desenvolvimento_fala")
        idade_primeiras_palavras = st.number_input(
            "Idade ao falar as primeiras palavras (meses)",
            min_value=0, max_value=600, key="idade_primeiras_palavras"
        )
    with col12:
        controle_esfincteriano = st.text_input("Controle esfincteriano (idade em meses)", key="controle_esfincteriano")
    st.divider()

    # SEÇÃO 5: PERFIL SENSORIAL E COMPORTAMENTAL — CORRIGIDO (SEM SLIDERS)
    st.header("5️⃣ Perfil Sensorial e Comportamental")
    col13, col14 = st.columns(2)
    with col13:
        meltdowns_frequencia = st.selectbox("Crises/Meltdowns - Frequência",
            options=FREQUENCIA_MELTDOWNS_OPTIONS, key="meltdowns_frequencia")
        meltdowns_duracao = st.selectbox("Crises/Meltdowns - Duração",
            options=DURACAO_MELTDOWNS_OPTIONS, key="meltdowns_duracao")
        gatilhos_selecionados = st.multiselect(
            "Gatilhos mais comuns *",
            options=GATILHOS_MELTDOWNS,
            key="meltdowns_gatilhos_multiselect"
        )
        outros_gatilhos = ""
        if "Outros" in gatilhos_selecionados:
            outros_gatilhos = st.text_input("Especifique outros gatilhos", key="outros_gatilhos_meltdowns")
    with col14:
        agressividade_autoagressao = st.text_area("Agressividade / Autoagressão",
            key="agressividade_autoagressao", height=100)
        estereotipias_selecionadas = st.multiselect(
            "Estereotipias (Stimming) *",
            options=ESTEREOTIPIAS_OPTIONS,
            key="estereotipias_multiselect"
        )
        outras_estereotipias = ""
        if "Outros" in estereotipias_selecionadas:
            outras_estereotipias = st.text_input("Especifique outras estereotipias", key="outras_estereotipias_stimming")
    
    # CAMPOS DE TEXTO RESTAURADOS
    hipersensibilidade = st.text_area("Hipersensibilidade / Hipossensibilidade",
        key="hipersensibilidade", height=100)
    col15, col16 = st.columns(2)
    with col15:
        rigidez_cognitiva = st.text_area("Rigidez Cognitiva",
            key="rigidez_cognitiva", height=100)
    with col16:
        contato_visual = st.text_area("Contato Visual e Interação Social",
            key="contato_visual", height=100)
    st.divider()

    # SEÇÃO 6: SONO E ALIMENTAÇÃO
    st.header("6️⃣ Sono e Alimentação")
    col17, col18 = st.columns(2)
    with col17:
        padrao_sono = st.multiselect("Padrão de Sono",
            options=PADRAO_SONO_OPTIONS, key="padrao_sono")
    with col18:
        alimentacao_seletividade = st.selectbox("Seletividade Alimentar",
            options=ALIMENTACAO_SELETIVIDADE_OPTIONS, key="alimentacao_seletividade")
    funcao_intestinal = st.multiselect("Função Intestinal",
        options=FUNCAO_INTESTINAL_OPTIONS, key="funcao_intestinal")
    st.divider()

    # SEÇÃO 7: HISTÓRICO MÉDICO
    st.header("7️⃣ Histórico Médico e Comorbidades")
    col19, col20 = st.columns(2)
    with col19:
        convulsoes_eeg = st.text_area("Convulsões / EEG",
            key="convulsoes_eeg", height=100)
        alergias = st.text_area("Alergias",
            key="alergias", height=100)
    with col20:
        imunidade = st.selectbox("Imunidade",
            options=IMUNIDADE_OPTIONS, key="imunidade")
    st.divider()

    # SEÇÃO 8: HISTÓRICO TERAPÊUTICO
    st.header("8️⃣ Histórico Terapêutico")
    medicamentos_atuais = st.text_area("Medicamentos em Uso Atuais",
        key="medicacoes_atuais", height=100)
    medicamentos_previos = st.text_area("Medicamentos em uso Prévios",
        key="medicacoes_previas", height=100)
    terapias_atuais = st.text_area("Terapias em Curso",
        key="terapias_atuais", height=100)
    st.divider()

    # SEÇÃO 9: EXPECTATIVAS
    st.header("9️⃣ Expectativas com Terapia Canabinoide")
    objetivo_terapia = st.text_area("Qual o principal objetivo da família? *",
        key="objetivo_terapia_canabinoide", height=100)
    experiencia_cannabis = st.selectbox("Experiência prévia com Cannabis",
        options=EXPERIENCIA_CANNABIS_OPTIONS, key="experiencia_cannabis_previa")
    st.divider()

    # SEÇÃO 10: UPLOAD DE RELATÓRIOS
    st.header("🔟 Upload de Relatórios (Opcional)")
    st.write("Você pode anexar relatórios de terapias anteriores (PDF). Máximo: 10MB.")
    arquivo_pdf = st.file_uploader("Selecione um arquivo PDF",
        type=["pdf"], key="arquivo_pdf")
    arquivo_bytes = None
    if arquivo_pdf:
        arquivo_bytes = arquivo_pdf.read()
        valido, msg = validar_arquivo_pdf(arquivo_bytes, arquivo_pdf.name)
        if valido:
            st.success(f"✅ {msg}")
        else:
            st.error(f"❌ {msg}")
            arquivo_bytes = None
    st.divider()

    # SEÇÃO 11: CONSENTIMENTO
    st.header("1️⃣1️⃣ Consentimento Informado")
    st.write("""
    **Termos de Consentimento e Privacidade**
    Ao preencher este formulário, você concorda que:
    1. **Dados Clínicos**: As informações serão utilizadas exclusivamente para fins de triagem e planejamento terapêutico.
    2. **Privacidade**: Seus dados serão armazenados de forma segura e criptografada, em conformidade com a LGPD.
    3. **Pseudo-anonimização**: O paciente será identificado por um código único (iniciais + últimos 3 dígitos do CPF).
    4. **Acesso Restrito**: Apenas profissionais autorizados terão acesso aos dados clínicos.
    5. **Direitos**: Você tem direito a acessar, corrigir ou solicitar a exclusão de seus dados a qualquer momento.
    """)
        consentimento_assinado = st.checkbox("Eu li e concordo com os termos de consentimento *",
        key="consentimento_assinado")
    assinatura_responsavel = ""
    data_consentimento = None
    if consentimento_assinado:
        assinatura_responsavel = st.text_input("Assinatura do Responsável (nome completo) *",
            key="assinatura_responsavel")
        data_consentimento = st.date_input("Data do Consentimento *",
            key="data_consentimento", value=date.today(), format="DD/MM/YYYY")
    st.divider()

    # BOTÃO DE ENVIO
    col_submit = st.columns([1, 1, 1])
    with col_submit[1]:
        botao_enviar = st.form_submit_button("📤 Enviar Triagem", use_container_width=True)

# 
# PROCESSAMENTO DO FORMULÁRIO
# 

if botao_enviar:
    profissional_diagnostico_final_processado = profissionais_selecionados
    if outro_profissional:
        profissional_diagnostico_final_processado = [p for p in profissionais_selecionados if p != "Outro profissional legalmente habilitado"] + [outro_profissional]

    meltdowns_gatilhos_final_processado = gatilhos_selecionados
    if outros_gatilhos:
        meltdowns_gatilhos_final_processado = [g for g in gatilhos_selecionados if g != "Outros"] + [outros_gatilhos]

    estereotipias_final_processado = estereotipias_selecionadas
    if outras_estereotipias:
        estereotipias_final_processado = [e for e in estereotipias_selecionadas if e != "Outros"] + [outras_estereotipias]

    dados_formulario = {
        "nome_paciente": nome_paciente,
        "cpf_paciente": cpf_paciente,
        "data_nascimento": converter_data_iso(data_nascimento),
        "cuidador_nome": cuidador_nome,
        "cuidador_parentesco": cuidador_parentesco,
        "cuidador_profissao": cuidador_profissao,
        "residencia": residencia,
        "queixa_principal": queixa_principal,
        "idade_diagnostico_tea": idade_diagnostico_tea,
        "nivel_suporte": nivel_suporte,
        "profissional_diagnostico": profissional_diagnostico_final_processado,
        "outros_diagnosticos": outros_diagnosticos,
        "historico_gestacao": historico_gestacao,
        "tipo_parto": tipo_parto,
        "idade_gestacional": idade_gestacional,
        "condicoes_nascer": condicoes_nascer,
        "marco_cabeca": marco_cabeca,
        "marco_locomocao": marco_locomocao,
        "desenvolvimento_fala": desenvolvimento_fala,
        "idade_primeiras_palavras": idade_primeiras_palavras,
        "controle_esfincteriano": controle_esfincteriano,
        "meltdowns_frequencia": meltdowns_frequencia,
        "meltdowns_duracao": meltdowns_duracao,
        "meltdowns_gatilhos": meltdowns_gatilhos_final_processado,
        "agressividade_autoagressao": agressividade_autoagressao,
        "estereotipias": estereotipias_final_processado,
        "hipersensibilidade": hipersensibilidade,
        "rigidez_cognitiva": rigidez_cognitiva,
        "contato_visual": contato_visual,
        "padrao_sono": ", ".join(padrao_sono),
        "alimentacao_seletividade": alimentacao_seletividade,
        "funcao_intestinal": ", ".join(funcao_intestinal),
        "convulsoes_eeg": convulsoes_eeg,
        "alergias": alergias,
        "imunidade": imunidade,
        "medicacoes_atuais": medicamentos_atuais,
        "medicacoes_previas": medicamentos_previos,
        "terapias_atuais": terapias_atuais,
        "objetivo_terapia_canabinoide": objetivo_terapia,
        "experiencia_cannabis_previa": experiencia_cannabis,
        "consentimento_assinado": consentimento_assinado,
        "assinatura_responsavel": assinatura_responsavel,
        "data_consentimento": converter_data_iso(data_consentimento),
        "data_triagem": date.today().isoformat()
    }

    cpf_valido, msg_cpf = validar_cpf(cpf_paciente)
    if not cpf_valido:
        st.error(f"❌ CPF inválido: {msg_cpf}")
        st.stop()

    sucesso_id, msg_id, paciente_id = gerar_id_paciente(cpf_paciente, nome_paciente)
    if not sucesso_id:
        st.error(f"❌ Erro ao gerar ID: {msg_id}")
        st.stop()

    idade_valida, msg_idade = validar_idade_paciente(data_nascimento)
    if not idade_valida:
        st.error(f"❌ {msg_idade}")
        st.stop()

    prof_valido, msg_prof = validar_profissional_diagnostico(profissionais_selecionados)
    if not prof_valido:
        st.error(f"❌ {msg_prof}")
        st.stop()
    
    gatilhos_valido, msg_gatilhos = validar_gatilhos(gatilhos_selecionados)
    if not gatilhos_valido:
        st.error(f"❌ {msg_gatilhos}")
        st.stop()

    estereotipias_valido, msg_estereotipias = validar_estereotipias(estereotipias_selecionadas)
    if not estereotipias_valido:
        st.error(f"❌ {msg_estereotipias}")
        st.stop()

    if not consentimento_assinado or not assinatura_responsavel:
        st.error("❌ Consentimento e assinatura são obrigatórios")
        st.stop()

    dados_formulario["paciente_id"] = paciente_id
    sucesso, mensagem, _ = registrar_baseline_tea(dados_formulario)

    if sucesso:
        st.success(f"✅ {mensagem}")
        st.success(f"**ID do Paciente: {paciente_id}**")
        st.info("Seus dados foram registrados com sucesso e criptografados.")
        if arquivo_bytes:
            st.info("Processando upload de relatório...")
            tipo_terapia = st.selectbox("Tipo de terapia do relatório",
                options=TERAPIA_OPTIONS, key="tipo_terapia_relatorio")
            profissional_nome = st.text_input("Nome do profissional",
                key="profissional_nome_relatorio")
            profissional_registro = st.text_input("Registro profissional",
                key="profissional_registro_relatorio")
            if st.button("📤 Enviar Relatório"):
                sucesso_upload, msg_upload, relatorio_id = fazer_upload_relatorio_criptografado(
                    arquivo_bytes,
                    arquivo_pdf.name,
                    paciente_id,
                    tipo_terapia,
                    profissional_nome,
                    profissional_registro,
                    date.today()
                )
                if sucesso_upload:
                    st.success(f"✅ {msg_upload}")
                    st.info(f"ID do Relatório: {relatorio_id}")
                else:
                    st.error(f"❌ {msg_upload}")
    else:
        st.error(f"❌ {mensagem}")

# 
# FOOTER
# 

st.divider()
st.caption(FOOTER_COPYRIGHT)
st.caption(FOOTER_VERSAO)