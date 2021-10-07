import csv
with open("D:\Google Drive\Kişisel\Plants of melihhakay@gmail.com (Melih Akay) (1).csv", encoding="utf-8") as liste:
    oku = csv.reader(liste)
    oku = list(oku)
    oku[0][0] = 'Start Time'
    sutunlar = oku[0]
    print(oku)
    print(sutunlar)