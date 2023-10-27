x = int(input("Podaj wartość :"))
print("Liczby od podanej wartości do 0:")

for i in range(x, 0, -1):
    print(i)

print("Liczby do podanej wartości podzielne przez 6:")
for y in range(0, x):
    if y % 6 == 0:
        print(y)

print("Liczby do podanej wartości podzielne przez 9:")
for z in range(0, x):
    if z % 9 == 0:
        print(z)
