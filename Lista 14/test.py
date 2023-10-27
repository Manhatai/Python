class bird:

    def __init__(self, gatunek, szybkość):
        self.gatunek = gatunek
        self.szybkość = szybkość

    def fly(self):
        print("Tu", self.gatunek, ". Lecimy i osiągniemy prędkość", self.szybkość)


class eagle(bird):

    def __init__(self, szybkość):
        super().__init__("orzeł", szybkość)

    def attack(self):
        print("Tu", self.gatunek, ". Do atakuuuuu!")


class penguin(bird):

    def __init__(self, szybkość):
        super().__init__("pingwin", szybkość)

    def slide(self):
        print("Tu", self.gatunek, ". Bziuuuuum")

    def fly(self):
        print("Tu", self.gatunek, ". Nie potrafię latać :((")


orzel = eagle(90)
orzel.fly()
orzel.attack()

pingwin = penguin(50)
pingwin.slide()
pingwin.fly()
