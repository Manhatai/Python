import math

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

if a == 0:
    print("Wykonanie tego działania jest niemożliwe, gdyż równe jest 0.")
    exit()

delt = (b ** 2) - 4 * a * c
delta = delt

if delta < 0:
    print("Wykonanie tego dizałania jest niemożliwe, gdyż delta jest ujemna.")
    exit()

x1a = ((-b) - math.sqrt(delta))
x1b = x1a / 2 * a
x1 = x1b

x2a = ((-b) + math.sqrt(delta))
x2b = x2a / 2 * a
x2 = x2b

print(x1, x2, "to miejsca zerowe tej funkcji")

p = (-b) / 2 * a
q = (-delt) / 4 * a

print(p, q, "to wierzchołki tej funkcji")



