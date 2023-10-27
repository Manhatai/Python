##3. Napisz program, który porówna ze sobą 3 liczby i wskaże, która jest większa i czy liczby są identyczne. Zastanów się nad opcją zagnieżdżania ifów.

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

if a > b:
    if a > c:
        print("a jest najwieksze")

elif b > a:
    if b > c:
        print("b jest najwieksze")

elif c > a:
    if c > b:
        print("c jest najwieksze")

if a == b:
    print("a jest rowne b")

if b == c:
    print("b jest rowne c")

if a == c:
    print("a jest rowne c")
