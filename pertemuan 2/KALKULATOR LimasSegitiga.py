import tkinter as tk
from tkinter import ttk

def luas(panjang_alas, tinggi_segitiga, tinggi_limas):
    value = (panjang_alas * tinggi_segitiga) + (3 * (1 / 2) * panjang_alas * tinggi_limas)
    entry_luas.delete(0, tk.END)
    entry_luas.insert(tk.END, value)

def volume(panjang_alas, tinggi_segitiga, tinggi_limas):
    value = (1 / 3) * (1 / 2) * panjang_alas * tinggi_segitiga * tinggi_limas
    entry_volume.delete(0, tk.END)
    entry_volume.insert(tk.END, value)

def hitung():
    panjang_alas = float(entry_panjang_alas.get())
    tinggi_segitiga = float(entry_tinggi_segitiga.get())
    tinggi_limas = float(entry_tinggi_limas.get())
    luas(panjang_alas, tinggi_segitiga, tinggi_limas)
    volume(panjang_alas, tinggi_segitiga, tinggi_limas)

# Tk
window = tk.Tk()
window.title("Kalkulator Limas Segitiga")
window.resizable(False, False)

# Frame
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10)

# Panjang Alas
label_panjang_alas = ttk.Label(frame, text="Panjang Alas")
label_panjang_alas.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

entry_panjang_alas = ttk.Entry(frame)
entry_panjang_alas.grid(column=1, row=0, padx=10, pady=10)

# Tinggi Segitiga
label_tinggi_segitiga = ttk.Label(frame, text="Tinggi Segitiga")
label_tinggi_segitiga.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

entry_tinggi_segitiga = ttk.Entry(frame)
entry_tinggi_segitiga.grid(column=1, row=1, padx=10, pady=10)

# Tinggi Limas
label_tinggi_limas = ttk.Label(frame, text="Tinggi Limas")
label_tinggi_limas.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

entry_tinggi_limas = ttk.Entry(frame)
entry_tinggi_limas.grid(column=1, row=2, padx=10, pady=10)

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