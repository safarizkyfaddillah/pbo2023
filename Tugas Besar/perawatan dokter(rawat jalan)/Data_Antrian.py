from db import DBConnection as mydb

class Data_antrian:
    def __init__(self):
        self.__id=None
        self.__nama_pasien=None
        self.__nomor_antrian_pasien=None
        self.__tanggal_antri=None
        self.__jam_antri=None
        self.__status=None
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
    def nomor_antrian_pasien(self):
        return self.__nomor_antrian_pasien
        
    @nomor_antrian_pasien.setter
    def nomor_antrian_pasien(self, value):
        self.__nomor_antrian_pasien = value
    @property
    def tanggal_antri(self):
        return self.__tanggal_antri
        
    @tanggal_antri.setter
    def tanggal_antri(self, value):
        self.__tanggal_antri = value
    @property
    def jam_antri(self):
        return self.__jam_antri
        
    @jam_antri.setter
    def jam_antri(self, value):
        self.__jam_antri = value
    @property
    def status(self):
        return self.__status
        
    @status.setter
    def status(self, value):
        self.__status = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama_pasien,self.__nomor_antrian_pasien,self.__tanggal_antri,self.__jam_antri,self.__status)
        sql="INSERT INTO Data_antrian (nama_pasien,nomor_antrian_pasien,tanggal_antri,jam_antri,status) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nama_pasien,self.__nomor_antrian_pasien,self.__tanggal_antri,self.__jam_antri,self.__status, id)
        sql="UPDATE data_antrian SET nama_pasien = %s,nomor_antrian_pasien = %s,tanggal_antri = %s,jam_antri = %s,status = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMA_PASIEN(self, nama_pasien):
        self.conn = mydb()
        val = (self.__nomor_antrian_pasien,self.__tanggal_antri,self.__jam_antri,self.__status, nama_pasien)
        sql="UPDATE data_antrian SET nomor_antrian_pasien = %s,tanggal_antri = %s,jam_antri = %s,status = %s WHERE nama_pasien=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM data_antrian WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMA_PASIEN(self, nama_pasien):
        self.conn = mydb()
        sql="DELETE FROM data_antrian WHERE nama_pasien='" + str(nama_pasien) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM data_antrian WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nama_pasien = self.result[1]
        self.__nomor_antrian_pasien = self.result[2]
        self.__tanggal_antri = self.result[3]
        self.__jam_antri = self.result[4]
        self.__status = self.result[5]
        self.conn.disconnect
        return self.result
    def getByNAMA_PASIEN(self, nama_pasien):
        a=str(nama_pasien)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM data_antrian WHERE nama_pasien='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nama_pasien = self.result[1]
           self.__nomor_antrian_pasien = self.result[2]
           self.__tanggal_antri = self.result[3]
           self.__jam_antri = self.result[4]
           self.__status = self.result[5]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nama_pasien = ''
           self.__nomor_antrian_pasien = ''
           self.__tanggal_antri = ''
           self.__jam_antri = ''
           self.__status = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM data_antrian"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nomor_antrian_pasien FROM data_antrian"
        self.result = self.conn.findAll(sql)
        return self.result  