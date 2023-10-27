import random

class Card:
    suits = ["Pik", "Kier", "Karo", "Trefl"]
    values = [None, "As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Walet", "Dama", "Król"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __lt__(self, c2): #lt - less than (karta 1 mniejsza od 2)
        return (self.value, self.suit) < (c2.value, c2.suit)

    def __gt__(self, c2): #gt - greater (karta 1 wieksza od 2)
        return (self.value, self.suit) > (c2.value, c2.suit)

    def __repr__(self): #returnuje wartość i kolor karty jako string
        return f"{self.values[self.value]} {self.suits[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = [Card(v, s) for v in range(1, 14) for s in range(4)] #losowany jest kolor i wartość dla każdej karty
        random.shuffle(self.cards)

    def rm_card(self): #usuwa kartę z talii metodą pop, a jeżeli nie ma w niej już kard, zwraca none.
        return self.cards.pop() if self.cards else None

    def add_card(self, card): #dodaje karty do talii
        self.cards.append(card)

    def __repr__(self): #returnuje value jako string
        return ', '.join(map(str, self.cards))

    def sort(self): #sortuje karty
        self.cards.sort()


def play_game(): #Wojna
    deck = Deck()
    p1 = deck.rm_card()
    p2 = deck.rm_card()
    print(f"Gracz 1 otrzymał kartę {p1}")
    print(f"Gracz 2 otrzymał kartę {p2}")
    print(f"{'Gracz 1' if p1 > p2 else 'Gracz 2'} wygrywa!")

play_game()
