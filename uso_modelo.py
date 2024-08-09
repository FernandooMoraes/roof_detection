import streamlit as st
from PIL import Image
from ultralytics import YOLO


def show_model_page():
    # Replace the relative path to your weight file
    model_path = 'https://github.com/FernandooMoraes/roof_detection/blob/main/best.pt'

    st.title('Application to identify problems on building roofs')

    # Creating sidebar
    with st.sidebar:
        st.header("Image")     # Adding header to sidebar
        # Adding file uploader to sidebar for selecting images
        source_img = st.file_uploader("Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    # Creating two columns on the main page
    col1, col2 = st.columns(2)

    # Adding image to the first column if image is uploaded
    if source_img:
        # Opening the uploaded image
        uploaded_image = Image.open(source_img)
        # Adding the uploaded image to the page with a caption
        with col1:
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # Load model
        try:
            model = YOLO(model_path)
        except Exception as ex:
            st.error(f"Unable to load model. Check the specified path: {model_path}")
            st.error(ex)
            model = None

        if model:
            if st.sidebar.button('Detect Objects'):
                res = model.predict(uploaded_image, conf=0.5, iou=0.5)
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                with col2:
                    st.image(res_plotted, caption='Detected Image', use_column_width=True)
                    try:
                        with st.expander("Detection Results"):
                            for box in boxes:
                                st.write(f"Coordinates: {box.xywh}")
                    except Exception as ex:
                        st.error("Error displaying detection results.")
    else:
        st.warning("Please upload an image to proceed with object detection.")
