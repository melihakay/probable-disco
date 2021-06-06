import sys
kod, gKodlama, hata = sys.argv

def main(dosya, kodlama, hatalar):
    satir = dosya.readline()
    if satir:
        yazdir(satir, kodlama, hatalar)
        return main(dosya, kodlama, hatalar)

def yazdir(satir, kodlama, hatalar):
    sonrakidil = satir.strip()
    rawbit = sonrakidil.encode(kodlama, errors=hatalar)
    dolubit = rawbit.decode(kodlama, errors = hatalar)

    print(rawbit, "<==>", dolubit)

diller = open("languages.txt", encoding="utf-8")

main(diller, gKodlama, hata)
