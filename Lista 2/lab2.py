x = int(input("Podaj liczbę: "))
if x > 0:
    print("x jest liczbą dodatnią")
else:
    print("x jest liczbą ujemną")


if x % 2 == 0:
    print("x jest parzysty")
else:
    print("x jest nieparzysty")


a = 33
b = 33
if b > a:
    print("b jest wieksze od a")

elif a == b:
    print("a i b sa rowne")

a = 200
b = 33
if b > a:
    print("b jest wieksze niż a")
elif a == b:
    print("a i b są równe")
else:
    print("a jest większe od b")

x = int(input("Podaj liczbę: "))
if x > 10:
    print("Liczba jest większa od 10")
if x > 20:
    print("Liczba jest wieksza od 20")
else:
    print("gowno")
