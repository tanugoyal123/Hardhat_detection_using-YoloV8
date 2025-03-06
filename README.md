# Hard Hat Detection using YOLOv8 

This project trains a **YOLOv8** model on the **Hard Hat Dataset** to detect whether workers are wearing hard hats (Helmet), vest in real-time. The trained model is deployed using **Streamlit**, making it accessible via a web interface.

## Features
- **Real-time hard hat detection** using YOLOv8
- **Streamlit-based UI** for user-friendly interaction
- **Custom-trained model** using the Hard Hat Dataset
- **Supports image and video input**

---

## Demo  

[./output.jpg]
---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/tanugoyal123/hardhat-detection-yolov8.git
cd hardhat-detection-yolov8
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App  
```bash
streamlit run app.py
```


---

##  Results  
| Metric       | Value |
|-------------|-------|
| Precision   | 0.87  |
| Recall      | 0.83  |
| mAP@50      | 0.88  |



## 📝 Acknowledgments  
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)  
- [Hard Hat Detection Dataset](https://www.kaggle.com/datasets/muhammetzahitaydn/hardhat-vest-dataset-v3)


