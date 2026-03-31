import streamlit as st

st.set_page_config(page_title="Manutenção — Triagem TEA", page_icon="🔧", layout="wide")

# CSS minimalista para manter o visual
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background-color: #0D2818;}
[data-testid="stMainBlockContainer"] {background-color: #0D2818;}
p, span, label {color: #E8E8E8 !important;}
h1, h2, h3 {color: #D4C5B9 !important;}
</style>
""", unsafe_allow_html=True)

# Sidebar com informações profissionais
with st.sidebar:
    st.markdown("---")
    st.markdown("### PLATAFORMA DE ACOMPANHAMENTO CLÍNICO")
    st.markdown("**Terapia Canabinoide + Dados + Precisão**")
    st.markdown("---")
    st.markdown("### Dr. Ticiano Sampaio")
    st.write("**CRM-CE 20130**")
    st.write("Medicina de Família • Terapia Canabinoide")
    st.markdown("---")
    st.write("**CONECTE-SE**")
    st.markdown("[🌐 Site: drticianosamapaio.com.br](https://drticianosamapaio.com.br)")
    st.markdown("[📱 Instagram: @drticianosampaio](https://www.instagram.com/drticianosampaio?igsh=MW50b3gzcm16OXA0dg==)")
    st.markdown("[📧 Contato: drticianosamapaio@gmail.com](mailto:drticianosamapaio@gmail.com)")
    st.markdown("[💬 WhatsApp](https://wa.me/5585920038130?text=Gostaria+de+agendar+uma+consulta.)")
    st.markdown("---")
    st.write("**CONFORMIDADE E SEGURANÇA**")
    st.write("🔒 Dados protegidos conforme LGPD 13.709/2018")
    st.markdown("---")
    st.caption("© 2026 Dr. Ticiano Sampaio. Todos os direitos reservados.")
    st.caption("v1.0 — Sistema de Triagem TEA")

# Mensagem principal de manutenção
st.title("🔧 Manutenção Programada")
st.subheader("Sistema de Triagem TEA em Atualização")

st.write("""
O sistema está passando por melhorias técnicas para garantir maior estabilidade e segurança na coleta de dados clínicos.

**O que está sendo feito:**
- Otimização da integração com banco de dados
- Correções de validações e fluxos
- Melhorias na interface de usuário

**Tempo estimado:** 1-2 horas (retorno previsto para hoje).

**Enquanto isso:**
- Para agendar consultas ou esclarecimentos, entre em contato via WhatsApp ou e-mail (links na sidebar).
- Se precisar de orientação imediata, responda a esta mensagem.

Agradecemos pela compreensão e paciência.
""")

st.info("📞 Para urgências clínicas, ligue: (85) 9 9200-3813")

st.divider()
st.caption("Atualização em andamento | 31 de março de 2026")