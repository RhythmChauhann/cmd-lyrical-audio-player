<p align="center">
  <img src="banner.png" width="650">
</p>

# ❤️ CMD Lyrical Audio Player  

A colorful, encrypted, neon-animated command-line audio player for Windows — built using Python, Pygame, and Fernet encryption.

---

## 🔥 Badges

<p align="left">
  <a href="https://github.com/RhythmChauhann/cmd-lyrical-audio-player/stargazers">
    <img src="https://img.shields.io/github/stars/RhythmChauhann/cmd-lyrical-audio-player?style=for-the-badge&color=ff0066" />
  </a>
  <a href="https://github.com/RhythmChauhann/cmd-lyrical-audio-player/forks">
    <img src="https://img.shields.io/github/forks/RhythmChauhann/cmd-lyrical-audio-player?style=for-the-badge&color=00c8ff" />
  </a>
  <a href="https://github.com/RhythmChauhann/cmd-lyrical-audio-player/issues">
    <img src="https://img.shields.io/github/issues/RhythmChauhann/cmd-lyrical-audio-player?style=for-the-badge&color=ffcc00" />
  </a>
  <a href="https://github.com/RhythmChauhann/cmd-lyrical-audio-player/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/RhythmChauhann/cmd-lyrical-audio-player?style=for-the-badge&color=00ff88" />
  </a>
  <img src="https://img.shields.io/badge/python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/pygame-2.6.1-00cc66?style=for-the-badge&logo=python&logoColor=white" />
</p>

---

## ✨ Features

### 🔐 Encrypted Audio Playback
- Audio stored as `audio.enc` (AES/Fernet)
- Original audio is never exposed
- Decrypted only in memory using temporary files

### 🌈 Neon RGB Lyrics Animation
- Smooth neon glow effect for each lyric
- Timestamp-based lyric synchronization
- Works perfectly in both console & EXE builds

### ❤️ Heart Intro Banner
- Displays a centered pixel-art heart animation
- Matches retro CMD theme

### 🧹 Safe Temp File Cleanup
- Temporary decrypted audio auto-deletes
- Handles crashes, exits, Q-hotkey, and CTRL+C

### 🖥️ CMD Customization
- Custom background colors
- Custom fonts (Consolas / Cascadia Code)
- Hidden pygame banner for a clean look

### 🖼️ EXE with Custom Icon
Build EXE with love.ico:

```
pyinstaller --onefile --console --icon=love.ico ^
  --add-data "audio;audio" --add-data "keys;keys" app.py
```

### 🧩 EXE-Ready With resource_path()
Ensures correct file access inside PyInstaller executables.

---

## 📂 Project Structure

```
cmd-lyrical-audio-player/
│
├── app.py                  # Main program
├── audio/
│   └── audio.enc           # Encrypted audio file
├── keys/
│   └── key.txt             # Fernet key
├── love.ico                # Icon for EXE build
├── banner.png              # Pixel-art banner
├── requirements.txt        # Dependencies
└── dist/                   # EXE output (after build)
```

---

## 🚀 How to Run (From Source)

### 1. Create virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the program
```
python app.py
```

Press **Q** anytime to exit.

---

## 🏗️ Build the EXE

```
pyinstaller --onefile --console --icon=love.ico ^
  --add-data "audio;audio" --add-data "keys;keys" app.py
```

The EXE will appear in:

```
dist/app.exe
```

---

## 🔧 Requirements

```
pygame
cryptography
keyboard
```

---

## 🎧 Controls

| Key | Action |
|-----|--------|
| **Q** | Quit the player and clean temp files |
| Auto | Lyrics sync with audio |

---

## 🖤 Credits

Made with ❤️ by Rhythm Chauhan.  
Pixel-art banner & icon generated specifically for this repository.

---

## 📜 License  
MIT License  
