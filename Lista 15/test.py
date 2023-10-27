import random

class Card:
    suits = ["Pik", "Kier", "Karo", "Trefl"]
    values = [None, "As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Walet", "Dama", "Król"]

    def __init__(self, v, s):
        self.value, self.suit = v, s

    def __lt__(self, c2):
        return (self.value, self.suit) < (c2.value, c2.suit)

    def __gt__(self, c2):
        return (self.value, self.suit) > (c2.value, c2.suit)

    def __repr__(self):
        return f"{self.values[self.value]} {self.suits[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = [Card(v, s) for v in range(1, 14) for s in range(4)]
        random.shuffle(self.cards)

    def rm_card(self):
        return self.cards.pop() if self.cards else None

    def add_card(self, card):
        self.cards.append(card)

    def __repr__(self):
        return ', '.join(map(str, self.cards))

    def sort(self):
        self.cards.sort()


def play_game():
    deck = Deck()
    p1c = deck.rm_card()
    p2c = deck.rm_card()
    print(f"Gracz 1 otrzymał kartę {p1c}")
    print(f"Gracz 2 otrzymał kartę {p2c}")
    print(f"{'Gracz 1' if p1c > p2c else 'Gracz 2'} wygrywa!")

play_game()
