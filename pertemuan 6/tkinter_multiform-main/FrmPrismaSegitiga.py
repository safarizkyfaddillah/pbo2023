from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import tkinter as tk
from tkinter import ttk
import math

class FrmPrismaSegitiga:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Alas Segitiga:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Segitiga:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Prisma:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Segitiga:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Permukaan Prisma:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="volume:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtAlas_Segitiga = Entry(mainFrame) 
        self.txtAlas_Segitiga.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggi_Segitiga = Entry(mainFrame) 
        self.txtTinggi_Segitiga.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggi_Prisma = Entry(mainFrame) 
        self.txtTinggi_Prisma.grid(row=2, column=1, padx=5, pady=5)
        self.txtLuas_Segitiga = Entry(mainFrame) 
        self.txtLuas_Segitiga.grid(row=4, column=1, padx=5, pady=5)  
        self.txtLuas_Permukaan_Prisma = Entry(mainFrame) 
        self.txtLuas_Permukaan_Prisma.grid(row=5, column=1, padx=5, pady=5) 
        self.txtvolume = Entry(mainFrame) 
        self.txtvolume.grid(row=6, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan volume bola  
    def onHitung(self, event=None):
        alas_segitiga = int(self.txtAlas_Segitiga.get())
        tinggi_segitiga = int(self.txtTinggi_Segitiga.get())
        tinggi_prisma = int(self.txtTinggi_Prisma.get())
        luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
        luas_permukaan_prisma = 2 * alas_segitiga * tinggi_segitiga + 3 * alas_segitiga * tinggi_prisma
        volume = luas_segitiga * tinggi_prisma
        self.txtLuas_Segitiga.delete(0,END)
        self.txtLuas_Segitiga.insert(END,str(luas_segitiga))
        self.txtLuas_Permukaan_Prisma.delete(0,END)
        self.txtLuas_Permukaan_Prisma.insert(END,str(luas_permukaan_prisma))
        self.txtvolume.delete(0,END)
        self.txtvolume.insert(END,str(volume))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmPrismaSegitiga(root, "Program Luas dan Volume Prisma Segitiga")
    root.mainloop() 