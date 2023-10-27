class Beer:
    def __init__(self, name, review, type, price, alc_volume):
        self.name = name
        self.review = review
        self.type = type
        self.price = price
        self.alc_volume = alc_volume

    def __lt__(self, other): #lt - less than
        return self.review < other.review

    def __eq__(self, other): #eq - equal
        return self.name == other.name


class Shop:
    def __init__(self, name):
        self.name = name
        self.beers = [] #beers to lista

    def add_beer(self, beer):
        self.beers.append(beer) #dodajemy pIWO do listy

    def sort_beers_by_review(self):
        print("\nOto nasze piwa posortowane ocenami.")
        self.beers.sort(reverse=True) #sortujemy listę od największej oceny
        for beer in shop.beers:
          print(f"Nazwa: {beer.name}, Ocena: {beer.review}")

    def sort_beers_by_name(self):
        print("\nOto nasze piwa posortowane alfabetycznie.")
        self.beers.sort(key=str) #Sortujemy listę alfabetycznie (odpowiada za to key=str)
        for beer in shop.beers:
          print(f"Nazwa: {beer.name}, Ocena: {beer.review}")



beer1 = Beer("AagerMEISTER", 10, "Ale", 10.99, 3)
beer2 = Beer("Barka", 8, "Lager", 20.99, 4.5)
beer3 = Beer("CroOro", 2, "Lager", 7.99, 2)
beer4 = Beer("Dasztelan", 5, "Jasne niepasteryzowane", 15.45, 6.5)


shop = Shop("Sklep z piwem :))")
shop.add_beer(beer1)
shop.add_beer(beer2)
shop.add_beer(beer3)
shop.add_beer(beer4)
shop.sort_beers_by_review()
shop.sort_beers_by_name()

