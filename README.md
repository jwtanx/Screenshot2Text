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
1. Install Tesseract
```sh
sudo apt update
sudo add-apt-repository ppa:alex-p/tesseract-ocr-devel
sudo apt install -y tesseract-ocr
sudo apt update
tesseract -–version
```
2. Create Python virtual environment and activate it
```sh
python3.10 -m venv env
. env/bin/activate
```
3. Install dependencies
```sh
pip install -r requirements.txt
```
4. For more languages
   - Method 1: Download at https://github.com/tesseract-ocr/tessdata, then copy the file to `/usr/share/tesseract-ocr/<version>/tessdata`
   - Method 2: `sudo apt-get install tesseract-ocr-[lang]`

5. For simplicity of opening it, add a new shortcut with you own custom key
   ```gnome-terminal --window-with-profile=Mini -x bash -c 'cd /home/<username>/Desktop/personal/Screenshot2Text ; source <venv-name>/bin/activate ; python ocr.py ; deactivate'```
   - Optional: `--window-with-profile=Mini`
   - Reference: https://askubuntu.com/questions/1072688/what-is-the-difference-between-the-e-and-x-options-for-gnome-terminal

### Mac OS Setup
1. Install Tesseract
```zsh
brew install tesseract
tesseract --list-langs
```
2. Create Python virtual environment and activate it
```sh
python3.12 -m venv env
. env/bin/activate
```
3. Install dependencies
```sh
pip3 install -r requirements.txt
```
4. To install the all languages
```zsh
brew install tesseract --all-languages 
```
OR copy the required files from this [folder](./langs) to /opt/homebrew/share/tessdata/
5. Adding alias for executing the script from terminal since there is no keyboard shortcut like Linux where you can open the terminal explicitly and run the script
```zsh
# Add this line into ~/.zshrc
alias ocr='cd ~/PATH/TO/Screenshot2Text ; env/bin/python3 ocr.py'
```

## How to use?
1. Run the script
2. Enter to use the recent screenshot image to convert OR paste the image filepath
3. The output will be copied to your clipboard directly

## Future work
- [x] URL images
- [x] Google drive link
- [x] Compatible for Linux
- [x] Compatible for Mac OS
- [ ] PyQt a simple UI
- [ ] Google Chrome and Firefox extension for extracting the text
- [ ] Preprocess the image by inverting the dark image into bright image for better tesseract extraction.
- [ ] Multimodel image description generation
- [ ] LLM for answering simple question in PyQt