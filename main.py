import streamlit as st
from ultralytics import YOLO
import cv2
from utility_function import *

# For the title of streamlit app
st.set_page_config(page_title="Object Detection App", layout="wide")
st.title("🔍 Object Detection App")

#to chooose you want to model to detect in a live streaming , in video or in image
st.sidebar.title("Choose Detection Mode")
option = st.sidebar.radio("Select:", ["Image Detection", "Video Detection", "Live Detection"])

model = YOLO("runs/detect/train/weights/best.pt") 

if option == "Image Detection":
    st.subheader("📷 Image Detection")
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image_detect(uploaded_file,model)
elif option == "Video Detection":
    st.subheader("🎥 Video Detection")
    uploaded_video = st.file_uploader("Upload a video...", type=["mp4", "avi", "mov"])
    if uploaded_video:
        video_detection(uploaded_video,model)

elif option == "Live Detection":
    st.subheader("📹 Live Object Detection")
    live_detection(model)