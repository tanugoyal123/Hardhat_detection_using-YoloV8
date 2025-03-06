from ultralytics import YOLO
import streamlit as st
import cv2
from PIL import Image

#for live detection
def live_detection(model):
        video_feed = st.empty()
        try:
            cap = cv2.VideoCapture(0)
        except Exception as e:
            st.error("Error: Unable to Access Webcam")
            return

        while cap.isOpened():
            success, frame = cap.read()
            if success:

                results = model.track(frame, persist=True, conf=0.5,
                                    max_det=6,classes = [0, 1, 2])


                processed_frame = results[0].plot()

                video_feed.image(processed_frame, caption='Detected Video.', channels="BGR",
                                use_container_width='auto', output_format='auto', width=None)
        cap.release()


# for video detection
def video_detection(uploaded_video,model):
        video_feed = st.empty()
        temp_video_path = f"temp/temp_{uploaded_video.name}"

        with open(temp_video_path, "wb") as temp_video_file:
            temp_video_file.write(uploaded_video.getvalue())

        cap = cv2.VideoCapture(temp_video_path)
        while cap.isOpened():
            success, frame = cap.read()
            if success:

                results = model.track(frame, persist=True, conf=0.5,
                                    max_det=6,classes = [0, 1, 2])

                processed_frame = results[0].plot()

                video_feed.image(processed_frame, caption='Detected Video.', channels="BGR",
                                use_column_width='auto', output_format='auto', width=None)
                
        cap.release()


#image detection        
def image_detect(uploaded_image,model):

    
    image = Image.open(uploaded_image)

    results = model.predict(image, conf=0.5,
                            max_det=6,classes=[0,1,2])

    plot = results[0].plot()

    processed_image = cv2.cvtColor(plot, cv2.COLOR_BGR2RGB)

    st.image(processed_image, caption='Detected Image.', use_column_width='auto', output_format='auto', width=None)
