import os
import gdown
import requests
from PIL import Image
import pytesseract
import pyperclip

# Reference: https://superuser.com/questions/1527929/where-did-windows-10-save-clipped-images-using-windows-key-shift-s
# SCREENSHOT_PATH = "C:\Users\Acer\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\TempState\ScreenClip"
WINDOWS_SS_PATH = os.getenv("LOCALAPPDATA") + "/Packages/"
WINDOWS_SS_SUB_FOLD = [f for f in os.listdir(WINDOWS_SS_PATH) if f.startswith("MicrosoftWindows.Client.")][0]
WINDOWS_SS_PATH += f"{WINDOWS_SS_SUB_FOLD}/TempState/ScreenClip"

LANGS = ["ENGLISH", "TRADITIONAL CHINESE", "SIMPLIFIED CHINESE", "KOREAN", "JAPANESE"]
LANGS_KEY = ["eng", "chi_tra", "chi_sim", "kor", "jpn"]
SELECTIONS = "\n".join([f"{str(i+1)}. {l}" for i, l in enumerate(LANGS)])

IMG_EXT = ["png", "jpg", "jpeg", "tiff", "bmp", "webp"]
DOWNLOAD_DIR  = "temp"
BASEPATH = os.path.abspath(".")

if not os.path.isdir(DOWNLOAD_DIR):
    os.mkdir(DOWNLOAD_DIR)

while True:

    try:
        choice = int(input(f"\nLanguages available:\n{SELECTIONS}\nInput [Type 0 to quit]: "))
        if choice == 0:
            break
        elif not (0 < choice <= len(LANGS)):
            print(f"Enter between 1 and {len(LANGS)}")
            continue
    except:
        continue

    img_path = input("\nFilepath or URL [ENTER TO USE RECENT SCREENSHOT / CTRL + C TO QUIT]: ").replace('"', "").replace("\\", "/")

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
        tmp_url = img_path.lower()
        if tmp_url.startswith("http"):
            for ex in IMG_EXT:
                if tmp_url.endswith(ex):
                    # Download the file
                    filename = tmp_url.split("/")[-1]
                    ext = os.path.splitext(filename)[1].lower()
                    response = requests.get(img_path, stream=True)
                    
                    if response.ok:
                        img_path = f"{DOWNLOAD_DIR}/{filename}" 
                        with open(img_path, "wb") as fd:
                            for chunk in response.iter_content(2000):
                                fd.write(chunk)
                    else:
                        print(f"ERROR: CONNECTION ERROR {img_path}")
                    
                    break


            if img_path.lower().startswith("https://drive.google.com/file/d/"):
                try:
                    # Donwload the Google file
                    os.chdir(DOWNLOAD_DIR)
                    filename = gdown.download(url=img_path, quiet=True, fuzzy=True, use_cookies=False)
                    img_path = f"{DOWNLOAD_DIR}/{filename}"
                    os.chdir(BASEPATH)

                    # Getting the latest file and 
                except Exception as e:
                    print(e)

        try:
            img = Image.open(img_path).convert("1")
        except Exception as e:
            print("File not supported, only image files are supported.\n")
            continue

    # Available langauges: eng, kor, jpn, chi_tra, chi_sim
    text = pytesseract.image_to_string(img, lang=LANGS_KEY[choice-1])
    print(text)
    print("\n-------------------------------------------------")

    pyperclip.copy(text)
    print("Copied to clipboard")