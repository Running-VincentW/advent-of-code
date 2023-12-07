# In[0]:
from enum import IntEnum
from collections import defaultdict


class CamelCardsHand(IntEnum):
    HighCard = 1
    OnePair = 2
    TwoPair = 3
    ThreeOfAKind = 4
    FullHouse = 5
    FourOfAKind = 6
    FiveOfAKind = 7


def get_hand(cards: str):
    count_dict = defaultdict(int)
    for c in cards:
        count_dict[c] += 1

    was_three = False
    was_two = False
    hand = CamelCardsHand.HighCard
    for c, n in count_dict.items():
        if c == "J":
            continue
        if n == 5:
            hand = CamelCardsHand.FiveOfAKind
            break
        elif n == 4:
            hand = CamelCardsHand.FourOfAKind
            break
        elif (n == 3 and was_two) or (n == 2 and was_three):
            hand = CamelCardsHand.FullHouse
            break
        elif n == 3:
            hand = CamelCardsHand.ThreeOfAKind
            was_three = True
        elif n == 2 and was_two:
            hand = CamelCardsHand.TwoPair
            break
        elif n == 2:
            hand = CamelCardsHand.OnePair
            was_two = True

    n_jokes = count_dict["J"]
    if n_jokes > 0:
        if n_jokes == 5:
            hand = CamelCardsHand.FiveOfAKind
        elif n_jokes == 4:
            hand = CamelCardsHand.FiveOfAKind
        elif n_jokes == 3:  # 2 cards left
            if hand == CamelCardsHand.HighCard:
                hand = CamelCardsHand.FourOfAKind
            elif hand == CamelCardsHand.OnePair:
                hand = CamelCardsHand.FiveOfAKind
        elif n_jokes == 2:  # 3 cards left
            if hand == CamelCardsHand.HighCard:
                hand = CamelCardsHand.ThreeOfAKind
            elif hand == CamelCardsHand.OnePair:
                hand = CamelCardsHand.FourOfAKind
            elif hand == CamelCardsHand.ThreeOfAKind:
                hand = CamelCardsHand.FiveOfAKind
        elif n_jokes == 1:  # 4 cards left
            if hand == CamelCardsHand.HighCard:
                hand = CamelCardsHand.OnePair
            elif hand == CamelCardsHand.OnePair:
                hand = CamelCardsHand.ThreeOfAKind
            elif hand == CamelCardsHand.TwoPair:
                hand = CamelCardsHand.FullHouse
            elif hand == CamelCardsHand.ThreeOfAKind:
                hand = CamelCardsHand.FourOfAKind
            elif hand == CamelCardsHand.FourOfAKind:
                hand = CamelCardsHand.FiveOfAKind

    return hand


# In[1]:

input_file = [
    (x.split()[0], int(x.split()[1])) for x in open("input.txt").read().splitlines()
]

print(input_file)


# %%
hands = []
for cards, bet in input_file:
    hands.append(get_hand(cards))

# %%
cards = list(zip([x[0] for x in input_file], [x[1] for x in input_file], hands))


def custom_key(input_set: tuple[str, int, CamelCardsHand]):
    cs, _, c_type = input_set
    c_order = ["J23456789TJQKA".index(c) for c in cs]
    return (c_type, c_order)


sorted_cards = sorted(cards, key=custom_key)

for card in sorted_cards:
    print(card)
# %%

bets = [(i + 1) * b for i, (cs, b, _) in enumerate(sorted_cards)]
print(bets)
sum(bets)
# %%
