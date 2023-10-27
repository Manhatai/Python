from math import pi

def kula():
    r = int(input("Podaj 'r' kuli: "))
    V = (4/3) * pi * (r ** 3)
    Pc = 4 * pi * (r ** 2)
    print("Objętość kuli to: ", V)
    print("Pole kuli to: ", Pc)

def stozek():
    r = int(input("Podaj 'r' stożka: "))
    H = int(input("Podaj 'H' stożka: "))
    l = int(input("Podaj 'l' stożka: "))
    V = (1/3) * pi * (r**2) * H
    Pc = pi * (r**2) + pi * r * l
    print("Objętość stożka to: ", V)
    print("Pole całkowite stożka to: ", Pc)

def szescian():
    a = int(input("Podaj 'a' sześcianu: "))
    V = (a**3)
    Pc = 6 * (a**2)
    print("Objętość sześcianu to: ", V)
    print("Pole sześcianu to: ", Pc)

while True:
   x = input("Co chcesz obliczyć?: ")
   if x == "kula":
       kula()
   elif x == "stozek":
       stozek()
   elif x == "szescian":
       szescian()
   else:
       continue

