from db import DBConnection as mydb

class data_pemeriksaan_pasien:
    def __init__(self):
        self.__id=None
        self.__nama_pasien=None
        self.__tanggal_pemeriksaan=None
        self.__keluhan=None
        self.__diagnosis=None
        self.__resep_obat=None
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
    def tanggal_pemeriksaan(self):
        return self.__tanggal_pemeriksaan
        
    @tanggal_pemeriksaan.setter
    def tanggal_pemeriksaan(self, value):
        self.__tanggal_pemeriksaan = value
    @property
    def keluhan(self):
        return self.__keluhan
        
    @keluhan.setter
    def keluhan(self, value):
        self.__keluhan = value
    @property
    def diagnosis(self):
        return self.__diagnosis
        
    @diagnosis.setter
    def diagnosis(self, value):
        self.__diagnosis = value
    @property
    def resep_obat(self):
        return self.__resep_obat
        
    @resep_obat.setter
    def resep_obat(self, value):
        self.__resep_obat = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama_pasien,self.__tanggal_pemeriksaan,self.__keluhan,self.__diagnosis,self.__resep_obat)
        sql="INSERT INTO data_pemeriksaan_pasien (nama_pasien,tanggal_pemeriksaan,keluhan,diagnosis,resep_obat) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nama_pasien,self.__tanggal_pemeriksaan,self.__keluhan,self.__diagnosis,self.__resep_obat, id)
        sql="UPDATE data_pemeriksaan_pasien SET nama_pasien = %s,tanggal_pemeriksaan = %s,keluhan = %s,diagnosis = %s,resep_obat = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMA_PASIEN(self, nama_pasien):
        self.conn = mydb()
        val = (self.__tanggal_pemeriksaan,self.__keluhan,self.__diagnosis,self.__resep_obat, nama_pasien)
        sql="UPDATE data_pemeriksaan_pasien SET tanggal_pemeriksaan = %s,keluhan = %s,diagnosis = %s,resep_obat = %s WHERE nama_pasien=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM data_pemeriksaan_pasien WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMA_PASIEN(self, nama_pasien):
        self.conn = mydb()
        sql="DELETE FROM data_pemeriksaan_pasien WHERE nama_pasien='" + str(nama_pasien) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM data_pemeriksaan_pasien WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nama_pasien = self.result[1]
        self.__tanggal_pemeriksaan = self.result[2]
        self.__keluhan = self.result[3]
        self.__diagnosis = self.result[4]
        self.__resep_obat = self.result[5]
        self.conn.disconnect
        return self.result
    def getByNAMA_PASIEN(self, nama_pasien):
        a=str(nama_pasien)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM data_pemeriksaan_pasien WHERE nama_pasien='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nama_pasien = self.result[1]
           self.__tanggal_pemeriksaan = self.result[2]
           self.__keluhan = self.result[3]
           self.__diagnosis = self.result[4]
           self.__resep_obat = self.result[5]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nama_pasien = ''
           self.__tanggal_pemeriksaan = ''
           self.__keluhan = ''
           self.__diagnosis = ''
           self.__resep_obat = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAlldata(self):
        self.conn = mydb()
        sql="SELECT * FROM data_pemeriksaan_pasien"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getCombodata(self):
        self.conn = mydb()
        sql="SELECT id,tanggal_pemeriksaan FROM data_pemeriksaan_pasien"
        self.result = self.conn.findAll(sql)
        return self.result