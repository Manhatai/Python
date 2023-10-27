x = int(input("Podaj liczbę z której chcesz otrzymać silnię: "))
a = 1
b = 1
for i in range(1, x + 1):
 a = i
 b = a * b
print("Silnia tej liczby wynosi:")
print(b)


