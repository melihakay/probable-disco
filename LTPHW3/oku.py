from sys import argv

kod, dosya = argv

def oku(dsy):
    #dosya okuma fonksiyonu
    metin = open(dsy)
    print(f"Dosyan ({dsy}):")
    print(metin.read())
    metin.close()

if dosya == "yardim":
    #yardim metni yazıp çıkış
    input("""
Kullanım:
    py3 dosya.py dosya_adi
""")
    exit()
#elif dosya == "":
#    dosya = input("Okunacak dosya: ")

oku(dosya)
while True:
    dosya = input("Sıradaki dosya: ")
    if dosya == "bitti":
        break
    oku(dosya)
print("Çıkış 1sn..")
exit()
