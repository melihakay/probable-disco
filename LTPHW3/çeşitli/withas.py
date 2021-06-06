#Aşağıdaki iki fonksiyon da aynı görevi görmekte

with open("kaynak.mlh", "w") as f:
    f.write("Deneme deneme")

f = open("kaynak.mlh", "w")
try:
    f.write("Denemelik!\n")
finally:
    f.close()
