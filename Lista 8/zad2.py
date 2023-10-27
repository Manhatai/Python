kontakty = {"maciek": 999999999, "marek": 123456789, "mariusz": 321123321, "mateusz": 998889998, "mieczysław": 778887778, "miras": 455445554, "maks": 699696996, "małgorzata": 987654321, "maurycy": 777888999, "marcel": 555666777}
print("Wszystkie kontakty:")
for wartosc, klucz in kontakty.items():
    print(wartosc, klucz)
print("..................................")
print("Kontakty poprawione:")
kontakty["maciek"] = 198123567
kontakty["marcel"] = 217339345
del kontakty["mieczysław"]
for wartosc, klucz in kontakty.items():
    print(wartosc, klucz)
print("..................................")
print("Wyczyszczona lista:")
kontakty.clear()
kontakty["Frajer"] = 891234122
kontakty["Pompka"] = 567321123
for wartosc, klucz in kontakty.items():
    print(wartosc, klucz)


print("..................................")
print("Posortowana lista:")
dict(sorted(kontakty.items()))
for wartosc, klucz in kontakty.items():
    print(wartosc, klucz)

kontakty = list(kontakty)
print("..................................")
print("Kontakty zmienione na listę:")
print(kontakty)

print("..................................")
print("Kontakty posortowane:")
kontakty.sort()
print(kontakty)