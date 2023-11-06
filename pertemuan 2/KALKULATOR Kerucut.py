import tkinter as tk
from tkinter import ttk
import math

def luas(jari_jari, tinggi):
    value = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari**2 + tinggi**2))
    entry_luas.delete(0, tk.END)
    entry_luas.insert(tk.END, value)

def volume(jari_jari, tinggi):
    value = (1/3) * math.pi * jari_jari**2 * tinggi
    entry_volume.delete(0, tk.END)
    entry_volume.insert(tk.END, value)

def hitung():
    jari_jari = float(entry_jari_jari.get())
    tinggi = float(entry_tinggi.get())
    luas(jari_jari, tinggi)
    volume(jari_jari, tinggi)

# Tk
window = tk.Tk()
window.title("Kalkulator Kerucut")
window.resizable(False, False)

# Frame
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10)

# Jari-jari
label_jari_jari = ttk.Label(frame, text="Jari-jari")
label_jari_jari.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

entry_jari_jari = ttk.Entry(frame)
entry_jari_jari.grid(column=1, row=0, padx=10, pady=10)

# Tinggi
label_tinggi = ttk.Label(frame, text="Tinggi")
label_tinggi.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

entry_tinggi = ttk.Entry(frame)
entry_tinggi.grid(column=1, row=1, padx=10, pady=10)

# Button
button = ttk.Button(frame, text="Hitung", command=hitung)
button.grid(column=1, row=2, padx=10, pady=10)

# Output Luas
label_luas = ttk.Label(frame, text="Luas")
label_luas.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)

entry_luas = ttk.Entry(frame)
entry_luas.grid(column=1, row=3, padx=10, pady=10)

# Output volume
label_volume = ttk.Label(frame, text="Volume")
label_volume.grid(column=0, row=4, sticky=tk.W, padx=10, pady=10)

entry_volume = ttk.Entry(frame)
entry_volume.grid(column=1, row=4, padx=10, pady=10)

window.mainloop()