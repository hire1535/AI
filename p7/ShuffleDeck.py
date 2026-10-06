import random
suits=["Hearts","Spade","Diamond","Club"]
ranks = [
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King", "Ace"
]
deck=[]
for suit in suits:
    for rank in ranks:
        card=suit + " of " + rank
        deck.append(card)
for card in deck:
    print(card)
random.shuffle(deck)
print("After Shuffle")
for card in deck:
    print(card)