import streamlit as st
from paddleocr import PaddleOCR, draw_ocr
import cv2
import numpy as np
from PIL import Image

# Supported languages (add more languages as needed)
languages = {
    "English": "en",
    "Arabic": "ar"
}

# Default language
selected_lang = st.sidebar.selectbox("Select Language", list(languages.keys()))
lang_code = languages[selected_lang]

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang=lang_code, use_gpu=False)

# Streamlit app
st.title('OCR Image Processing with PaddleOCR')

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Convert the uploaded file to an OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
    
    # Display the uploaded image
    st.image(img, channels="BGR")

    # Save the uploaded image to a temporary file
    img_path = 'temp_img.jpg'
    cv2.imwrite(img_path, img)
    
    # Perform OCR
    result = ocr.ocr(img_path, cls=True)
    
    # Extract OCR results
    boxes = [detection[0] for line in result for detection in line]
    txts = [detection[1][0] for line in result for detection in line]
    scores = [detection[1][1] for line in result for detection in line]
    
    # Draw OCR results on the image
    image = Image.open(img_path).convert('RGB')
    
    # Set a valid font path for Arabic (adjust based on your system)
    if lang_code == "ar":
        font_path = 'fonts\Amiri-Regular.ttf'  # Example Arabic font path
    else:
        font_path = 'fonts\simfang.ttf'  # Default font path (adjust if needed)
    
    im_show = draw_ocr(image, boxes, txts, scores, font_path=font_path)
    im_show = Image.fromarray(im_show)
    
    # Save and display the processed image
    output_path = 'test.jpg'
    im_show.save(output_path)
    st.image(im_show, caption='Processed Image', use_column_width=True)
