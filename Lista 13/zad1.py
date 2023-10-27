class car:
    def __init__(self, brand, model, age, mileage, colour, type, price):
        self.brand = brand
        self.model = model
        self.age = age
        self.mileage = mileage
        self.colour = colour
        self.type = type
        self.price = price

    def driveforward(self):
        return "{} {} jedzie doprzodu".format(self.brand, self.model)

    def offer(self):
        return "{} {} koloru {} kosztuje {} i ma przebieg {}".format(self.brand, self.model, self.colour, self.price,
                                                                     self.mileage)

    def service(self, km):
        return "{} {} po {} wciąż ma się dobrze. Za kolejne {} trzeba będzię wymienić olej.".format(self.brand,
                                                                                                    self.model,
                                                                                                    self.mileage, km)

    def racetrack(self):
        return "{} nieźle zapierdala po torze.".format(self.brand)

    def flex(self):
        return "Twoi znajomi są zachwyceni {} {}. Miejmy nadzieje, że lubią też brak pieniędzy.".format(self.brand,
                                                                                                        self.model)


ferrari = car("Ferrari", "F8", "2019", "10 000km", "red", "coupe", "60 000zł")

print(ferrari.driveforward())
print(ferrari.offer())
print(ferrari.service("1000km"))
print(ferrari.racetrack())
print(ferrari.flex())
