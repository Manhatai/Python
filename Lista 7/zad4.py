x = input("Wpisz zdanie:")
tuple = ("a", "b", "c", "d", "e", "f", x)

for i in tuple:
    if i == "a":
        print("Indeks 'a' to:")
        print(tuple.index("a"))
print(tuple)

print("Ilość 'a' w zdaniu to:")
print(x.count("a"))

