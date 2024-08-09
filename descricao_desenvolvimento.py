import streamlit as st

def show_description_page():
    st.title('Development Description')

    st.write('This application was developed with the aim of creating a YOLOv8 model for detecting damage in residential roofs. The images used for training and testing were collected through commercial drones.')
    # Descrição do que o modelo identifica

    st.header('Main Features:')
    st.write("""
    - **Open Trapdoor  Detection:** Identifies if there are open trapdoor in the installations.
    - **Extra Tile Detection:** Identifies the presence of extra tiles, which may indicate structural issues.
    - **Gutter Oxidation Detection:** Identifies signs of oxidation in the gutters, which may indicate wear or damage.
    """)

    st.write('The image below shows examples of roof anomalies covered in this research:')
   
    # Adicionando uma imagem de boas-vindas

    image_path = "examples.jpeg"
    st.image(image_path, caption="a) Extra tile on the roof, b) Gutter integrity (Oxidation), c) Open trapdoor.", use_column_width=True)

    st.write('The images below show examples of test set classifications.')
    
    image_path1 = "https://github.com/FernandooMoraes/roof_detection/tree/main/extra.jpeg"
    st.image(image_path1, caption="Test set classification for extra tiles.", use_column_width=True)

    image_path2 = "https://github.com/FernandooMoraes/roof_detection/tree/main/rufos.jpeg"
    st.image(image_path2, caption="Test set classification for oxidation.", use_column_width=True)

    image_path3 = "https://github.com/FernandooMoraes/roof_detection/tree/main/open.jpeg"
    st.image(image_path3, caption="Test set classification for open skylight.", use_column_width=True)

    # Adicionando uma imagem de exemplo
    #image_path = "path/to/your/image.jpg"
    #image = Image.open(image_path)
    #st.image(image, caption="Exemplos de anomalias de telhado contemplados desta pesquisa. a - Telha extra no telhado, b - Integridade das calhas (Oxidação) , c - Alçapão aberto", use_column_width=True)



    #st.write('## Os codigos desse aplicativo e da aplicação estão disponiveis em:')
    # Descrição do que o modelo identifica
    #st.write('Inserir onde estão disponiveis aqui')

    #st.write('## O artigo dessa pesquisa pode ser encontrado em:')
    # Descrição do que o modelo identifica
    #st.write('## Autores:')
