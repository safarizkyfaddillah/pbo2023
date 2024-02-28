import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from data_pasien import data_pasien
from tkcalendar import Calendar, DateEntry

class Formdata_pasien:   
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

        Label(mainFrame, text='ALAMAT:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtALAMAT = Entry(mainFrame) 
        self.txtALAMAT.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='TANGGAL_LAHIR:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtTANGGAL_LAHIR = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL_LAHIR.grid(row=2, column=1, padx=5, pady=5)

        Label(mainFrame, text='JENIS_KELAMIN:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtJENIS_KELAMIN = StringVar()
        CboJENIS_KELAMIN = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJENIS_KELAMIN) 
        CboJENIS_KELAMIN.grid(row=3, column=1, padx=5, pady=5)
        CboJENIS_KELAMIN['values'] = ('Laki-Laki','Perempuan')
        CboJENIS_KELAMIN.current()
        
        Label(mainFrame, text='NOMOR_TELEPON:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtNOMOR_TELEPON = Entry(mainFrame) 
        self.txtNOMOR_TELEPON.grid(row=4, column=1, padx=5, pady=5)
                
        Label(mainFrame, text='RIWAYAT_MEDIS:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.txtRIWAYAT_MEDIS = Entry(mainFrame) 
        self.txtRIWAYAT_MEDIS.grid(row=5, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','nama_pasien','alamat','tanggal_lahir','jenis_kelamin','nomor_telepon','riwayat_medis')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="40")
        self.tree.heading('nama_pasien', text='nama_pasien')
        self.tree.column('nama_pasien', width="100")
        self.tree.heading('alamat', text='alamat')
        self.tree.column('alamat', width="100")
        self.tree.heading('tanggal_lahir', text='tanggal_lahir')
        self.tree.column('tanggal_lahir', width="150")
        self.tree.heading('jenis_kelamin', text='jenis_kelamin')
        self.tree.column('jenis_kelamin', width="100")
        self.tree.heading('nomor_telepon', text='nomor_telepon')
        self.tree.column('nomor_telepon', width="150")
        self.tree.heading('riwayat_medis', text='riwayat_medis')
        self.tree.column('riwayat_medis', width="150")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA_PASIEN.delete(0,END)
        self.txtNAMA_PASIEN.insert(END,"")
                                
        self.txtALAMAT.delete(0,END)
        self.txtALAMAT.insert(END,"")
                                
        self.txtJENIS_KELAMIN.set("")
            
        self.txtNOMOR_TELEPON.delete(0,END)
        self.txtNOMOR_TELEPON.insert(END,"")
                                
        self.txtRIWAYAT_MEDIS.delete(0,END)
        self.txtRIWAYAT_MEDIS.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data data_pasien
        obj = data_pasien()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        nama_pasien = self.txtNAMA_PASIEN.get()
        obj = data_pasien()
        res = obj.getByNAMA_PASIEN(nama_pasien)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        nama_pasien = self.txtNAMA_PASIEN.get()
        obj = data_pasien()
        res = obj.getByNAMA_PASIEN(nama_pasien)
            
        self.txtALAMAT.delete(0,END)
        self.txtALAMAT.insert(END,obj.alamat)
                                
        self.txtTANGGAL_LAHIR.delete(0,END)
        self.txtTANGGAL_LAHIR.insert(END,obj.tanggal_lahir)
                                
        self.txtJENIS_KELAMIN.set(obj.jenis_kelamin)
            
        self.txtNOMOR_TELEPON.delete(0,END)
        self.txtNOMOR_TELEPON.insert(END,obj.nomor_telepon)
                                
        self.txtRIWAYAT_MEDIS.delete(0,END)
        self.txtRIWAYAT_MEDIS.insert(END,obj.riwayat_medis)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        nama_pasien = self.txtNAMA_PASIEN.get()
        alamat = self.txtALAMAT.get()
        tanggal_lahir = self.txtTANGGAL_LAHIR.get()
        jenis_kelamin = self.txtJENIS_KELAMIN.get()
        nomor_telepon = self.txtNOMOR_TELEPON.get()
        riwayat_medis = self.txtRIWAYAT_MEDIS.get()       
        obj = data_pasien()
        obj.nama_pasien = nama_pasien
        obj.alamat = alamat
        obj.tanggal_lahir = tanggal_lahir
        obj.jenis_kelamin = jenis_kelamin
        obj.nomor_telepon = nomor_telepon
        obj.riwayat_medis = riwayat_medis
        if(self.ditemukan==True):
            res = obj.updateByNAMA_PASIEN(nama_pasien)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        nama_pasien = self.txtNAMA_PASIEN.get()
        obj = data_pasien()
        obj.nama_pasien = nama_pasien
        if(self.ditemukan==True):
            res = obj.deleteByNAMA_PASIEN(nama_pasien)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Formdata_pasien(root, "Aplikasi Data data_pasien")
    root.mainloop() 