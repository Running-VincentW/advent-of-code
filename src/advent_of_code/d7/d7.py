from enum import IntEnum
from collections import Counter


class CamelCardsHand(IntEnum):
    HighCard = 1
    OnePair = 2
    TwoPair = 3
    ThreeOfAKind = 4
    FullHouse = 5
    FourOfAKind = 6
    FiveOfAKind = 7


class CamelCardParser:
    def parse(self, raw_input: str):
        l_cards, l_bets = zip(*(line.split() for line in raw_input.splitlines()))

        hand_type_of_cards = (self.get_hand(cards) for cards in l_cards)
        cards = list(zip(l_cards, l_bets, hand_type_of_cards))

        def custom_key(input_tuple: tuple[str, int, CamelCardsHand]):
            cs, _, c_type = input_tuple
            c_order = ["J23456789TJQKA".index(c) for c in cs]
            return (c_type, c_order)

        self.sorted_cards = sorted(cards, key=custom_key)

    @property
    def total_bets(self):
        return sum(
            (
                (rank_idx + 1) * bet
                for rank_idx, (_, bet, _) in enumerate(self.sorted_cards)
            )
        )

    @staticmethod
    def get_hand(cards: str):
        count_dict = Counter(cards)
        js = count_dict.pop("J") if "J" in count_dict else 0
        c = Counter(list(count_dict.values()))

        if 5 - js in c or js == 5:
            return CamelCardsHand.FiveOfAKind
        elif 4 - js in c:
            return CamelCardsHand.FourOfAKind
        elif (c[2] == 2 and js == 1) or (c[3] and c[2]):
            return CamelCardsHand.FullHouse
        elif 3 - js in c:
            return CamelCardsHand.ThreeOfAKind
        elif c[2] == 2:
            return CamelCardsHand.TwoPair
        elif 2 - js in c:
            return CamelCardsHand.OnePair
        else:
            return CamelCardsHand.HighCard


if __name__ == "__main__":
    from pathlib import Path

    filename = Path(__file__).resolve().parent / "input.txt"
    with open(filename) as file_read:
        raw_input = file_read.read()

    parser = CamelCardParser()
    parser.parse(raw_input)
    assert parser.total_bets == 249356515
