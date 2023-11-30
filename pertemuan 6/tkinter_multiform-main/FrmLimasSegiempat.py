from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import tkinter as tk
from tkinter import ttk
import math

class FrmLimasSegiempat:
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
        Label(mainFrame, text='Panjang:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Limas:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Lebar:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="volume:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtPanjang = Entry(mainFrame) 
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggi_Limas = Entry(mainFrame) 
        self.txtTinggi_Limas.grid(row=1, column=1, padx=5, pady=5)
        self.txtLebar = Entry(mainFrame) 
        self.txtLebar.grid(row=2, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=3, column=1, padx=5, pady=5)  
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5) 
        self.txtvolume = Entry(mainFrame) 
        self.txtvolume.grid(row=6, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=4, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan volume bola  
    def onHitung(self, event=None):
        panjang = int(self.txtPanjang.get())
        tinggi_limas = int(self.txtTinggi_Limas.get())
        lebar = int(self.txtLebar.get())
        tinggi = int(self.txtTinggi.get())
        luas =  panjang * lebar + 2 * (panjang * tinggi_limas / 2) + 2 * (lebar * tinggi_limas / 2)
        volume = (1/3) * panjang * lebar * tinggi
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
        self.txtvolume.delete(0,END)
        self.txtvolume.insert(END,str(volume))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLimasSegiempat(root, "Program Luas dan volume segiaempat")
    root.mainloop() 