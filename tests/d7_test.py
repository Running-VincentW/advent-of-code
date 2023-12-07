from advent_of_code.d7 import CamelCardParser, CamelCardsHand


class TestGetHand:
    def test_get_hand(self):
        parser = CamelCardParser()
        assert parser.get_hand("AAAAA") == CamelCardsHand.FiveOfAKind
        assert parser.get_hand("AAAAJ") == CamelCardsHand.FiveOfAKind
        assert parser.get_hand("AAAJJ") == CamelCardsHand.FiveOfAKind
        assert parser.get_hand("AAJJJ") == CamelCardsHand.FiveOfAKind
        assert parser.get_hand("AJJJJ") == CamelCardsHand.FiveOfAKind
        assert parser.get_hand("JJJJJ") == CamelCardsHand.FiveOfAKind
        assert parser.get_hand("JJJJJ") == CamelCardsHand.FiveOfAKind
        assert parser.get_hand("AAAAB") == CamelCardsHand.FourOfAKind
        assert parser.get_hand("AAABJ") == CamelCardsHand.FourOfAKind
        assert parser.get_hand("AABJJ") == CamelCardsHand.FourOfAKind
        assert parser.get_hand("ABJJJ") == CamelCardsHand.FourOfAKind
        assert parser.get_hand("AABBB") == CamelCardsHand.FullHouse
        assert parser.get_hand("AABBJ") == CamelCardsHand.FullHouse
        assert parser.get_hand("AAABC") == CamelCardsHand.ThreeOfAKind
        assert parser.get_hand("AABCJ") == CamelCardsHand.ThreeOfAKind
        assert parser.get_hand("ABCJJ") == CamelCardsHand.ThreeOfAKind
        assert parser.get_hand("AABBC") == CamelCardsHand.TwoPair
        assert parser.get_hand("AABCD") == CamelCardsHand.OnePair
        assert parser.get_hand("ABCDJ") == CamelCardsHand.OnePair
        assert parser.get_hand("ABCDE") == CamelCardsHand.HighCard
