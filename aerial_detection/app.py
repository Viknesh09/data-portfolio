import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
import os
from ultralytics import YOLO

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="Aerial AI Intelligence System",
    page_icon="🛰️",
    layout="wide"
)

# ============================================
# PREMIUM UI STYLE
# ============================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

/* Main Title */
.main-title {
    font-size: 52px;
    font-weight: bold;
    color: #00FFE7;
    text-align: center;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    font-size: 24px;
    text-align: center;
    color: #FFFFFF;
    margin-bottom: 30px;
}

/* Card Style */
.card {
    background-color: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 25px rgba(0,0,0,0.3);
}

/* Footer */
.footer {
    text-align: center;
    font-size: 16px;
    color: #CCCCCC;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)

IMG_SIZE = (224, 224)

# ============================================
# LOAD CLASSIFICATION MODEL
# ============================================
@st.cache_resource
def load_classifier():

    model_path = r"D:\Guvi\Projects\Aerial_detection\models\bird_drone_model2.h5"

    if not os.path.exists(model_path):
        st.error(f"❌ Classification model not found:\n{model_path}")
        return None

    return tf.keras.models.load_model(model_path)

# ============================================
# LOAD YOLO MODEL
# ============================================
@st.cache_resource
def load_yolo():

    yolo_path = r"D:\Guvi\Projects\Aerial_detection\models\best.pt"

    if not os.path.exists(yolo_path):
        st.warning("⚠️ YOLO model not found. Detection disabled.")
        return None

    return YOLO(yolo_path)

classifier = load_classifier()
yolo_model = load_yolo()

# ============================================
# IMAGE PREPROCESS
# ============================================
def preprocess_image(image):

    image = image.resize(IMG_SIZE)

    img_array = np.array(image) / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    return img_array

# ============================================
# HEADER
# ============================================
st.markdown(
    '<div class="main-title">🛰️ Aerial Object Intelligence System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">🔍 Bird 🐦 vs Drone 🚁 Classification + YOLOv8 Detection</div>',
    unsafe_allow_html=True
)

# ============================================
# MAIN LAYOUT
# ============================================
col1, col2 = st.columns([1, 1])

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "📤 Upload Aerial Image",
        type=["jpg", "jpeg", "png"]
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.info("""
    ✅ Upload an aerial image
    
    ✅ CNN Classification
    
    ✅ YOLOv8 Object Detection
    
    ✅ Real-Time AI Prediction
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# PREDICTION SECTION
# ============================================
if uploaded_file is not None and classifier is not None:

    image = Image.open(uploaded_file).convert("RGB")

    # ========================================
    # DISPLAY IMAGE
    # ========================================
    st.markdown("## 📷 Uploaded Image")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # ========================================
    # CLASSIFICATION
    # ========================================
    st.markdown("## 🧠 Classification Result")

    processed_image = preprocess_image(image)

    prediction = classifier.predict(processed_image)[0][0]

    drone_probability = float(prediction)

    bird_probability = 1 - drone_probability

    confidence = max(drone_probability, bird_probability)

    if prediction > 0.5:

        st.error(
            f"🚁 Drone Detected | Confidence: {drone_probability:.2%}"
        )

    else:

        st.success(
            f"🐦 Bird Detected | Confidence: {bird_probability:.2%}"
        )

    st.progress(int(confidence * 100))

    # ========================================
    # YOLO DETECTION
    # ========================================
    st.markdown("## 🎯 YOLOv8 Object Detection")

    if yolo_model is not None:

        img_array = np.array(image)

        with st.spinner("Running YOLOv8 Detection..."):

            results = yolo_model(img_array)

            annotated_frame = results[0].plot()

        st.image(
            annotated_frame,
            caption="YOLOv8 Detection Output",
            use_container_width=True
        )

        # ====================================
        # DETECTION DETAILS
        # ====================================
        boxes = results[0].boxes

        if boxes is not None and len(boxes) > 0:

            st.markdown("### 📋 Detection Details")

            for box in boxes:

                cls_id = int(box.cls[0])

                conf = float(box.conf[0])

                class_name = yolo_model.names[cls_id]

                st.success(
                    f"✅ {class_name.upper()} detected with confidence {conf:.2%}"
                )

        else:

            st.warning("No objects detected.")

    else:

        st.warning("⚠️ YOLO model not loaded.")

# ============================================
# FOOTER
# ============================================
st.markdown("---")

st.markdown(
    '<div class="footer">🚀 Built with TensorFlow + YOLOv8 + Streamlit</div>',
    unsafe_allow_html=True
)