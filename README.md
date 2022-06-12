# Screenshot2Text
Using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## Main Functionality
- Converting the image using the image link pasted into text
- Converting the recent screenshotted image into text

### Windows Setup
1. Creating an virtual environment using Python >= 3.8  
   ```py 3.8 -m venv env```
2. Activate the env  
   ```env\Scripts\activate.bat```
3. Installing the Python libraries  
   ```pip install -r requirements.txt```
4. Download **unofficial** Tesseract for Windows: [tesseract-ocr-w64-setup-v5.1.0.20220510.exe (64 bit)](https://github.com/UB-Mannheim/tesseract/wiki)
5. Adding the path of [Tesseract](https://github.com/maxenxe/HQ-Trivia-Bot-NOT-MAINTAINED-/issues/51)
6. For simplicity, you can create a shortcut to your desktop and run this script
   1. For example:
   - Target: ```C:\Windows\System32\cmd.exe /K "D:\Project\Python\2022\Screenshot2Text\env\Scripts\activate.bat" && ocr.py```
   - Start in: ```D:\Project\Python\2022\Screenshot2Text```
7. For more languages, download at https://github.com/tesseract-ocr/tessdata and put those into the C:\Prorgam Files\Tesseract-OCR\tessdata

### Linux Setup
- Later in the future

## How to use?
1. Run the script
2. Enter to use the recent screenshot image to convert OR paste the image filepath
3. The output will be copied to your clipboard directly

## Future work
- [ ] PyQt a simple UI / Streamlit
- [ ] Compaitible for Linux
- [ ] Google Chrome and Firefox extension for extracting the text
- [ ] Preprocess the image by inverting the dark image into bright image for better tesseract extraction.