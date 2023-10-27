import random

print("Symulator lotto!")

a = random.randint(1, 49)
b = random.randint(1, 49)
if b == a:
    random.shuffle(b)
c = random.randint(1, 49)
if c == a:
    if c == b:
     random.shuffle(c)
d = random.randint(1, 49)
if d == a:
    if d == b:
        if d == c:
         random.shuffle(d)
e = random.randint(1, 49)
if e == a:
    if e == b:
        if e == c:
            if e == d:
             random.shuffle(e)
f = random.randint(1, 49)
if f == b:
    if f == c:
        if f == d:
            if f == e:
                random.shuffle(f)
licz1 = int(input("Podaj liczbę pierwszą: "))
if licz1 > 49:
    print("Nie możesz wpisać liczby większej niż 49.")
    quit()
licz2 = int(input("Podaj liczbę drugą: "))
if licz2 > 49:
    print("Nie możesz wpisać liczby większej niż 49.")
    quit()
licz3 = int(input("Podaj liczbę trzecią: "))
if licz3 > 49:
    print("Nie możesz wpisać liczby większej niż 49.")
    quit()
licz4 = int(input("Podaj liczbę czwartą: "))
if licz4 > 49:
    print("Nie możesz wpisać liczby większej niż 49.")
    quit()
licz5 = int(input("Podaj liczbę piątą: "))
if licz5 > 49:
    print("Nie możesz wpisać liczby większej niż 49.")
    quit()
licz6 = int(input("Podaj liczbę szóstą: "))
if licz6 > 49:
    print("Nie możesz wpisać liczby większej niż 49.")
    quit()
else:
 print("Dzisiejsze losowanie to:")
print(a, b, c, d, e, f)
print("Twoje liczby to:")
print(licz1, licz2, licz3, licz4, licz5, licz6)
