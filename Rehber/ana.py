import mysql.connector
from os import system, name
from getpass import getpass
from time import sleep

def ekle():
    print("İsim: ",end="")
    isim = input()
    print("Soyisim: ",end="")
    soyisim = input()
    print("Yaş: ",end="")
    yas = input()
    print("Meslek: ",end="")
    meslek = input()

    #en uzun stringi alan fonksiyon
    liste = [isim , soyisim, yas, meslek]
    max_len = -1
    for n in liste:
        if len(n) > max_len:
            max_len = len(n)
            en_uzun = n

    #Tablo oluşturan fonksiyon
    temizle()
    print("  ","-"*(16 + len(en_uzun)))
    print("  ","|","İsim:   ","|",isim," "*(len(en_uzun)-len(isim)),"|")
    print("  ","-"*(16 + len(en_uzun)))
    print("  ","|","Soyisim:","|",soyisim," "*(len(en_uzun)-len(soyisim)),"|")
    print("  ","-"*(16 + len(en_uzun)))
    print("  ","|","Yaş:    ","|",yas," "*(len(en_uzun)-len(yas)),"|")
    print("  ","-"*(16 + len(en_uzun)))
    print("  ","|","Meslek: ","|",meslek," "*(len(en_uzun)-len(meslek)),"|")
    print("  ","-"*(16 + len(en_uzun)))

    kesinlik = input("\nBelirtilen bilgileri rehbere ekle? (E/h)")
    if kesinlik == "E":
        print("Ekleniyor")
        komut = "INSERT INTO genel (isim, soyisim, yas, meslek) VALUES ( %s, %s, %s, %s )"
        kayit = (isim, soyisim, yas, meslek)
        etki.execute(komut, kayit)
        vt.commit()
        print(etki.rowcount, "Eklendi!")
        sleep(2)
        temizle()

def temizle():
    #windows
    if name == 'nt':
        _ = system('cls')

    #linux
    else:
        _ = system('clear')
    print("")
def cikis():
    temizle()
    print("2sn içinde çıkış")
    sleep(2)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    quit(0)



#Giriş
temizle()
print("Rehber (version 0.2.1)")
vt = mysql.connector.connect(
        host="melihakay.com",
        user="py3",
        password=getpass("Şifre: "),
        database=("rehber"),
        )
print("Başarılı Giriş! Lütfen Bekleyin...")
etki = vt.cursor()
sleep(2)
temizle()

while True:
    temizle()
    isaret = input("Rehbere verilecek komut? (Yardım için \'yardim\', çıkış için \'bitti\')\n>>")
    if isaret == "bitti":
        cikis()
    elif isaret == "yardim":
        print("""
Çıkış için bitti,
Eklemek için ekle,
        """)
    elif isaret == "ekle":
        temizle()
        ekle()
