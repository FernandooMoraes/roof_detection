import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np
import cv2
def show_model_page():
    # Substitua pelo caminho correto do seu arquivo de modelo
    model_path = 'https://github.com/FernandooMoraes/roof_detection/raw/main/yolo12.pt'

    st.title('Application to identify problems on building roofs')

    # Criando a barra lateral
    with st.sidebar:
        st.header("Image")  # Adicionando cabeçalho à barra lateral
        # Adicionando o uploader de arquivo à barra lateral para selecionar imagens
        source_img = st.file_uploader("Choose an image...", type=("jpg", "jpeg", "png", "bmp", "webp"))

    # Criando duas colunas na página principal
    col1, col2 = st.columns(2)

    # Adicionando a imagem à primeira coluna se a imagem for enviada
    if source_img:
        # Abrindo a imagem enviada
        uploaded_image = Image.open(source_img)
        # Adicionando a imagem enviada à página com uma legenda
        with col1:
            st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

        # Carregando o modelo
        try:
            model = YOLO(model_path)
        except Exception as ex:
            st.error(f"Unable to load model. Check the specified path: {model_path}")
            st.error(ex)
            model = None

        if model:
            if st.sidebar.button('Detect Objects'):
                # Convertendo a imagem para o formato adequado
                image_cv = np.array(uploaded_image)
                image_cv = cv2.cvtColor(image_cv, cv2.COLOR_RGB2BGR)

                # Fazendo a predição
                res = model.predict(image_cv, conf=0.5, iou=0.5)
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                with col2:
                    st.image(res_plotted, caption='Detected Image', use_container_width=True)
                    try:
                        with st.expander("Detection Results"):
                            for box in boxes:
                                st.write(f"Coordinates: {box.xywh}")
                    except Exception as ex:
                        st.error("Error displaying detection results.")
    else:
        st.warning("Please upload an image to proceed with object detection.")


