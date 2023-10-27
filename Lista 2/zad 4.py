## Napisz program, który wypisze czy podana liczba jest ujemna czy dodatnia oraz czy jest podzielna przez 2 z resztą. Zaproponuj odpowiednie warunki.

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

if a > 0:
    print("a jest liczba dodatnia")
    if b > 0:
        print("b jest liczba dodatnia")
        if c > 0:
            print("c jest liczba dodatnia")

if a % 2 == 0:
    print("Liczba a jest podzielna przez 2")

if a % 2 > 0:
        print("Liczba a jest niepodzielna przez 2")


if b % 2 == 0:
    print("Liczba b jest podzielna przez 2")

if b % 2 > 0:
        print("Liczba b jest niepodzielna przez 2")


if c % 2 == 0:
    print("Liczba c jest podzielna przez 2")

if c % 2 > 0:
        print("Liczba c jest niepodzielna przez 2")
