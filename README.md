# ❤️ CMD Lyrical Audio Player  
A colorful, encrypted, neon-animated command-line audio player for Windows — built using Python, Pygame, and Fernet encryption.

This project plays **encrypted audio**, shows **live-synced lyrics**, and displays them with **RGB neon glow effects** inside the Windows CMD.  
Includes a beautiful **pixel-style heart icon** for EXE builds.

---

## ✨ Features

### 🔐 Encrypted Audio Playback
- Audio stored as `audio.enc` (AES/Fernet)
- Fully protected — original audio is never exposed
- Decrypted only in memory at runtime

### 🌈 Neon RGB Lyrics Animation
- Smooth neon glow effect for each lyric line  
- Timestamp-based lyric syncing  
- Works in console & EXE builds

### ❤️ Heart Intro Banner
- Displays a centered heart at program start  
- Styled CMD color background and custom fonts

### 🧹 No Temp File Leftovers
- Uses secure temporary files  
- Automatic cleanup via signal/atexit  
- Deletes on Q exit, crash exit, or normal exit

### 🖥️ CMD Customization
- Custom colors  
- Custom fonts (Consolas / Cascadia Code)  
- Clean console (pygame banner hidden)

### 🖼️ EXE with Custom Icon
Supports EXE builds with custom heart icon:

```
pyinstaller --onefile --console --icon=love.ico ^
  --add-data "audio;audio" --add-data "keys;keys" app.py
```

### 🧩 Fully EXE-Ready With resource_path()
Automatic path handling so EXE works anywhere.

---

## 📂 Project Structure

```
cmd-lyrical-audio-player/
│
├── app.py                  # Main player script
├── audio/
│   └── audio.enc           # Encrypted audio file
├── keys/
│   └── key.txt             # Fernet encryption key
├── love.ico                # EXE icon
├── requirements.txt        # Dependencies
├── app.spec                # PyInstaller build file
└── dist/                   # Generated EXE (after build)
```

---

## 🚀 How to Run (Source)

### 1. Create virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the player
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

(Installed automatically from requirements.txt)

---

## 🎧 Controls

| Key | Action |
|-----|--------|
| **Q** | Quit & cleanup |
| Auto | Plays audio + syncs lyrics |

---

## 🖤 Credits

Made with ❤️ by Rhythm Chauhan  
Pixel heart icon generated for this project.

---

## 📜 License  
This project is open-source under the MIT License.
