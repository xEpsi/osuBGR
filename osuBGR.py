"""
osu! Background Replacer
This program replaces all osu! backgrounds with a custom image.
It can also restore the backgrounds to their original state.
"""

#------- SETTINGS

custom_image = r"osu.jpg" # if None, the program will prompt you to enter RGB values for a custom image
#   ^ example: custom_image = r"C:\Users\user\Desktop\image.png" (recommended resolution: 1920x1080)

mode = "replace" # replace, restore

import os
from PIL import Image
from colorama import Fore, Style
import logging

#------- LOGGING

logLevel = logging.INFO

sr = Style.RESET_ALL
logging.basicConfig(format=f"{Fore.LIGHTBLUE_EX}[%(asctime)s] [%(levelname)s] %(message)s{sr}", datefmt="%H:%M:%S", level=logging.INFO)
logging.addLevelName(logging.WARNING, f"{Fore.YELLOW}[WARNING]{sr}")
logging.addLevelName(logging.ERROR, f"{Fore.RED}[ERROR]{sr}")
logging.addLevelName(logging.CRITICAL, f"{Fore.RED}[CRITICAL]{sr}")
logging.addLevelName(logging.DEBUG, f"{Fore.BLUE}[DEBUG]{sr}")

osu_path = fr"C:\Users\{os.getlogin()}\AppData\Local\osu!"
songs_path = os.path.join(osu_path, "Songs")
logging.info(f"osu! path: {osu_path}")
logging.info(f"Songs path: {songs_path}")

#------- IMAGE
if mode == "replace":
    if not custom_image:
        logging.info(f"Custom image not specified, please enter RGB values: (From 0 -> 255){sr}")
        red, green, blue = None, None, None
    
        while red is None:
            try:
                red = int(input(f"{Fore.RED}Red:{sr} "))
            except ValueError:
                logging.error(f"Invalid value{sr}")
        while green is None:
            try:
                green = int(input(f"{Fore.GREEN}Green:{sr} "))
            except ValueError:
                logging.error(f"Invalid value{sr}")
        while blue is None:
            try:
                blue = int(input(f"{Fore.BLUE}Blue:{sr} "))
            except ValueError:
                logging.error(f"Invalid value{sr}")
                    
        logging.info(f"Creating image...{sr}")
        img = Image.new("RGB", (1920, 1080), color=(red, green, blue))
        imgname = f"custombg_{red}_{green}_{blue}.jpg"
        img.save(imgname)
        image_path = imgname
    else:
        if os.path.isfile(custom_image):
            image_path = custom_image
            logging.info(f"Using image at {custom_image}{sr}")
        else:
            logging.error(f"Image not found at {custom_image}{sr}")
            exit(1)
    
    
    
#------- CODE

import glob
import shutil

if mode == "replace":
    logging.info(f"Replacing backgrounds...{sr}")
    for song in glob.glob(os.path.join(songs_path, "*")):
        if os.path.isdir(song):
            logging.info(f"Song: {song}{sr}")
            for file in glob.glob(os.path.join(song, "*")):
                if os.path.isfile(file):
                    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                        logging.info(f"Background: {file}{sr}")
                        if not os.path.isfile(file + ".bak"):
                            shutil.copy(file, file + ".bak")
                            logging.debug(f"Created backup of {file}{sr}")
                        os.remove(file)
                        shutil.copy(image_path, file)
                        logging.debug(f"Replaced {file} with {image_path}{sr}")
elif mode == "restore":
    logging.info(f"Restoring backgrounds...{sr}")
    for song in glob.glob(os.path.join(songs_path, "*")):
        if os.path.isdir(song):
            logging.info(f"Song: {song}{sr}")
            for file in glob.glob(os.path.join(song, "*")):
                if os.path.isfile(file):
                    if file.endswith(".bak"):
                        logging.info(f"Background: {file}{sr}")
                        shutil.copy(file, file.replace(".bak", ""))
                        os.remove(file)
                        logging.info(f"Restored background{sr}")
else:
    logging.error(f"Invalid mode: {mode}{sr}")
    exit(1)
    
logging.info(f"Done!{sr}")
