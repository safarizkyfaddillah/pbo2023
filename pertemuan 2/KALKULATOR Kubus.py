import tkinter as tk
from tkinter import ttk

def luas(sisi):
    value = 6 * sisi**2
    entry_luas.delete(0, tk.END)
    entry_luas.insert(tk.END, value)

def volume(sisi):
    value = sisi**3
    entry_volume.delete(0, tk.END)
    entry_volume.insert(tk.END, value)

def hitung():
    sisi = float(entry_sisi.get())
    luas(sisi)
    volume(sisi)

# Tk
window = tk.Tk()
window.title("Kalkulator Kubus")
window.resizable(False, False)

# Frame
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10)

# Sisi
label_sisi = ttk.Label(frame, text="Sisi")
label_sisi.grid(column=0, row=0, padx=10, pady=10)

entry_sisi = ttk.Entry(frame)
entry_sisi.grid(column=1, row=0, padx=10, pady=10)

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