class Deck:
    CARDS = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
    ]

    def __init__(self, num_decks=1):
        self.cards = self.CARDS*num_decks*4

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)