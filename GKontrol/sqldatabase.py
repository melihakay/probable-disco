#SQLite3 ve Hashlib kullanarak giriş kontrol mekanizması

import sqlite3 as sl
from sys import argv
import hashlib

db = sl.connect("temel.vt")
etki = db.cursor()

def girisKarar():
    while True:
        x = input("Komut: (giris, yeni)")
        if x == "yeni":
            while True:
                kullanici = input("Kullanıcı adı: ")
                durum = userKontrol(kullanici)
                if durum != "Kullanıcı mevcut":
                    break
            sifre = input("Şifre: ")
            sifre2 = input("Şifre tekrar: ")
            if sifre == sifre2:
                yeniKullanici(kullanici, sifre)
        elif x == "giris":
            while True:
                while True:
                    kullanici = input("Kullanıcı adı: ")
                    durum = userKontrol(kullanici)
                    if durum == "mevcut":
                        break
                    print("Kullanıcı mevcut değil...")
                sifre = input("Şifre: ")
                dq = giris(kullanici, sifre)
                if dq != 17:
                    break
            return dq
def vtKontrol():
    sonuc = etki.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='kullanicilar';").fetchall()
    if len(sonuc):
        return "mevcut"
    else:
        etki.execute("""
        CREATE TABLE kullanicilar (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        isim TEXT,
        sifre TEXT);
        """)
        return "oluşturuldu"
def sifrele(x):
    y = hashlib.sha256()
    y.update(x.encode("utf-8"))
    n = y.hexdigest()
    return n
def cevir(f):
    a = """('{}',)"""
    return a.format(f)
def userKontrol(ad):
    komut = """SELECT isim FROM kullanicilar;"""
    etki.execute(komut)
    userlistesi = etki.fetchall()
    kontrol = """('{}',)"""
    for a in userlistesi:
        if str(a) == str(kontrol.format(ad)):
            print("Kullanıcı mevcut")
            return "mevcut"
def yeniKullanici(ad, sifre):
    hash = sifrele(sifre)
    n = """INSERT INTO kullanicilar(isim, sifre) VALUES ("{}","{}");"""
    print(n.format(ad, hash))
    etki.execute(n.format(ad, hash))
    db.commit()
def giris(ad, sifre):
    hash = sifrele(sifre)
    komut = """SELECT sifre FROM kullanicilar WHERE isim ="{}";"""
    etki.execute(komut.format(ad))
    gsifre = cevir(hash)
    lsifre = etki.fetchall()
    hsifre = str(lsifre[0])

    if gsifre == hsifre:
        print("Giriş başarılı! Hoşgeldin {}".format(ad))
        return ad
    else:
        print("Giriş başarısız!")
        return 17

vtsonuc = vtKontrol()
mevcutKullanici = girisKarar()
