import random

print("Symulator multi multi!")

a = random.randint(1, 80)
b = random.randint(1, 80)
if b == a:
    random.shuffle(b)
c = random.randint(1, 80)
if c == a:
    if c == b:
     random.shuffle(c)
d = random.randint(1, 80)
if d == a:
    if d == b:
        if d == c:
          random.shuffle(d)
e = random.randint(1, 80)
if e == a:
    if e == b:
        if e == c:
            if e == d:
             random.shuffle(d)
f = random.randint(1, 80)
if f == b:
    if f == c:
        if f == d:
            if f == e:
                random.shuffle(d)
g = random.randint(1, 80)
if g == b:
    if g == c:
        if g == d:
            if g == e:
                if g == f:
                 random.shuffle(g)
h = random.randint(1, 80)
if h == b:
    if h == c:
        if h == d:
            if h == e:
                if h == f:
                  if h == g:
                   random.shuffle(h)
i = random.randint(1, 80)
if i == b:
    if i == c:
        if i == d:
            if i == e:
                if i == f:
                   if i == g:
                       if i == h:
                        random.shuffle(i)
j = random.randint(1, 80)
if j == b:
    if j == c:
        if j == d:
            if j == e:
                if j == f:
                   if j == g:
                       if j == h:
                           if j == i:
                            random.shuffle(j)
licz1 = int(input("Podaj liczbę pierwszą: "))
if licz1 > 80:
    print("Nie możesz wpisać liczby większej niż 80.")
    quit()
licz2 = int(input("Podaj liczbę drugą: "))
if licz2 > 80:
    print("Nie możesz wpisać liczby większej niż 80.")
    quit()
licz3 = int(input("Podaj liczbę trzecią: "))
if licz3 > 80:
    print("Nie możesz wpisać liczby większej niż 80.")
    quit()
licz4 = int(input("Podaj liczbę czwartą: "))
if licz4 > 80:
    print("Nie możesz wpisać liczby większej niż 80.")
    quit()
licz5 = int(input("Podaj liczbę piątą: "))
if licz5 > 80:
    print("Nie możesz wpisać liczby większej niż 80.")
    quit()
licz6 = int(input("Podaj liczbę szóstą: "))
if licz6 > 80:
    print("Nie możesz wpisać liczby większej niż 80.")
    quit()
licz7 = int(input("Podaj liczbę siódmą: "))
if licz7 > 80:
    print("Nie możesz wpisać liczby większej niż 80.")
    quit()
licz8 = int(input("Podaj liczbę ósmą: "))
if licz8 > 80:
    print("Nie możesz wpisać liczby większej niż 80.")
    quit()
licz9 = int(input("Podaj liczbę dziewiątą: "))
if licz9 > 80:
    print("Nie możesz wpisać liczby większej niż 80.")
    quit()
licz10 = int(input("Podaj liczbę dziesiątą: "))
if licz10 > 80:
    print("Nie możesz wpisać liczby większej niż 80.")
    quit()
else:
 print("Dzisiejsze losowanie to:")
print(a, b, c, d, e, f, g, h, i, j)
print("Twoje liczby to:")
print(licz1, licz2, licz3, licz4, licz5, licz6, licz7, licz8, licz9, licz10)
