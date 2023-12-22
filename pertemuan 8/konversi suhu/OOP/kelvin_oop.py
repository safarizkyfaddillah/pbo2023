class Kelvin:
    def _init_(self, suhu):
        self.suhu = suhu
        
    def get_kelvin(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = self.suhu - 273
        return val

    def get_reamur(self):
        val = 4/5 * ((self.suhu) - 273)
        return val

    def get_fahrenheit(self):
        val = 9/5 * ((self.suhu) - 273) + 32
        return val

suhu = input("Masukkan suhu dalam Fahrenheit:")
K = Kelvin (float (suhu))
val = K.get_kelvin()

C = K.get_celcius()
R = K.get_reamur ()
F = K.get_fahrenheit()

print(str(val) + " Kelvin, sama dengan:")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")