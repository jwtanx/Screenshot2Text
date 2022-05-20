# Screenshot2Text
Using Tesseract OCR

## Main Functionality
- Converting the image using the image link pasted into text
- Converting the recent screenshotted image into text

# Windows Setup
1. Creating an virtual environment using Python >= 3.8  
   ```py 3.8 -m venv env```
2. Activate the env  
   ```env\Scripts\activate.bat```
3. Installing the Python libraries  
   ```pip install -r requirements.txt```
4. Download [tesseract-ocr-w64-setup-v5.1.0.20220510.exe (64 bit)](https://github.com/UB-Mannheim/tesseract/wiki)
5. Adding the path of [Tesseract](https://github.com/maxenxe/HQ-Trivia-Bot-NOT-MAINTAINED-/issues/51)
6. For simplicity, you can create a shortcut to your desktop and run this script
   1. For example:
   - Target: ```C:\Windows\System32\cmd.exe /K "D:\Project\Python\2022\Screenshot2Text\env\Scripts\activate.bat" && ocr.py```
   - Start in: ```D:\Project\Python\2022\Screenshot2Text```