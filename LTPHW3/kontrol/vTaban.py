kullanicilar = {"alfa" : "pass", "beta" : "word", "bal" : "sut"}
def giris(kullanici):
    sifre = input("Password??\n>")
    if sifre == kullanicilar[kullanici]:
        return 100
    else:
        exit()
