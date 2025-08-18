import streamlit as st
from PIL import Image


def show_home_page():
    st.title('Welcome to the Object Detection Application using YOLOv12')

    st.write("""
    This application was developed to identify issues in building roofs using YOLOv12 object detection technology. 
    It enables automatic detection of damage and irregularities in residential roofs, helping with maintenance and prevention of larger problems.
     """)



    st.header('How to Navigate:')
    st.write("""
    - **Home:** You're here! This page provides an overview of the application.
    - **Model Usage:** Upload a roof image and use our YOLO11 model to detect potential issues.
    - **Development Description:** Learn more about the methodology used to develop this application in detail.
    """)

    st.header('Get Started Now:')
    st.write("""
    Use the sidebar to navigate between different sections of the application. 
    To start detecting roof issues, go to the **Model Usage** section and upload an image.
    """)

    st.write('We hope you have a great experience using our application!')

