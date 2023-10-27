import math
import numpy as np
x = int(input("Podaj liczbę: "))

lista = []
n = math.sqrt(x)

for y in np.arange(1, n):
    lista.append(y)

for i in lista:
 if i > 1:
    if i < n:
        print("liczba nie jest pierwsza")
    else:
        print("liczba jest pierwsza")