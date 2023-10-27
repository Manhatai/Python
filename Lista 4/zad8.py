#zadanie 8 bez uzycia "while"

print('Witaj w kalkulatorze oszczędności!')
print('Przykład działania:')
print('Kwota wypłaty brutto: 3891')
print('Kwota którą chcemy odłożyć miesięcznie: 333')
print('Procent odsetek: 8')

x = 3891
y = 333

lista_msc = []
lista_kaski = []
lista_kaski_plus_odsetki = []
a = 0

for i in range(1, 13):
 lista_msc.append(i)


for i in lista_msc:
    a = a + 333
    lista_kaski.append(a)

print('Ilość odłożonych pieniędzy brutto w respektywnych miesiącach:')
print(lista_kaski)

for a in lista_kaski:
    z = 8/100 * a
    a = a + z
    lista_kaski_plus_odsetki.append(a)

print('Ilość odłożonych pieniędzy brutto wraz z odsetkami:')
print(lista_kaski_plus_odsetki)

print('Finalna ilość odłożonych pieniędzy + odsetki, brutto: ')
print(lista_kaski_plus_odsetki[-1])

#zadanie 8 z użyciem "while"



while True:

 x = int(input("Podaj wypłatę brutto: "))
 y = int(input("Podaj kwotę którą chcesz odłożyć miesięczie: "))
 q = int(input("Podaj procent odsetek od odłożonej kwoty: "))

 lista_msc = []
 lista_kaski = []
 lista_kaski_plus_odsetki = []
 a = 0

 for i in range(1, 13):
     lista_msc.append(i)

 for i in lista_msc:
     a = a + y
     lista_kaski.append(a)

 print('Ilość odłożonych pieniędzy brutto w respektywnych miesiącach:')
 print(lista_kaski)

 for a in lista_kaski:
     z = q / 100 * a
     a = a + z
     lista_kaski_plus_odsetki.append(a)

 print('Ilość odłożonych pieniędzy brutto wraz z odsetkami:')
 print(lista_kaski_plus_odsetki)

 print('Finalna ilość odłożonych pieniędzy + odsetki, brutto: ')
 print(lista_kaski_plus_odsetki[-1])