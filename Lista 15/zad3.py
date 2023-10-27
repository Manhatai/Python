class Citizen:
    def __init__(self, name=input("Podaj imię: "), surname=input("Podaj nazwisko: "), street=input("Podaj nazwę ulicy: "),
                 house_number=input("Podaj numer domu: "), postal_code=input("Podaj kod pocztowy: "), city=input("Podaj miasto: ")):
        self.name = name
        self.surname = surname
        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.city = city

    def create_card(self):
        separator = "----------------------"
        card = f"{separator}\n{self.name} {self.surname}\nul. {self.street} {self.house_number}\n{self.postal_code} {self.city}\n{separator}"
        return card

    def save_card_to_file(self, filename="card.txt"):
        card = self.create_card()
        with open(filename, "w") as file:
            file.write(card)

citizen = Citizen()
card = citizen.create_card()
print(card)
citizen.save_card_to_file()
