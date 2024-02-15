from db import DBConnection as mydb

class Data_obat:
    def __init__(self):
        self.__id=None
        self.__nama_obat=None
        self.__jenis_obat=None
        self.__keterangan=None
        self.__harga=None
        self.__stok=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def nama_obat(self):
        return self.__nama_obat
        
    @nama_obat.setter
    def nama_obat(self, value):
        self.__nama_obat = value
    @property
    def jenis_obat(self):
        return self.__jenis_obat
        
    @jenis_obat.setter
    def jenis_obat(self, value):
        self.__jenis_obat = value
    @property
    def keterangan(self):
        return self.__keterangan
        
    @keterangan.setter
    def keterangan(self, value):
        self.__keterangan = value
    @property
    def harga(self):
        return self.__harga
        
    @harga.setter
    def harga(self, value):
        self.__harga = value
    @property
    def stok(self):
        return self.__stok
        
    @stok.setter
    def stok(self, value):
        self.__stok = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama_obat,self.__jenis_obat,self.__keterangan,self.__harga,self.__stok)
        sql="INSERT INTO Data_obat (nama_obat,jenis_obat,keterangan,harga,stok) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nama_obat,self.__jenis_obat,self.__keterangan,self.__harga,self.__stok, id)
        sql="UPDATE data_obat SET nama_obat = %s,jenis_obat = %s,keterangan = %s,harga = %s,stok = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMA_OBAT(self, nama_obat):
        self.conn = mydb()
        val = (self.__jenis_obat,self.__keterangan,self.__harga,self.__stok, nama_obat)
        sql="UPDATE data_obat SET jenis_obat = %s,keterangan = %s,harga = %s,stok = %s WHERE nama_obat=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM data_obat WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMA_OBAT(self, nama_obat):
        self.conn = mydb()
        sql="DELETE FROM data_obat WHERE nama_obat='" + str(nama_obat) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM data_obat WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nama_obat = self.result[1]
        self.__jenis_obat = self.result[2]
        self.__keterangan = self.result[3]
        self.__harga = self.result[4]
        self.__stok = self.result[5]
        self.conn.disconnect
        return self.result
    def getByNAMA_OBAT(self, nama_obat):
        a=str(nama_obat)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM data_obat WHERE nama_obat='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nama_obat = self.result[1]
           self.__jenis_obat = self.result[2]
           self.__keterangan = self.result[3]
           self.__harga = self.result[4]
           self.__stok = self.result[5]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nama_obat = ''
           self.__jenis_obat = ''
           self.__keterangan = ''
           self.__harga = ''
           self.__stok = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM data_obat"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,jenis_obat FROM data_obat"
        self.result = self.conn.findAll(sql)
        return self.result    