import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from data_obat import data_obat

class Formdata_obat:   
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
        Label(mainFrame, text='NAMA_OBAT:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtNAMA_OBAT = Entry(mainFrame) 
        self.txtNAMA_OBAT.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNAMA_OBAT.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='JENIS_OBAT:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtJENIS_OBAT = Entry(mainFrame) 
        self.txtJENIS_OBAT.grid(row=1, column=1, padx=5, pady=5)
                
        Label(mainFrame, text='KETERANGAN:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtKETERANGAN = StringVar()
        CboKETERANGAN = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtKETERANGAN) 
        CboKETERANGAN.grid(row=2, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboKETERANGAN['values'] = ('text')
        CboKETERANGAN.current()

        Label(mainFrame, text='HARGA:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtHARGA = Entry(mainFrame) 
        self.txtHARGA.grid(row=3, column=1, padx=5, pady=5)
                
        Label(mainFrame, text='STOK:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtSTOK = Entry(mainFrame) 
        self.txtSTOK.grid(row=4, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','nama_obat','jenis_obat','keterangan','harga','stok')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="40")
        self.tree.heading('nama_obat', text='nama_obat')
        self.tree.column('nama_obat', width="150")
        self.tree.heading('jenis_obat', text='jenis_obat')
        self.tree.column('jenis_obat', width="100")
        self.tree.heading('keterangan', text='keterangan')
        self.tree.column('keterangan', width="680")
        self.tree.heading('harga', text='harga')
        self.tree.column('harga', width="140")
        self.tree.heading('stok', text='stok')
        self.tree.column('stok', width="50")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA_OBAT.delete(0,END)
        self.txtNAMA_OBAT.insert(END,"")
                                
        self.txtJENIS_OBAT.delete(0,END)
        self.txtJENIS_OBAT.insert(END,"")
                                
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,"")
                                
        self.txtSTOK.delete(0,END)
        self.txtSTOK.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data data_obat
        obj = data_obat()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        nama_obat = self.txtNAMA_OBAT.get()
        obj = data_obat()
        res = obj.getByNAMA_OBAT(nama_obat)
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
        nama_obat = self.txtNAMA_OBAT.get()
        obj = data_obat()
        res = obj.getByNAMA_OBAT(nama_obat)
            
        self.txtJENIS_OBAT.delete(0,END)
        self.txtJENIS_OBAT.insert(END,obj.jenis_obat)
                                
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,obj.harga)
                                
        self.txtSTOK.delete(0,END)
        self.txtSTOK.insert(END,obj.stok)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        nama_obat = self.txtNAMA_OBAT.get()
        jenis_obat = self.txtJENIS_OBAT.get()
        keterangan = self.txtKETERANGAN.get()
        harga = self.txtHARGA.get()
        stok = self.txtSTOK.get()       
        obj = data_obat()
        obj.nama_obat = nama_obat
        obj.jenis_obat = jenis_obat
        obj.keterangan = keterangan
        obj.harga = harga
        obj.stok = stok
        if(self.ditemukan==True):
            res = obj.updateByNAMA_OBAT(nama_obat)
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
        nama_obat = self.txtNAMA_OBAT.get()
        obj = data_obat()
        obj.nama_obat = nama_obat
        if(self.ditemukan==True):
            res = obj.deleteByNAMA_OBAT(nama_obat)
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
    aplikasi = Formdata_obat(root, "Aplikasi Data Obat")
    root.mainloop() 