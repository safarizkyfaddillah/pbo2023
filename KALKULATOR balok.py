import tkinter as tk
from tkinter import ttk

def luas(panjang, lebar, tinggi):
    value = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    entry_luas.delete(0, tk.END)
    entry_luas.insert(tk.END, value)

def volume(panjang, lebar, tinggi):
    value = panjang * lebar * tinggi
    entry_volume.delete(0, tk.END)
    entry_volume.insert(tk.END, value)

def hitung():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    tinggi = float(entry_tinggi.get())
    luas(panjang, lebar, tinggi)
    volume(panjang, lebar, tinggi)

# Tk
window = tk.Tk()
window.title("Kalkulator Balok")
window.resizable(False, False)

# Frame
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10)

# Panjang
label_panjang = ttk.Label(frame, text="Panjang")
label_panjang.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

entry_panjang = ttk.Entry(frame)
entry_panjang.grid(column=1, row=0, padx=10, pady=10)

# Lebar
label_lebar = ttk.Label(frame, text="Lebar")
label_lebar.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

entry_lebar = ttk.Entry(frame)
entry_lebar.grid(column=1, row=1, padx=10, pady=10)

# Tinggi
label_tinggi = ttk.Label(frame, text="Tinggi")
label_tinggi.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

entry_tinggi = ttk.Entry(frame)
entry_tinggi.grid(column=1, row=2, padx=10, pady=10)

# Button
button = ttk.Button(frame, text="Hitung", command=hitung)
button.grid(column=1, row=3, padx=10, pady=10)

# Output Luas
label_luas = ttk.Label(frame, text="Luas")
label_luas.grid(column=0, row=4, sticky=tk.W, padx=10, pady=10)

entry_luas = ttk.Entry(frame)
entry_luas.grid(column=1, row=4, padx=10, pady=10)

# Output volume
label_volume = ttk.Label(frame, text="Volume")
label_volume.grid(column=0, row=5, sticky=tk.W, padx=10, pady=10)

entry_volume = ttk.Entry(frame)
entry_volume.grid(column=1, row=5, padx=10, pady=10)

window.mainloop()