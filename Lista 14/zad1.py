class vehicle:
    def __init__(self, rodzaj, nr_tablica, marka, przebieg, kolor, koła, paliwo, szypkosc):
        self.rodzaj = rodzaj
        self.nr_tablica = nr_tablica
        self.marka = marka
        self.przebieg = przebieg
        self.kolor = kolor
        self.koła = koła
        self.paliwo = paliwo
        self.szypkosc = szypkosc

    def driving(self):
        print("Twój", self.rodzaj, self.nr_tablica, "jest marki", self.marka, ", ma przebieg", self.przebieg,
              "km, oraz jest koloru",
              self.kolor, ".")

    def wheels(self):
        print("Ten", self.rodzaj, "ma", self.koła, "koła")

    def __del__(self):
        print("Destruktor przyzwany, czysczczenie pamięci")


class car(vehicle):
    def __init__(self, marka, przebieg, kolor, koła, paliwo, szypkosc):
        super().__init__("samochód", "L1 KOSA", marka, przebieg, kolor, koła, paliwo, szypkosc)

    def gas(self):
        print(self.rodzaj, "jedzie na", self.paliwo)

    def __del__(self):
        print("Destruktor przyzwany, czysczczenie pamięci...")


class motorcycle(vehicle):
    def __init__(self, marka, przebieg, kolor, koła, paliwo, szypkosc):
        super().__init__("motocykl", "RST28141", marka, przebieg, kolor, koła, paliwo, szypkosc)

    def predkosc(self):
        print("Ten", self.rodzaj, "jedzie z predkoscia", self.szypkosc)

    def __del__(self):
        print("Destruktor przyzwany, czysczczenie pamięci...")


samochod = car("Bambo", "190000", "czerwony", 4, "gaz", "180km/h")
samochod.driving()
samochod.wheels()
samochod.gas()

motocykl = motorcycle("YAKUZA", "1", "czarny", 2, "diesel", "300km/h")
motocykl.driving()
motocykl.wheels()
motocykl.predkosc()
