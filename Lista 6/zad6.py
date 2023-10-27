import random
lista = []
for i in range(1, 31):
    lista.append(i)
print("Lista wygląda w następujący sposób:")
print(lista)


for i in range(1, 21):
    x = random.randint(1, 51)
    lista.append(x)
lista.sort()
print("Lista po dodaniu wygenerowanych liczb wygląda w ten sposób:")
print(lista)

print("Lista po usunięciu duplikatów: ")
usun = (set(lista))
print(usun)

print("Długość listy to:")
print(len(usun))