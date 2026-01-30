import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"

import warnings
warnings.filterwarnings("ignore")

import pygame

folder_path=input("enter the folder path contains musics:")

if os.path.exists(folder_path):
    print("path found :)")
    mp3_files=[file for file in os.listdir(folder_path) if file.endswith(".mp3")]
    for index,song in enumerate(mp3_files,start=1):
        print(f"{index}.{song}")
else:
    print("not found :(")