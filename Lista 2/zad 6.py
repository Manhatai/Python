a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))
d = int(input("Podaj liczbę d: "))

if a > b:
    if a > c:
        if a > d:
         print(a, "jest najwieksze")


elif b > a:
    if b > c:
        if b > d:
         print(b, "jest najwieksze")

elif c > b:
    if c > a:
        if c > d:
         print(c, "jest najwieksze")

elif d > b:
    if d > c:
        if d > a:
         print(d, "jest najwieksze")

