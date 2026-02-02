import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"

import warnings
warnings.filterwarnings("ignore")

import pygame

def play(s,f):
    fp=os.path.join(f,s)

    if not os.path.exists(fp):
        print("file not found")
        return
    
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()

    print(f"\nNow playing:{s}")
    print("Commands: [P]ause, [R]esume, [S]top")

    while True:
        cmd=input("*").upper()
        if cmd == "P":
            pygame.mixer.music.pause()
            print("paused -_-")
        elif cmd =="R":
            pygame.mixer.music.unpause()
            print("resumed :)")
        elif cmd =="S":
            pygame.mixer.music.stop()
            print("stopped ~")
            return
        else:
            print("invalid input nter a valid input")


def main():
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
                if 1 <=i <=len(mp3_files):
                    sgtp=mp3_files[i-1]
                    play(sgtp,folder_path)
                else:
                    print("index not found please enter a valid index")
            except ValueError :
                print("invalid input please enter valid input Q")
    else:
        print("not found :(")

if __name__=="__main__":
    main()