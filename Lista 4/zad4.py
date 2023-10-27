# Napisz program przy użyciu pętli while wczytujący z klawiatury wartości, a następnie wyświetlający średnią tych wartości, niech program kończy wprowadzanie, kiedy natrafi na cyfrę 0. Czy możliwe by było przerwanie jeśli ktoś wpisze wybrany znak albo string o treści NULL?
from statistics import mean
print("Witaj w programie liczącym średnią z podanych liczb.")
x = int(input("Podaj liczbę: "))
lista = []

while True:
 lista.append(x)
 print(lista)
 print("Średnia z podanych liczb to:",mean(lista))
 x = int(input("Podaj liczbę: "))
 if mean(lista) < 1:
  print("Średnia liczb jest mniejsza niż 0")
  break
