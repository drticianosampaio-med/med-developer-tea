# 
# app.py — PÁGINA DE MANUTENÇÃO
# Sistema de Triagem Canabinoide TEA
# Data: 1 de abril de 2026
# Status: Manutenção Programada
# 

import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Triagem TEA - Em Manutenção",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS Customizado
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0D2818 0%, #1a3a2e 100%);
    }
    [data-testid="stMainBlockContainer"] {
        background: linear-gradient(135deg, #0D2818 0%, #1a3a2e 100%);
    }
    h1, h2, h3 {
        color: #D4C5B9 !important;
        font-weight: 600;
    }
    p, span {
        color: #E8E8E8 !important;
    }
    .maintenance-container {
        text-align: center;
        padding: 60px 20px;
        background-color: rgba(45, 90, 61, 0.2);
        border-radius: 12px;
        border: 2px solid #3D7A4D;
        margin: 40px 0;
    }
    .status-badge {
        display: inline-block;
        background-color: #F77F00;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: bold;
        margin-bottom: 20px;
        font-size: 14px;
    }
    .contact-info {
        background-color: rgba(61, 122, 77, 0.3);
        padding: 20px;
        border-radius: 8px;
        margin-top: 30px;
        border-left: 4px solid #52B788;
    }
    </style>
""", unsafe_allow_html=True)

# Conteúdo Principal
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<div class='maintenance-container'>", unsafe_allow_html=True)
    
    st.markdown("# 🧠 Triagem TEA")
    st.markdown("## Terapia Canabinoide em Autismo Infantil")
    
    st.markdown("<div class='status-badge'>🔧 EM MANUTENÇÃO</div>", unsafe_allow_html=True)
    
    st.markdown("""
    ### Estamos Trabalhando Para Você
    
    Nosso sistema está passando por **manutenção programada** para garantir a melhor experiência e segurança dos seus dados.
    
    **Atividades em Andamento:**
    - ✅ Configuração de banco de dados seguro
    - ✅ Validação de formulários clínicos
    - ✅ Testes de conformidade LGPD
    - ⏳ Integração final com Supabase
    
    **Tempo Estimado de Retorno:** 24-48 horas
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### Sobre Este Sistema
    
    Este é um **sistema de triagem digital** para pacientes pediátricos com Transtorno do Espectro Autista (TEA) 
    que desejam iniciar **terapia com canabinoides**.
    
    O formulário coleta dados clínicos estruturados seguindo protocolos científicos validados, 
    garantindo:
    - 🔒 **Segurança**: Criptografia e conformidade LGPD
    - 📋 **Rigor Clínico**: Dados estruturados e validados
    - 🎯 **Precisão**: Avaliação inicial detalhada
    """)
    
    st.markdown("---")
    
    st.markdown("""
    <div class='contact-info'>
    <h3 style='color: #D4C5B9; margin-top: 0;'>Dúvidas ou Sugestões?</h3>
    
    **Dr. Ticiano Sampaio**  
    CRM-CE 20130 | Medicina de Família | Terapia Canabinoide
    
    📱 [WhatsApp](https://wa.me/5585920038130?text=Olá%20Dr.%20Ticiano!%20Tenho%20dúvidas%20sobre%20o%20sistema%20de%20triagem.)
    
    📧 [Email](mailto:drticianosamapaio@gmail.com)
    
    🌐 [Website](https://drticianosamapaio.com.br)
    
    📸 [@drticianosampaio](https://www.instagram.com/drticianosampaio)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<p style='text-align: center; color: #D4C5B9; font-size: 12px;'>
© 2026 Dr. Ticiano Sampaio. Todos os direitos reservados.<br>
Sistema de Triagem TEA — Versão 1.0 (Manutenção)<br>
Última atualização: 1 de abril de 2026
</p>
""", unsafe_allow_html=True)