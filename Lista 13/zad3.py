konto_bankowe = 10000


class smartphone:
    def __init__(self, firma, przekatna, iloscram, iloscpam, jakosckam, cena, wejscielad, rozdzielczosc, ):
        self.firma = firma
        self.prekatna = przekatna
        self.iloscram = iloscram
        self.iloscpam = iloscpam
        self.jakosckam = jakosckam
        self.cena = cena
        self.wejscielad = wejscielad
        self.rozdzielczosc = rozdzielczosc

    def kupno(self):
        return "Wow! Kupiles {}! Thats emejzing.".format(self.firma)

    def spec(self):
        return "Telefon który wybrałeś ma przekątną {} cali, {} ramu, {} wbudowanej pamięci, aparat z {}, ma wejście {} i rozdzielczość {}.".format(
            self.prekatna, self.iloscram, self.iloscpam, self.jakosckam, self.wejscielad, self.rozdzielczosc)

    def price(self):
        if self.cena > 2300:
            return "Kurde no calkiem drogi ten fonik"
        else:
            return "W porownaniu z pozostalymi cenowo jest niezle"

    def flexfactor(self):
        if x == "iPhone":
            return "Ale z ciebie bogol no niezle kidosku + 10 do respectu"
        if x == "Xiaomi":
            return "Chyba nikt cie w szkole nie lubi biedaczku malutki"
        else:
            return "Normik"

    def staradzwoni(self):
        if konto_bankowe < 7000:
            return "Twoja stara zadzwoni zaraz i zapyta na jakie ty glupoty wydajesz."
        else:
            return "Wow zostanie ci jeszcze na malucha :)"


iPhone = smartphone("Apple", "6,1''", "64GB", "256GB", "12 Mpix + 12 Mpix", 3699, "Lightning", "2532 x 1170 pikseli")
Samsung = smartphone("Samsung", "6,8''", "12GB", "512GB", "200 Mpix + 12 Mpix + 10 Mpix + 10 Mpix", 6999, "USB-C",
                     "3088 x 1440 pikseli")
Xiaomi = smartphone("Xiaomi", "6,77''", "8GB", "128GB", "200 Mpix", 2299, "USB-C", "2400 x 1080 pikseli")
Nokia = smartphone("Nokia", "6,43''", "8GB", "256GB", "50 Mpix", 2599, "USB-C", "2400 x 1080 pikseli")

print()
print(f"Stan twojego konta to: {konto_bankowe}")
print()
x = input("Jaki telefon kupujesz? (iPhone, Samsung, Xiaomi, Nokia): ")
print()

if x == "Nokia":
    konto_bankowe = konto_bankowe - 2599
if x == "iPhone":
    konto_bankowe = konto_bankowe - 3699
if x == "Samsung":
    konto_bankowe = konto_bankowe - 6999
if x == "Xiaomi":
    konto_bankowe = konto_bankowe - 2299


def kupnotelefonu():
    if x == "Nokia":
        print(Nokia.kupno())
        print(Nokia.spec())
        print(Nokia.price())
        print(Nokia.flexfactor())
        print(Nokia.staradzwoni())

    if x == "iPhone":
        print(iPhone.kupno())
        print(iPhone.spec())
        print(iPhone.price())
        print(iPhone.flexfactor())
        print(iPhone.staradzwoni())

    if x == "Samsung":
        print(Samsung.kupno())
        print(Samsung.spec())
        print(Samsung.price())
        print(Samsung.flexfactor())
        print(Samsung.staradzwoni())

    if x == "Xiaomi":
        print(Xiaomi.kupno())
        print(Xiaomi.spec())
        print(Xiaomi.price())
        print(Xiaomi.flexfactor())
        print(Xiaomi.staradzwoni())


kupnotelefonu()
print(f"Stan twojego konta to {konto_bankowe}, GRATULACJE!!!")

