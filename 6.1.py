
import random

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'Jack', 'Queen', 'King']

        self.deck = []

        for suit in suits:                  # nested 'for' loop means we will see all pair combination
            for rank in ranks:
                card = f"{rank} of {suit}"
                self.deck.append(card)


    def pick(self):
        if len(self.deck) == 0:
            None
        else:
            self.card = random.choice(self.deck)
            self.deck.remove(self.card)
            return self.card

    def shuffle(self):
        random.shuffle(self.deck)


print('generating new deck...')
print()

d = Deck()

print('picking cards 53 times from deck...')
print()

for i in range(52):
    card = d.pick()    # when all the cards are gone, must return None
    print(card)

print()

print('generating new deck...')

e = Deck()

print('picking one card from new deck...')
print()

ecard = e.pick()
print(ecard)           # should show one card from the new deck
print()

e.shuffle()            # reorder cards internally

for i in range(52):
    card = e.pick()    # when all the cards are gone, must return None
    print(card)

print('attempting to pick from old deck again...')
print()

dcard = d.pick()
print(dcard)           # must be None

f = Deck()

f.shuffle()

print(f.deck[0])