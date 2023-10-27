import random
lista = []
for i in range(0,50):
    x = random.randint(0,1)
    if x == 0:
        x = 'reszka'
    if x == 1:
        x = 'orzel'
    lista.append(x)
print(lista)
ilosc0 = lista.count('reszka')
ilosc1 = lista.count('orzel')
print('Ilosc orłów:' ,ilosc1,)
print('Ilosc reszek:' ,ilosc0,)


