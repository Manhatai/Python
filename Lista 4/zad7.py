import math
import numpy as np

while True:
 x = int(input("Podaj liczbę: "))

 lista = []
 n = math.sqrt(x)
 lista.append(x)
 lista.append(n)

 print("Pierwiastek z liczby to:",n)

 for i in np.arange(1, x):
  if x % i == 0:
      lista.append(i)
 lista.sort()
 list(set(lista))

 print("Dzielniki tej liczby to:",lista)

 for y in lista:
    if y > 1:
        if y < n:
         print("Liczba nie jest pierwsza")
         break
        else:
         print("Liczba jest pierwsza")
         break