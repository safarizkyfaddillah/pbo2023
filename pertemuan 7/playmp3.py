import tkinter as tk
from playsound import playsound

def play_sound():
    mp3_file_path ="Musik1.mp3"
    playsound(mp3_file_path, True)

root = tk.Tk()
root.title("Sound Player App")

play_button = tk.Button (root, text="play Sound", command=play_sound)
play_button.pack(padx=40 , pady=20)

root.mainloop()