import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from data_antrian import data_antrian
from tkcalendar import Calendar, DateEntry

class Formdata_antrian:   
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

        Label(mainFrame, text='NOMOR_ANTRIAN_PASIEN:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNOMOR_ANTRIAN_PASIEN = StringVar()
        CboNOMOR_ANTRIAN_PASIEN = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtNOMOR_ANTRIAN_PASIEN) 
        CboNOMOR_ANTRIAN_PASIEN.grid(row=1, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboNOMOR_ANTRIAN_PASIEN['values'] = ('001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020','021','022','023','024','025','026','027','028','029','030','031','032','033','034','035','036','037','038','039','040','041','042','043','044','045','046','047','048','049','050')
        CboNOMOR_ANTRIAN_PASIEN.current()

        Label(mainFrame, text='TANGGAL_ANTRI:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtTANGGAL_ANTRI = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL_ANTRI.grid(row=2, column=1, padx=5, pady=5)
                    
        Label(mainFrame, text='JAM_ANTRI:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtJAM_ANTRI = StringVar()
        CboJAM_ANTRI = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJAM_ANTRI) 
        CboJAM_ANTRI.grid(row=3, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboJAM_ANTRI['values'] = ("16:00","16:01","16:02","16:03","16:04","16:05","16:06","16:07","16:08","16:09","16:10","16:11","16:12","16:13","16:14","16:15","16:16","16:17","16:18","16:19","16:20","16:21","16:22","16:23","16:24","16:25","16:26","16:27","16:28","16:29","16:30","16:31","16:32","16:33","16:34","16:35","16:36","16:37","16:38","16:39","16:40","16:41","16:42","16:43","16:44","16:43","16:44","16:45","16:46","16:47","16:48","16:49","16:50","16:51","16:52","16:53","16:54","16:55","16:56","16:57","16:58","16:59","17:00","17:01","17:02","17:03","17:04","17:05","17:06","17:07","17:08","17:09","17:10","17:11","17:12","17:13","17:14","17:15","17:16","17:17","17:18","17:19","17:20","17:21","17:22","17:23","17:24","17:25","17:26","17:27","17:28","17:29","17:30","17:31","17:32","17:33","17:34","17:35","17:36","17:37","17:38","17:39","17:40","17:41","17:42","17:43","17:44","17:43","17:44","17:45","17:46","17:47","17:48","17:49","17:50","17:51","17:52","17:53","17:54","17:55","17:56","17:57","17:58","17:59","18:00","18:01","18:02","18:03","18:04","18:05","18:06","18:07","18:08","18:09","18:10","18:11","18:12","18:13","18:14","18:15","18:16","18:17","18:18","18:19","18:20","18:21","18:22","18:23","18:24","18:25","18:26","18:27","18:28","18:29","18:30","18:31","18:32","18:33","18:34","18:35","18:36","18:37","18:38","18:39","18:40","18:41","18:42","18:43","18:44","18:43","18:44","18:45","18:46","18:47","18:48","18:49","18:50","18:51","18:52","18:53","18:54","18:55","18:56","18:57","18:58","18:59","19:00","19:01","19:02","19:03","19:04","19:05","19:06","19:07","19:08","19:09","19:10","19:11","19:12","19:13","19:14","19:15","19:16","19:17","19:18","19:19","19:20","19:21","19:22","19:23","19:24","19:25","19:26","19:27","19:28","19:29","19:30","19:31","19:32","19:33","19:34","19:35","19:36","19:37","19:38","19:39","19:40","19:41","19:42","19:43","19:44","19:43","19:44","19:45","19:46","19:47","19:48","19:49","19:50","19:51","19:52","19:53","19:54","19:55","1:56","19:57","19:58","19:59","20:00")
        CboJAM_ANTRI.current()

        Label(mainFrame, text='STATUS:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtSTATUS = StringVar()
        CboSTATUS = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtSTATUS) 
        CboSTATUS.grid(row=4, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboSTATUS['values'] = ('Menunggu','Diproses','Selesai')
        CboSTATUS.current()
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','nama_pasien','nomor_antrian_pasien','tanggal_antri','jam_antri','status')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="40")
        self.tree.heading('nama_pasien', text='nama_pasien')
        self.tree.column('nama_pasien', width="100")
        self.tree.heading('nomor_antrian_pasien', text='nomor_antrian_pasien')
        self.tree.column('nomor_antrian_pasien', width="150")
        self.tree.heading('tanggal_antri', text='tanggal_antri')
        self.tree.column('tanggal_antri', width="150")
        self.tree.heading('jam_antri', text='jam_antri')
        self.tree.column('jam_antri', width="100")
        self.tree.heading('status', text='status')
        self.tree.column('status', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA_PASIEN.delete(0,END)
        self.txtNAMA_PASIEN.insert(END,"")
                                
        self.txtNOMOR_ANTRIAN_PASIEN.set("")
            
        self.txtSTATUS.set("")
            
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data data_antrian
        obj = data_antrian()
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
        obj = data_antrian()
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
        obj = data_antrian()
        res = obj.getByNAMA_PASIEN(nama_pasien)
            
        self.txtNOMOR_ANTRIAN_PASIEN.set(obj.nomor_antrian_pasien)
            
        self.txtTANGGAL_ANTRI.delete(0,END)
        self.txtTANGGAL_ANTRI.insert(END,obj.tanggal_antri)
                                
        self.txtSTATUS.set(obj.status)
            
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        nama_pasien = self.txtNAMA_PASIEN.get()
        nomor_antrian_pasien = self.txtNOMOR_ANTRIAN_PASIEN.get()
        tanggal_antri = self.txtTANGGAL_ANTRI.get()
        jam_antri = self.txtJAM_ANTRI.get()
        status = self.txtSTATUS.get()       
        obj = data_antrian()
        obj.nama_pasien = nama_pasien
        obj.nomor_antrian_pasien = nomor_antrian_pasien
        obj.tanggal_antri = tanggal_antri
        obj.jam_antri = jam_antri
        obj.status = status
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
        obj = data_antrian()
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
    aplikasi = Formdata_antrian(root, "Aplikasi Data data_antrian")
    root.mainloop() 