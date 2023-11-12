import tkinter as tk
from tkinter import ttk
import math
from Fungsi import luas_bola,volume_bola

def luas(jari_jari):
    value = luas_bola(jari_jari)
    entry_luas.delete(0, tk.END)
    entry_luas.insert(tk.END, value)

def volume(jari_jari):
    value = volume_bola(jari_jari)
    entry_volume.delete(0, tk.END)
    entry_volume.insert(tk.END, value)

def hitung():
    jari_jari = float(entry_jari_jari.get())
    luas(jari_jari)
    volume(jari_jari)

# Tk
window = tk.Tk()
window.title("Kalkulator Bola")
window.resizable(False, False)

# Frame
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10)

# Jari-jari
label_jari_jari = ttk.Label(frame, text="Jari-jari")
label_jari_jari.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

entry_jari_jari = ttk.Entry(frame)
entry_jari_jari.grid(column=1, row=0, padx=10, pady=10)

# Button
button = ttk.Button(frame, text="Hitung", command=hitung)
button.grid(column=1, row=1, padx=10, pady=10)

# Output Luas
label_luas = ttk.Label(frame, text="Luas")
label_luas.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

entry_luas = ttk.Entry(frame)
entry_luas.grid(column=1, row=2, padx=10, pady=10)

# Output volume
label_volume = ttk.Label(frame, text="Volume")
label_volume.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)

entry_volume = ttk.Entry(frame)
entry_volume.grid(column=1, row=3, padx=10, pady=10)

window.mainloop()