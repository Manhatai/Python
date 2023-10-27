# Napisz program przy użyciu pętli while , który skończy wczytywania liczb podawanych przez użytkownika, gdy ich suma przekroczy 100 albo średnia wyniesie 66.
from statistics import mean

lista = []

while True:
 x = int(input("Podaj liczbę: "))
 lista.append(x)
 print(lista)
 print(sum(lista))
 if sum(lista) >= 100:
  print("Suma jest większa niż 100")
  quit()
 if mean(lista) == 66:
  print("Średnia równa jest 66")
  quit()


