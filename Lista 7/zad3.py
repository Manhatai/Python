lista1 = []
lista2 = []

for i in range(0,101):
    if i % 2 == 0:
        lista1.append(i)
    if i % 2 != 0:
        lista2.append(i)

tuple1 = tuple(lista1)
tuple2 = tuple(lista2)
tuple1 = tuple1 + tuple2

print("Długośc krotki po dodaniu to:", len(tuple1))
for i in tuple1:
    if i == 0:
        print("W krotce jest 0")
    if i == 100:
        print("W krotce jest 100")
