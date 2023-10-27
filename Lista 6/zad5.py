import random      #Przepraszam za nieuporządkowanie kodu, długo zajęło mi to zadanie

lista = []
lista2 = []
x = int(input("Podaj początek ciągu: "))
z = int(input("Podaj koniec ciągu: "))

for i in range(x, z + 1):
    lista.append(i)
print(lista[-3])
k = int(input("Podaj który element od końca chcesz usunąć: "))
lista.pop(-k - 1)

for i in range(x, z + 1):
    q = random.randint(x, z + 1)
    lista2.append(q)

lista.extend(lista2)
lista.sort()
print(lista)
licznik = 0

for i in lista:
    if lista[i] == lista[i+1]:
        licznik = licznik + 1
print("Długośc listy to:")
print(len(lista))
print("Ilość powtórzeń w liście to:")
print(licznik)

