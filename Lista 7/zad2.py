import random
lista = []
lista_niep = []
lista_p = []
for i in range (0, 100):
    x = random.randint(0, 10)
    lista.append(x)
print(lista)
licznik0 = 0
licznik1 = 0
licznik2 = 0
tuple = tuple(lista)
for i in tuple:
 if i == 0:
    licznik0 = licznik0 + 1
 if i == 1:
     licznik1 = licznik1 + 1
 if i == 2:
     licznik2 = licznik2 + 1


print("Ilość 0 to:", licznik0)
print("Ilość 1 to:", licznik1)
print("Ilość 2 to:", licznik2)

for i in tuple:
    if i % 2 == 0:
        lista_p.append(i)
    if i % 2 != 0:
        lista_niep.append(i)

print("Liczby parzyste w krotce:")
print(lista_p)
print("Liczby nieparzyste w krotce:")
print(lista_niep)