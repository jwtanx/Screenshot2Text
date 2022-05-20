import os
import sys
from PIL import Image
import pytesseract
import pyperclip

# Reference: https://superuser.com/questions/1527929/where-did-windows-10-save-clipped-images-using-windows-key-shift-s
# SCREENSHOT_PATH = "C:\Users\Acer\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\TempState\ScreenClip"
WINDOWS_SS_PATH = os.getenv("LOCALAPPDATA") + "/Packages/"
WINDOWS_SS_SUB_FOLD = [f for f in os.listdir(WINDOWS_SS_PATH) if f.startswith("MicrosoftWindows.Client.")][0]
WINDOWS_SS_PATH += f"{WINDOWS_SS_SUB_FOLD}/TempState/ScreenClip"

img_path = input("Filepath [ENTER TO USE RECENT SCREENSHOT / CTRL + C TO QUIT]: ").replace('"', "").replace("\\", "/")

# Getting the most recent screenshot image
if img_path == "":
    img_path_list = [f for f in os.listdir(WINDOWS_SS_PATH) if f.endswith(".png")]
    img_path_list.sort(key=lambda f: os.path.getctime(f"{WINDOWS_SS_PATH}/{f}"), reverse=True)
    imgs = img_path_list[:2]

    img_1 = WINDOWS_SS_PATH + f"/{imgs[0]}"
    img_2 = WINDOWS_SS_PATH + f"/{imgs[1]}"
        
    # Comparing which files is the larger one
    img = img_1 if os.path.getsize(img_1) > os.path.getsize(img_2) else img_2

# Using the current paste filepath
else:
    try:
        img = Image.open(img_path).convert("1")
    except Exception as e:
        print("File not supported, only image files are supported.\n")
        os.execv(sys.argv[0], sys.argv)

text = pytesseract.image_to_string(img)
print(text)
print("\n-------------------------------------------------")

pyperclip.copy(text)
print("Copied to clipboard")