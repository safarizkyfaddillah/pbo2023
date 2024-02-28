import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from data_pemeriksaan_pasien import data_pemeriksaan_pasien
from tkcalendar import Calendar, DateEntry

class Formdata_pemeriksaan_pasien:   
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.update_main_window = update_main_window
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
        # Label 
        Label(mainFrame, text='NAMA_PASIEN:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtNAMA_PASIEN = Entry(mainFrame) 
        self.txtNAMA_PASIEN.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNAMA_PASIEN.bind("<Return>",self.onCari) # menambahkan event Enter key
                
        Label(mainFrame, text='TANGGAL_PEMERIKSAAN:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtTANGGAL_PEMERIKSAAN = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL_PEMERIKSAAN.grid(row=1, column=1, padx=5, pady=5)
                    
        Label(mainFrame, text='KELUHAN:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtKELUHAN = Entry(mainFrame) 
        self.txtKELUHAN.grid(row=2, column=1, padx=5, pady=5)
                
        Label(mainFrame, text='DIAGNOSIS:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtDIAGNOSIS = Entry(mainFrame) 
        self.txtDIAGNOSIS.grid(row=3, column=1, padx=5, pady=5)
                
        Label(mainFrame, text='RESEP_OBAT:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtRESEP_OBAT = Entry(mainFrame) 
        self.txtRESEP_OBAT.grid(row=4, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','nama_pasien','tanggal_pemeriksaan','keluhan','diagnosis','resep_obat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="40")
        self.tree.heading('nama_pasien', text='nama_pasien')
        self.tree.column('nama_pasien', width="100")
        self.tree.heading('tanggal_pemeriksaan', text='tanggal_pemeriksaan')
        self.tree.column('tanggal_pemeriksaan', width="150")
        self.tree.heading('keluhan', text='keluhan')
        self.tree.column('keluhan', width="300")
        self.tree.heading('diagnosis', text='diagnosis')
        self.tree.column('diagnosis', width="150")
        self.tree.heading('resep_obat', text='resep_obat')
        self.tree.column('resep_obat', width="180")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA_PASIEN.delete(0,END)
        self.txtNAMA_PASIEN.insert(END,"")
                                
        self.txtKELUHAN.delete(0,END)
        self.txtKELUHAN.insert(END,"")
                                
        self.txtDIAGNOSIS.delete(0,END)
        self.txtDIAGNOSIS.insert(END,"")
                                
        self.txtRESEP_OBAT.delete(0,END)
        self.txtRESEP_OBAT.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data data_pemeriksaan_pasien
        obj = data_pemeriksaan_pasien()
        result = obj.getAlldata()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        nama_pasien = self.txtNAMA_PASIEN.get()
        obj = data_pemeriksaan_pasien()
        res = obj.getByNAMA_PASIEN(nama_pasien)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "data Ditemukan")
            self.Tampilkandata()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def Tampilkandata(self, event=None):
        nama_pasien = self.txtNAMA_PASIEN.get()
        obj = data_pemeriksaan_pasien()
        res = obj.getByNAMA_PASIEN(nama_pasien)
            
        self.txtTANGGAL_PEMERIKSAAN.delete(0,END)
        self.txtTANGGAL_PEMERIKSAAN.insert(END,obj.tanggal_pemeriksaan)
                                
        self.txtKELUHAN.delete(0,END)
        self.txtKELUHAN.insert(END,obj.keluhan)
                                
        self.txtDIAGNOSIS.delete(0,END)
        self.txtDIAGNOSIS.insert(END,obj.diagnosis)
                                
        self.txtRESEP_OBAT.delete(0,END)
        self.txtRESEP_OBAT.insert(END,obj.resep_obat)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        nama_pasien = self.txtNAMA_PASIEN.get()
        tanggal_pemeriksaan = self.txtTANGGAL_PEMERIKSAAN.get()
        keluhan = self.txtKELUHAN.get()
        diagnosis = self.txtDIAGNOSIS.get()
        resep_obat = self.txtRESEP_OBAT.get()       
        obj = data_pemeriksaan_pasien()
        obj.nama_pasien = nama_pasien
        obj.tanggal_pemeriksaan = tanggal_pemeriksaan
        obj.keluhan = keluhan
        obj.diagnosis = diagnosis
        obj.resep_obat = resep_obat
        if(self.ditemukan==True):
            res = obj.updateByNAMA_PASIEN(nama_pasien)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        nama_pasien = self.txtNAMA_PASIEN.get()
        obj = data_pemeriksaan_pasien()
        obj.nama_pasien = nama_pasien
        if(self.ditemukan==True):
            res = obj.deleteByNAMA_PASIEN(nama_pasien)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Formdata_pemeriksaan_pasien(root, "Aplikasi data data_pemeriksaan_pasien")
    root.mainloop()