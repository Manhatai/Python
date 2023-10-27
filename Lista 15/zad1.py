class Restaurant:
    def __init__(self, name, discounts, location):
        self.menu = { #Menu unikalne dla Restaurant zapisane w słowniku
            "Hawaiian": 7.50,
            "Champagne Ham & Cheese": 7.50,
            "Beef & Onion": 7.50,
            "Pepperoni": 7.50,
            "Simply Cheese": 7.50,
            "Bacon & Mushroom": 7.50,
            "Italiano": 7.50,
            "The Deluxe": 13.50,
            "Ham, Egg & Hollandaise": 13.50,
            "Americano": 13.50,
            "Mr Wedge": 13.50,
            "BBQ Meatlovers": 13.50
        }
        self.discounts = discounts
        self.location = location
        self.name = name

    def pizza(self):
        print(f"Witamy w {self.name} ! Oto menu które proponujemy:")
        for dish, price in self.menu.items():
            print("-",dish, ' ' * 10, 'ZŁ', price)



class IceCreamStand(Restaurant):
    def __init__(self, flavours):
        super().__init__("Lodziarnia Louda", "Zniżki dla studentów!!!", "Maja 27")
        self.flavours = flavours

    def display_flavours(self):
        print(f"Witamy w {self.name}! oto dostępne smaki lodów:")
        for flavour in self.flavours:
            print("-",flavour)


class CoffeeShop(Restaurant):
    def __init__(self, coffee_flavours):
        super().__init__("Kawiarnia Kawusia", "Posiadamy zniżki dla studentów.", "Jarocinska 11")
        self.coffee_flavours = coffee_flavours

    def display_coffees(self):
        print(f"Witamy w {self.name} ! oto dostępne smaki kawy:")
        for coffee in self.coffee_flavours:
            print("-",coffee)




restaurant = Restaurant("Pickaria", "Żadnych zniżek", "Morawskiego 15")
stand = IceCreamStand(["Czekoladowy", "Truskawkowy", "Pistacjowy"])
shop = CoffeeShop(["Americano", "Latte", "Espresso"]) #unikalne menu zapisane w jednym argumencie

print("\n")
stand.display_flavours()
print("\n")
shop.display_coffees()
print("\n")
restaurant.pizza()
