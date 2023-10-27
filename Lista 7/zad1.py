tuple = (1, "a", 2, "b", 3, "c", 4)
tuple2 = (2, 1)
lista = []
print('Długość krotki to:')
print(len(tuple))
print('Miejsce w pamieci tej krotki to:')
print(id(tuple))
tuple = tuple + tuple2
tuple = list(tuple)
print(tuple)