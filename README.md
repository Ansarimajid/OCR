# OCR Image Processing with PaddleOCR

This project is a web application for Optical Character Recognition (OCR) using PaddleOCR and Streamlit. It allows users to upload an image and extract text from it in multiple languages with confidence scores.

## Features

- Support for multiple languages (currently English and Arabic).
- Displays uploaded image.
- Extracts and displays text with confidence scores.
- Provides an option to visualize OCR results on the image.

## Technologies Used

- [Streamlit](https://streamlit.io/): An open-source app framework for Machine Learning and Data Science.
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR): A rich repository for OCR models.
- [OpenCV](https://opencv.org/): A library for computer vision tasks.
- [NumPy](https://numpy.org/): A library for numerical computations.
- [PIL (Pillow)](https://python-pillow.org/): A library for image processing.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ansarimajid/OCR.git
   cd OCR
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the required PaddleOCR models:
   ```bash
   paddleocr --lang en  # for English
   paddleocr --lang ar  # for Arabic (if needed)
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Select the language from the sidebar.

4. Upload an image in PNG, JPG, or JPEG format.

5. View the uploaded image and the extracted text with confidence scores.

6. Optionally, visualize the OCR results on the image by checking the "Draw OCR Results on Image" checkbox.

## File Structure

- `app.py`: Main application file.
- `requirements.txt`: Contains the list of Python packages required for the project.
- `README.md`: Project documentation.
- `temp_img.jpg`: Temporary image file created during OCR processing.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
