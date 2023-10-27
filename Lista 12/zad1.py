import math

def obliczenia():
    x = int(input("Podaj liczbę pierwszą: "))
    y = int(input("Podaj liczbę drugą:"))
    dodawanie = x + y
    odejmowanie1 = x - y
    odejmowanie2 = y - x
    mnożenie = x * y
    dzielenie1 = x / y
    dzielenie2 = y / x
    pierwiastkowanie1 = math.sqrt(x)
    pierwiastkowanie2 = math.sqrt(y)
    print("Wynik dodawania to: ", dodawanie)
    print("Wynik odejmowania liczby pierwszej od drugiej to: ", odejmowanie1)
    print("Wynik odejmowania liczby drugiej od pierwszej to: ", odejmowanie2)
    print("Wynik mnożenia to: ", mnożenie)
    print("Wynik dzielenia liczby pierwszej przez drugą: ", dzielenie1)
    print("Wynik dzielenia liczby drugiej przez pierwszą: ", dzielenie2)
    print("Pierwiastkowanie liczby pierwszej: ", pierwiastkowanie1)
    print("Pierwiastkowanie liczby drugiej: ", pierwiastkowanie2)

obliczenia()