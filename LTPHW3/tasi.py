from sys import argv
from os.path import exists

kod, ilk, son = argv
gir = ">"
print(f"{ilk} dosyasının içindekiler {son} dosyasına taşınacak..")
print("Devam etmek için herhangi bir tuşa basın...")
input(gir)

dosya1 = open(ilk)
veri = dosya1.read()

print(f"Data {len(veri)} byte uzunluğunda")

print(f"Çıkış dosyası var mı? {exists(son)}")
input(gir)

sondosya = open(son, 'w')
sondosya.write(veri)
sondosya.close()

print("Okey")

sondosya = open(son, 'r')
sonveri = sondosya.read()
print(sonveri)

sondosya.close()
dosya1.close()
