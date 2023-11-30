from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
import tkinter as tk
from tkinter import ttk
import math

class FrmBola:
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
        Label(mainFrame, text='Jari-jari:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="volume:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtJarijari = Entry(mainFrame) 
        self.txtJarijari.grid(row=0, column=1, padx=5, pady=5)  
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=2, column=1, padx=5, pady=5) 
        self.txtvolume = Entry(mainFrame) 
        self.txtvolume.grid(row=3, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas dan volume bola  
    def onHitung(self, event=None):
        jarijari = int(self.txtJarijari.get())
        luas = 4 * math.pi * jarijari ** 2
        volume = (4/3) * math.pi * jarijari ** 3
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
        self.txtvolume.delete(0,END)
        self.txtvolume.insert(END,str(volume))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmBola(root, "Program Luas dan Volume bola")
    root.mainloop() 