from random import randrange
print("Witaj w grze Za dużo, za mało!")
wygrana = randrange(1000,100000)
print("Dzisiejsza pula to:",wygrana,"zł")
x = randrange(1,101)
licznik = 0

while True:
    y = int(input("Podaj liczbę: "))
    if y > 100:
        print("Nie możesz podać większej liczby niż 100")
        continue
    if y > x:
        print("Podałeś za dużą wartość")
        licznik += 1
    if y < x:
        print("Podałeś za małą wartość:")
        licznik += 1
    if y == x:
        print("Hurra! Wygrałeś",wygrana,"zł!")
        break
    if licznik >= 3:
        print("Haha przegrałeś lmao")
        break