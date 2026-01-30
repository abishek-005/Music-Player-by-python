import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"

import warnings
warnings.filterwarnings("ignore")

import pygame

def play(s):
    print(s)

folder_path=input("enter the folder path contains musics:")

if os.path.exists(folder_path):
    print("path found :)")
    mp3_files=[file for file in os.listdir(folder_path) if file.endswith(".mp3")]
    for index,song in enumerate(mp3_files,start=1):
        print(f"{index}.{song}")
    while True:
        i=input("which song do u want to play nter the number :) (to QUIT Q):")
        if i.upper()=="Q":
            break
        else:
            try:
                i=int(i)
                if 1 <=i <=len(songs):
                    sgtp=mp3_files[i-1]
                    play(sgtp)
                else:
                    print("index not found please enter a valid index")
            except ValueError :
                print("invalid input please enter valid input Q")
else:
    print("not found :(")