from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import tkinter as tk
from tkinter import ttk
import math

class FrmLimasSegitiga:
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
        Label(mainFrame, text='Panjang Alas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Segitiga:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Limas:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtPanjang_alas = Entry(mainFrame) 
        self.txtPanjang_alas.grid(row=0, column=1, padx=5, pady=5)
        self.txttinggi_segitiga = Entry(mainFrame) 
        self.txttinggi_segitiga.grid(row=1, column=1, padx=5, pady=5)
        self.txttinggi_limas = Entry(mainFrame) 
        self.txttinggi_limas.grid(row=2, column=1, padx=5, pady=5)  
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        self.txtvolume = Entry(mainFrame) 
        self.txtvolume.grid(row=5, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan volume bola  
    def onHitung(self, event=None):
        panjang_alas = int(self.txtPanjang_alas.get())
        tinggi_segitiga = int(self.txttinggi_segitiga.get())
        tinggi_limas = int(self.txttinggi_limas.get())
        luas = (panjang_alas * tinggi_segitiga) + (3 * (1 / 2) * panjang_alas * tinggi_limas)
        volume = (1 / 3) * (1 / 2) * panjang_alas * tinggi_segitiga * tinggi_limas
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
        self.txtvolume.delete(0,END)
        self.txtvolume.insert(END,str(volume))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLimasSegitiga(root, "Program Luas dan volume Limas Segitiga")
    root.mainloop() 