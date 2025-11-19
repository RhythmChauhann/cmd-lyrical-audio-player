from cryptography.fernet import Fernet

key =Fernet.generate_key()
cipher = Fernet(key)
print(f"The key in generated in txt file in worlking directory 💀")
key_to_save = key.decode()
with open("keys/key.txt","w") as file:
    file.write(key_to_save)
print("Key saved")

with open("audio/new_audio.wav","rb") as f:
    original = f.read()

encrypted = cipher.encrypt(original)

with open("audio/audio.enc","wb") as f:
    f.write(encrypted)

print(f"Encrypted file created in specified path")