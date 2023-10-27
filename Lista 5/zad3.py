x = input("Podaj liczbę: ")
z = reversed(x)
a = "".join(z)

if a == x:
    print("Liczba jest palindromem")
    quit()
else:
    print("Podana liczba odwrócona to:")
    print(a)