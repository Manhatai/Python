import random

print("Symulator mini lotto!")

a = random.randint(1, 42)
b = random.randint(1, 42)
if b == a:
    random.shuffle(b)
c = random.randint(1, 42)
if c == a:
    if c == b:
     random.shuffle(c)
d = random.randint(1, 42)
if d == a:
    if d == b:
        if d == c:
         random.shuffle(d)
e = random.randint(1, 42)
if e == a:
    if e == b:
        if e == c:
            if e == d:
             random.shuffle(d)
licz1 = int(input("Podaj liczbę pierwszą: "))
if licz1 > 42:
    print("Nie możesz wpisać liczby większej niż 42.")
    quit()
licz2 = int(input("Podaj liczbę drugą: "))
if licz2 > 42:
    print("Nie możesz wpisać liczby większej niż 42.")
    quit()
licz3 = int(input("Podaj liczbę trzecią: "))
if licz3 > 42:
    print("Nie możesz wpisać liczby większej niż 42.")
    quit()
licz4 = int(input("Podaj liczbę czwartą: "))
if licz4 > 42:
    print("Nie możesz wpisać liczby większej niż 42.")
    quit()
licz5 = int(input("Podaj liczbę piątą: "))
if licz5 > 42:
    print("Nie możesz wpisać liczby większej niż 42.")
    quit()
else:
 print("Dzisiejsze losowanie to:")
print(a, b, c, d, e,)
print("Twoje liczby to:")
print(licz1, licz2, licz3, licz4, licz5,)
