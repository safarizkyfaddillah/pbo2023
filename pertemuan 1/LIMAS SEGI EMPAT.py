# Menghitung luas permukaan dan volume limas segi empat

# Panjang sisi alas, tinggi limas, dan tinggi segitiga sisi
sisi_alas = 5
tinggi_limas = 10
tinggi_segitiga = 8

# Menghitung luas permukaan limas segi empat
luas_permukaan = (sisi_alas ** 2) + 2 * sisi_alas * (tinggi_limas + tinggi_segitiga)

# Menghitung volume limas segi empat
volume = (sisi_alas ** 2 * tinggi_limas) / 3

# Menampilkan hasil
print("Luas Permukaan Limas Segi Empat: ", luas_permukaan)
print("Volume Limas Segi Empat: ", volume)
