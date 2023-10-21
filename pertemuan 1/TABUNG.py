# Menghitung luas permukaan dan volume tabung

# Jari-jari tabung dan tinggi tabung
jari_jari = 5
tinggi = 10

# Mengimport nilai pi
from math import pi

# Menghitung luas permukaan tabung
luas_permukaan = 2 * pi * jari_jari * (jari_jari + tinggi)

# Menghitung volume tabung
volume = pi * (jari_jari ** 2) * tinggi

# Menampilkan hasil
print("Luas Permukaan Tabung: ", luas_permukaan)
print("Volume Tabung: ", volume)
