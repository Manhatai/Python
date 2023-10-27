import math

x = input(
    "Podaj nazwę figury jakiej chcesz obliczyć pole i obwód (do wyboru: kwadrat,prostokąt,trójkąt[rownoramienny],koło,romb,trapez [bez polskich znaków]): ")

if x == "kwadrat":
    y = int(input("Podaj długość boku: "))

if x == "prostokat":
    a = int(input("Podaj długość boku 1: "))
    b = int(input("Podaj długość boku 2: "))

if x == "trojkat":
    a = int(input("Podaj długość ramion: "))
    b = int(input("Podaj długość podstawy: "))
    h = int(input("Podaj wysokość: "))

if x == "kolo":
    r = int(input("Podaj długość promienia: "))

if x == "romb":
    a = int(input("Podaj długość boku: "))
    h = int(input("Podaj wysokość: "))

if x == "trapez":
    a = int(input("Podaj długość boku 1: "))
    b = int(input("Podaj długość boku 2: "))
    c = int(input("Podaj długość boku 3: "))
    h = int(input("Podaj wysokość: "))


class figura:
    def __init__(self, rodzaj, pole, obwod):
        self.rodzaj = rodzaj
        self.pole = pole
        self.obwod = obwod

    def pobw(self):
        print("Pole", self.rodzaj, "to:", self.pole, ", a obwód to:", self.obwod, ".")


class square(figura):
    def __init__(self):
        P = y * y
        Obw = 4 * y
        super().__init__("kwadrat", P, Obw)


class rectangle(figura):
    def __init__(self):
        P = a * b
        Obw = (2 * a) + (2 * b)
        super().__init__("prostokąt", P, Obw)


class triangle(figura):
    def __init__(self):
        P = (a * h) / 2
        Obw = a + (2 * b)
        super().__init__("trójkąt", P, Obw)


class circle(figura):
    def __init__(self):
        P = 3.14 * math.sqrt(r)
        Obw = 2 * 3.14 * r
        super().__init__("koło", P, Obw)


class rhombus(figura):
    def __init__(self):
        P = a * h
        Obw = 4 * a
        super().__init__("romb", P, Obw)


class trapezoid(figura):
    def __init__(self):
        P = (a + b * h) / 2
        Obw = a + b + (2 * c)
        super().__init__("trapez", P, Obw)


if x == "kwadrat":
    kwadrat = square()
    kwadrat.pobw()

if x == "prostokat":
    prostokat = rectangle()
    prostokat.pobw()

if x == "trojkat":
    trojkat = triangle()
    trojkat.pobw()

if x == "kolo":
    kolo = circle()
    kolo.pobw()

if x == "romb":
    romb = rhombus()
    romb.pobw()

if x == "trapez":
    trapez = trapezoid()
    trapez.pobw()
