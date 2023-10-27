class animal:
    def __init__(self, rodzaj, rasa, waga, kolor, dzwiek):
        self.rodzaj = rodzaj
        self.rasa = rasa
        self.waga = waga
        self.kolor = kolor
        self.dzwiek = dzwiek

    def hau(self):
        print("Twój", self.rodzaj, "robi", self.dzwiek, "!")

    def race(self):
        print("Twój", self.rodzaj, "jest rasy", self.rasa)


class dog(animal):
    def __init__(self, rasa, waga, kolor, ):
        super().__init__("pies", rasa, waga, kolor, "hau hau")

    def run(self):
        print(self.rodzaj, "biega!", self.dzwiek)


class cat(animal):
    def __init__(self, rasa, waga, kolor, ):
        super().__init__("kot", rasa, waga, kolor, "miau miau")

    def scratch(self):
        print("O NIE!", self.rodzaj, "PODRAPAŁ CI DYWAN I TERAZ ROBI", self.dzwiek, "!!!")


class bird(animal):
    def __init__(self, rasa, waga, kolor, ):
        super().__init__("ptak", rasa, waga, kolor, "ćwir ćwir")

    def fly(self):
        print("Lubię latać!", self.dzwiek)


class fish(animal):
    def __init__(self, rasa, waga, kolor, ):
        super().__init__("ryba", rasa, waga, kolor, "bul bul")

    def suffocate(self):
        print("O nie!", self.rodzaj, "dusi się!", self.dzwiek, ":((")

    def race(self):
        print(self.rodzaj, "nie ma rasy! tylko gatunki :D")


pies = dog("malamut", "50kg", "biało-czarny")
kot = cat("serwal", "50kg", "cętkowany")
ptak = bird("papuga", "0.5kg", "teczowa")
ryba = fish("karp", "15kg", "karpiowy")

pies.hau()
kot.hau()
ptak.hau()
ryba.hau()
pies.race()
kot.race()
ptak.race()
ryba.race()

pies.run()
kot.scratch()
ptak.fly()
ryba.suffocate()
ryba.race() #ez