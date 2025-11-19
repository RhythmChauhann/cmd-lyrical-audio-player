import uuid
import time
import threading
from cryptography.fernet import Fernet
import keyboard
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
import colorsys
import tempfile


import shutil
# import colorsys
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource (works for dev and for PyInstaller EXE) """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(relative_path)




def rgb_to_ansi(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
# os.system("color 57")
def print_rainbow(text, speed=0.05):
    hue = 0.0
    step = 0.02   # smaller = slower & smoother

    for char in text:
        # Convert hue → RGB
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        r, g, b = int(r*255), int(g*255), int(b*255)

        print(rgb_to_ansi(r, g, b, char), end="", flush=True)

        hue += step
        if hue > 1:
            hue = 0.0

        time.sleep(speed)  # delay between characters

    print()  # n


def load_key():
    path = resource_path("keys/key.txt")
    with open(path,"r") as f:
        return f.read().strip().encode()

LYRICS = {
    1: {"line": "Kyun Yun Sehte Sehte", "start": 0.5, "end": 3.98},
    2: {"line": "Dil Ko Gham Kha Chuka Meri Jaan", "start": 3.98, "end": 7.4},
    3: {"line": "Kyun Yun Rehte Rehte", "start": 7.4, "end": 10.7},
    4: {"line": "Dikhayi Na Koi Disha", "start": 10.7, "end": 14.50},
    5: {"line": "Kyun Yun Sehte Sehte", "start": 14.50, "end": 18.39},
    6: {"line": "Dil Ko Gham Kha Chuka Meri Jaan", "start": 18.39, "end":21.50  },
    7: {"line": "Kyun Yun Rehte Rehte", "start": 21.50, "end": 24.00},
    8: {"line": "Dikhayi Na Koi Disha", "start": 24.00, "end": 26.40},
    9: {"line": "Jo Tu Nahi Toh Aisa Main Chehra", "start": 26.40, "end": 30.00},
    10: {"line": "Ke Jiski Khoobsurti Maand Padti Ho", "start": 30.00, "end": 34.10},
    11: {"line": "Aisa Main Dariya Jo Behna Na Chahe", "start": 34.10, "end": 40.20},
    12: {"line": "Jo Tu Nahi Toh Aisa Main Chehra", "start": 40.20, "end": 42.3},
    13: {"line": "Ke Jiski Khoobsurti Maand Padti Ho", "start": 42.3, "end": 47.5},
    14: {"line": "Aisa Main Dariya Jo Behna Na Chahe", "start": 47.5, "end": 55.70}
}

stop_flag = False
temp_file_global = None


def play_audio():
    cypher = Fernet(load_key())
    audio_path = resource_path("audio/audio.enc")

    with open(audio_path, "rb") as f:
        enc_data = f.read()

    decrypted = cypher.decrypt(enc_data)

    # create temp file that auto deletes
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(decrypted)
        temp_name = tmp.name

    pygame.mixer.init()
    pygame.mixer.music.load(temp_name)
    pygame.mixer.music.play()

    # wait until playback or stop_flag
    while pygame.mixer.music.get_busy() and not stop_flag:
        time.sleep(0.05)

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.quit()

    # delete file safely
    try:
        os.remove(temp_name)
    except PermissionError:
        time.sleep(0.05)
        os.remove(temp_name)
def show_lyrics(start):
    global stop_flag
    printed = set()

    while not stop_flag:
        now = time.time() - start

        for key, block in LYRICS.items():
            if key not in printed and now >= block["start"]:
                print_rainbow("❤️"+block["line"], speed=0.01)

                printed.add(key)

        if len(printed) == len(LYRICS):
            break
        
        time.sleep(0.03)
    print('\n')
    print("Press Q to quit.")

def monitor_exit():
    global stop_flag, temp_file_global

    keyboard.wait("q")
    print("\n[EXIT] Q pressed. Stopping...\n")
    stop_flag = True

    # stop audio
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.quit()
    except:
        pass

    # delete temp file safely
    if temp_file_global and os.path.exists(temp_file_global):
        for _ in range(5):   # retry in case Windows still holds lock
            try:
                os.remove(temp_file_global)
                break
            except PermissionError:
                time.sleep(0.05)



if __name__ == "__main__":
    

    cols = shutil.get_terminal_size().columns
    heart = "❤️"

    print("\n" * 2)
    print(heart.center(cols))            # centered big heart
    print("\033[1;31m" + "♥".center(cols) + "\033[0m")  # matching smaller heart
    print("\n" * 1)
    print("\033[1;36m" + "Starting Music Player...".center(cols) + "\033[0m")
    print("\n" * 2)
    print("Listen to this...\n")
    print("Press Q to exit anytime.\n")

    start = time.time()

    t1 = threading.Thread(target=play_audio)
    t2 = threading.Thread(target=show_lyrics, args=(start,))
    t3 = threading.Thread(target=monitor_exit)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    stop_flag = True
