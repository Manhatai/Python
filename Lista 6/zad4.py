lista = []
while True:
 n = int(input("Podaj liczbę: "))
 if n < 1:
    print("Podawaj tylko liczby naturalne")
    continue
 for i in range(1, n):
    if n % i == 0:
     lista.append(i)
 lista.append(n)
 print(lista)

