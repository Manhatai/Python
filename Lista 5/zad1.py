import numpy as np
lista = []

while True:
    x = float(input("Podaj liczbę: "))
    if x < 0:
        print("Podawaj tylko liczby nieujemne")
        continue
    lista.append(x)
    print("Lista podanych liczb:")
    print(lista)
    print("Średnia podanych liczb:")
    print(np.mean(lista))

#mój pomysł na użycie funkcji random:

# import random
# import numpy as np
# lista = []
# licznik = 0
# while True:
#    x = random.random()
#    lista.append(x)
#    print("Lista wygenerowanych liczb:")
#    print(lista)
#    print("Średnia liczb:")
#    print(np.mean(lista))
#    print("Ilość liczb w zbiorze:")
#    print(len(lista))
#    licznik = licznik + 1
#    if licznik >= 100:
#        quit()
