import math
def luas_balok (panjang,lebar,tinggi):
    luas_balok = (2 * (panjang * lebar + panjang * tinggi + lebar * tinggi))
    return luas_balok
def volume_balok (panjang,lebar,tinggi):
    volume_balok = (panjang * lebar * tinggi)
    return volume_balok
def luas_bola (jari_jari):
    luas_bola = (4 * math.pi * jari_jari ** 2)
    return luas_bola
def volume_bola (jari_jari):
    volume_bola = ((4/3) * math.pi * jari_jari ** 3)
    return volume_bola
def luas_kerucut (jari_jari, tinggi):
    luas_kerucut = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari**2 + tinggi**2))
    return luas_kerucut
def volume_kerucut (jari_jari, tinggi):
    volume_kerucut = (1/3) * math.pi * jari_jari**2 * tinggi
    return volume_kerucut
def luas_kubus (sisi):
    luas_kubus = 6 * sisi**2
    return luas_kubus
def volume_kubus (sisi):
    volume_kubus = sisi**3
    return volume_kubus
def luas_limas_segiempat (panjang, lebar, tinggi_limas):
    luas_limas_segiempat = panjang * lebar + 2 * (panjang * tinggi_limas / 2) + 2 * (lebar * tinggi_limas / 2)
    return luas_limas_segiempat
def volume_limas_segiempat (panjang, lebar, tinggi):
    volume_limas_segiempat = (1/3) * panjang * lebar * tinggi
    return volume_limas_segiempat
def luas_limas_segitiga (panjang_alas, tinggi_segitiga, tinggi_limas):
    luas_limas_segitiga = (panjang_alas * tinggi_segitiga) + (3 * (1 / 2) * panjang_alas * tinggi_limas)
    return luas_limas_segitiga
def volume_limas_segitiga (panjang_alas, tinggi_segitiga, tinggi_limas):
    volume_limas_segitiga = (1 / 3) * (1 / 2) * panjang_alas * tinggi_segitiga * tinggi_limas
    return volume_limas_segitiga
def luas_segitiga (alas_segitiga, tinggi_segitiga):
    luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
    return luas_segitiga
def luas_permukaan_prisma(alas_segitiga, tinggi_segitiga, tinggi_permukaan_prisma):
    luas_permukaan_prisma = 2 * alas_segitiga * tinggi_segitiga + 3 * alas_segitiga * tinggi_permukaan_prisma
    return luas_permukaan_prisma
def volume_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_permukaan_prisma):
    volume_prisma_segitiga = 0.5 * alas_segitiga * tinggi_segitiga * tinggi_permukaan_prisma
    return volume_prisma_segitiga
def luas_tabung(jari_jari, tinggi):
    luas_tabung = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return luas_tabung
def volume_tabung(jari_jari, tinggi):
    volume_tabung = math.pi * jari_jari**2 * tinggi
    return volume_tabung
