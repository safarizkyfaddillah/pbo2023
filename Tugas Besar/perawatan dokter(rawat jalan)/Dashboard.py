import tkinter as tk
from tkinter import Menu, messagebox
from FormLogin import *
from FrmData_Pasien import *
from FrmData_Antrian import *
from FrmData_Pemeriksaan_Pasien import *
from FrmData_Obat import *

class Dashboard:
    def __init__(self):
        # root window
        self.root = tk.Tk()
        self.root.title('Menu Demo')
        # self.root.attributes('-fullscreen', True)
        self.root.geometry("900x400")
        self.__data = None
        self.__level = None

        # create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # create menu
        self.file_menu = Menu(self.menubar)
        self.guest_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)
        self.apoteker_menu = Menu(self.menubar)
        self.dokter_menu = Menu(self.menubar)

        # add menu items to File menu
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.file_menu.add_command(label='Exit', command=self.root.destroy)

        # add menu items to menu Admin
        self.admin_menu.add_command(label='Data Pasien', command=lambda: self.new_window("Data Pasien", FormData_pasien))
        self.admin_menu.add_command(label='Data Antrian', command=lambda: self.new_window("Data Antrian", FormData_antrian))
        self.admin_menu.add_command(label='Data Pemeriksaan Pasien', command=lambda: self.new_window("Data Pemeriksaan Pasien", FormData_pemeriksaan_pasien))
        self.admin_menu.add_command(label='Data Obat', command=lambda: self.new_window("Data Obat", FormData_obat))

        # add menu items to menu apoteker
        self.apoteker_menu.add_command(label='Data Pasien', command=lambda: self.new_window("Data Pasien", FormData_pasien))
        self.apoteker_menu.add_command(label='Data Antrian', command=lambda: self.new_window("Data Antrian", FormData_antrian))
        self.apoteker_menu.add_command(label='Data Pemeriksaan Pasien', command=lambda: self.new_window("Data Pemeriksaan Pasien", FormData_pemeriksaan_pasien))
        self.apoteker_menu.add_command(label='Data Obat', command=lambda: self.new_window("Data Obat", FormData_obat))

        # add menu items to menu Dokter
        self.dokter_menu.add_command(label='Data Pasien', command=lambda: self.new_window("Data Pasien", FormData_pasien))
        self.dokter_menu.add_command(label='Data Antrian', command=lambda: self.new_window("Data Antrian", FormData_antrian))
        self.dokter_menu.add_command(label='Data Pemeriksaan Pasien', command=lambda: self.new_window("Data Pemeriksaan Pasien", FormData_pemeriksaan_pasien))
        self.dokter_menu.add_command(label='Data Obat', command=lambda: self.new_window("Data Obat", FormData_obat))

        # add menus to the menubar
        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def new_window(self, number, _class):
        new = tk.Toplevel(self.root)
        new.transient()
        new.grab_set()
        _class(new, number, self.update_main_window)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        level = self.__data[0]
        loginvalid = self.__data[1]
        if(loginvalid==True):
            index = self.file_menu.index('Login')
            # hapus menu login
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)

            # tambahkan menu sesuai level
            if(level=='admin'): 
                self.menubar.add_cascade(label="Admin", menu=self.admin_menu)
                self.__level = 'Admin'
            elif(level=='apoteker'): 
                self.menubar.add_cascade(label="Apoteker", menu=self.apoteker_menu)
                self.__level = 'Apoteker'
            elif(level=='dokter'):
                self.menubar.add_cascade(label="Dokter", menu=self.dokter_menu)
                self.__level = 'Dokter'
            else:
                pass

    def Logout(self):
        index = self.file_menu.index('Logout')
        self.file_menu.delete(index)
        self.file_menu.add_command(label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.remove_all_menus()

    def remove_all_menus(self):
        index = self.menubar.index(self.__level)
        if index is not None:
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()
