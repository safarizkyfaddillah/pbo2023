from db import DBConnection as mydb

class data_pasien:
    def __init__(self):
        self.__id=None
        self.__nama_pasien=None
        self.__alamat=None
        self.__tanggal_lahir=None
        self.__jenis_kelamin=None
        self.__nomor_telepon=None
        self.__riwayat_medis=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def nama_pasien(self):
        return self.__nama_pasien
        
    @nama_pasien.setter
    def nama_pasien(self, value):
        self.__nama_pasien = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    @property
    def tanggal_lahir(self):
        return self.__tanggal_lahir
        
    @tanggal_lahir.setter
    def tanggal_lahir(self, value):
        self.__tanggal_lahir = value
    @property
    def jenis_kelamin(self):
        return self.__jenis_kelamin
        
    @jenis_kelamin.setter
    def jenis_kelamin(self, value):
        self.__jenis_kelamin = value
    @property
    def nomor_telepon(self):
        return self.__nomor_telepon
        
    @nomor_telepon.setter
    def nomor_telepon(self, value):
        self.__nomor_telepon = value
    @property
    def riwayat_medis(self):
        return self.__riwayat_medis
        
    @riwayat_medis.setter
    def riwayat_medis(self, value):
        self.__riwayat_medis = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama_pasien,self.__alamat,self.__tanggal_lahir,self.__jenis_kelamin,self.__nomor_telepon,self.__riwayat_medis)
        sql="INSERT INTO data_pasien (nama_pasien,alamat,tanggal_lahir,jenis_kelamin,nomor_telepon,riwayat_medis) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nama_pasien,self.__alamat,self.__tanggal_lahir,self.__jenis_kelamin,self.__nomor_telepon,self.__riwayat_medis, id)
        sql="UPDATE data_pasien SET nama_pasien = %s,alamat = %s,tanggal_lahir = %s,jenis_kelamin = %s,nomor_telepon = %s,riwayat_medis = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMA_PASIEN(self, nama_pasien):
        self.conn = mydb()
        val = (self.__alamat,self.__tanggal_lahir,self.__jenis_kelamin,self.__nomor_telepon,self.__riwayat_medis, nama_pasien)
        sql="UPDATE data_pasien SET alamat = %s,tanggal_lahir = %s,jenis_kelamin = %s,nomor_telepon = %s,riwayat_medis = %s WHERE nama_pasien=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM data_pasien WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMA_PASIEN(self, nama_pasien):
        self.conn = mydb()
        sql="DELETE FROM data_pasien WHERE nama_pasien='" + str(nama_pasien) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM data_pasien WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nama_pasien = self.result[1]
        self.__alamat = self.result[2]
        self.__tanggal_lahir = self.result[3]
        self.__jenis_kelamin = self.result[4]
        self.__nomor_telepon = self.result[5]
        self.__riwayat_medis = self.result[6]
        self.conn.disconnect
        return self.result
    def getByNAMA_PASIEN(self, nama_pasien):
        a=str(nama_pasien)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM data_pasien WHERE nama_pasien='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nama_pasien = self.result[1]
           self.__alamat = self.result[2]
           self.__tanggal_lahir = self.result[3]
           self.__jenis_kelamin = self.result[4]
           self.__nomor_telepon = self.result[5]
           self.__riwayat_medis = self.result[6]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nama_pasien = ''
           self.__alamat = ''
           self.__tanggal_lahir = ''
           self.__jenis_kelamin = ''
           self.__nomor_telepon = ''
           self.__riwayat_medis = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM data_pasien"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,alamat FROM data_pasien"
        self.result = self.conn.findAll(sql)
        return self.result