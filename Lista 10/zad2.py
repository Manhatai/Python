x = input("Podaj imię: ")
y = input("Podaj nazwisko: ")
a = input("Podaj numer telefonu: ")
b = input("Podaj numer buta: ")

list1 = []
if x.isalpha() == True:
    print("Twoje imię składa się tylko z liter.")
else:
    print("W twoim imieniu znajdują się liczby.")

if x.isalpha() == True:
    print("W twoim nazwisku znajdują się tylko litery.")
else:
    print("W twoim nazwisku znajdują się liczby.")

if x.isdigit() == True:
    print("W twoim numerze telefonu znajdują się tylko cyfry.")
else:
    print("W twoim numerze telefonu znajdują się litery.")

if x.isdigit() == True:
    print("W twoim numerze buta znajdują się tylko cyfry.")
else:
    print("W twoim numerze buta znajdują się litery.")

print(x.title())
print(y.title())

print(''.join(x for x in a if x.isdigit()))
print(''.join(x for x in b if x.isdigit()))

list1.append(x)
for i in list1:
    if i[-1] == "a":
        print("Jesteś kobietą XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD (imagine being w0man XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD)")
    elif i == "Miriam" or "Beatrycze" or "Nel" or "Abigail" or "Karmen" or "Nel" or "Noemi" or "Nicol" or "Nicole" or "Nikol":
        print("Jesteś kobietą XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD (imagine being w0man XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD)")



