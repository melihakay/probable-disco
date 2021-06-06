from sys import argv
kod, sayi = argv
sayi = int(sayi)

def main(sayi):
    carp = sayi * 2
    bol = sayi / 7
    kare = sayi * sayi
    return carp, bol, kare

liste = main(sayi)

print(type(liste))

a= 0
for n in liste:
    a += 1
    print(a, n)

# liste.append(n) ile listeye elemean eklenir
