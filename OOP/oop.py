class insan():
    liste = []
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim
        self.meslek = "Boş"
        self.__class__.liste.append(isim)

class ogrenci(insan):
    def __init__(self, isim, soyisim):
        self.meslek = "Öğrenci"
        super().__init__(isim, soyisim, meslek)

melih = insan("Melih","AKAY")
almila = ogrenci("Almila","Bağcı")
for n in insan.liste:
    print(n.meslek)
