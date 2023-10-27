x = int(input("Podaj liczbę: "))

while True:
    suma = 0
    for i in range(1, x):
        if x % i == 0:
            suma = suma + i
    if suma == x:
        print("Liczba jest liczbą doskonałą.")
    else:
        print("Liczba nie jest liczbą doskonałą.")
    x = int(input("Podaj liczbę: "))
