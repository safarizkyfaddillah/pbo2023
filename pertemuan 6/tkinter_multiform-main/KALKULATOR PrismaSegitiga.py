import tkinter as tk
from tkinter import ttk

def luas_segitiga(alas_segitiga, tinggi_segitiga):
    value = 0.5 * alas_segitiga * tinggi_segitiga
    entry_luas_segitiga.delete(0, tk.END)
    entry_luas_segitiga.insert(tk.END, value)

def luas_permukaan_prisma(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    value = 2 * alas_segitiga * tinggi_segitiga + 3 * alas_segitiga * tinggi_prisma
    entry_luas_permukaan_prisma.delete(0, tk.END)
    entry_luas_permukaan_prisma.insert(tk.END, value)

def volume(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
    value = luas_segitiga * tinggi_prisma
    entry_volume.delete(0, tk.END)
    entry_volume.insert(tk.END, value)

def hitung():
    alas_segitiga = float(entry_alas_segitiga.get())
    tinggi_segitiga = float(entry_tinggi_segitiga.get())
    tinggi_prisma = float(entry_tinggi_prisma.get())
    luas_segitiga(alas_segitiga, tinggi_segitiga)
    luas_permukaan_prisma(alas_segitiga, tinggi_segitiga, tinggi_prisma)
    volume(alas_segitiga, tinggi_segitiga, tinggi_prisma)

# Tk
window = tk.Tk()
window.title("Kalkulator Prisma Segitiga")
window.resizable(False, False)

# Frame
frame = ttk.Frame(window)
frame.pack(padx=10, pady=10)

# Alas Segitiga
label_alas_segitiga = ttk.Label(frame, text="Alas Segitiga")
label_alas_segitiga.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

entry_alas_segitiga = ttk.Entry(frame)
entry_alas_segitiga.grid(column=1, row=0, padx=10, pady=10)

# Tinggi Segitiga
label_tinggi_segitiga = ttk.Label(frame, text="Tinggi Segitiga")
label_tinggi_segitiga.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

entry_tinggi_segitiga = ttk.Entry(frame)
entry_tinggi_segitiga.grid(column=1, row=1, padx=10, pady=10)

# Tinggi Prisma
label_tinggi_prisma = ttk.Label(frame, text="Tinggi Prisma")
label_tinggi_prisma.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

entry_tinggi_prisma = ttk.Entry(frame)
entry_tinggi_prisma.grid(column=1, row=2, padx=10, pady=10)

# Button
button = ttk.Button(frame, text="Hitung", command=hitung)
button.grid(column=1, row=3, padx=10, pady=10)

# Output Luas Segitiga
label_luas_segitiga = ttk.Label(frame, text="Luas Segitiga")
label_luas_segitiga.grid(column=0, row=4, sticky=tk.W, padx=10, pady=10)

entry_luas_segitiga = ttk.Entry(frame)
entry_luas_segitiga.grid(column=1, row=4, padx=10, pady=10)

# Output Luas Permukaan Prisma
label_luas_permukaan_prisma = ttk.Label(frame, text="Luas Permukaan Prisma")
label_luas_permukaan_prisma.grid(column=0, row=5, sticky=tk.W, padx=10, pady=10)

entry_luas_permukaan_prisma = ttk.Entry(frame)
entry_luas_permukaan_prisma.grid(column=1, row=5, padx=10, pady=10)

# Output volume
label_volume = ttk.Label(frame, text="Volume")
label_volume.grid(column=0, row=6, sticky=tk.W, padx=10, pady=10)

entry_volume = ttk.Entry(frame)
entry_volume.grid(column=1, row=6, padx=10, pady=10)

window.mainloop()