from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards = []

    def add(self, card: Card):
        if any(p.name == card.name for p in self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card:str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        c = self.find(card)
        self.cards.remove(c)

    def find(self, name: str):
        searched_card = [card for card in self.cards if card.name == name][0]
        return searched_card

    @property
    def count(self):
        return len(self.cards)

