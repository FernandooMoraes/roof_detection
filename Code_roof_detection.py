import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Object Detection using YOLO12",  # Título da página
    page_icon="🤖",     # Ícone da página
    layout="wide",      # Layout
    initial_sidebar_state="expanded"    # Barra lateral expandida por padrão
)

# Título da barra lateral e navegação
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home","Development Description", "Model"])

# Importa e mostra a página selecionada
if page == "Home":
    from home import show_home_page
    show_home_page()
elif page == "Model":
    from uso_modelo import show_model_page
    show_model_page()
else:
    from descricao_desenvolvimento import show_description_page
    show_description_page()

