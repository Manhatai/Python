# Napisz program przy użyciu pętli while, w którym podajemy liczbę naturalną do momentu podania liczby podzielnej przez 12. Algorytm kończy działanie napisem: „Podałeś liczbę podzielną przez 12, wiec kończę działanie pętli".
x = int(input("Podaj liczbę: "))

while x % 12 != 0:
    x = int(input("Podaj kolejną liczbę: "))

if x%12 == 0:
    print("Podałeś liczbę podzielną przez 12, wiec kończę działanie pętli")

