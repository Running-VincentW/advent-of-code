from typing import Tuple


class ScratchCards:
    cards: list[Tuple[set, set]] = []
    total_score: int

    def parse(self, lines: str):
        for line in lines.splitlines():
            info, numbers = line.split(":")
            win_set, my_set = numbers.split("|")
            make_set = lambda xs: set((int(x) for x in xs))
            win_set = make_set(win_set.split())
            my_set = make_set(my_set.split())
            self.cards.append((win_set, my_set))
        total_score = self.get_points()

    def get_cards(self) -> int:
        solution = {}

        n_cards = len(self.cards)
        for idx, game in enumerate(reversed(self.cards)):
            arr_idx = n_cards - 1 - idx
            game_id = n_cards - idx

            win_set, my_set = game
            n_matches = len(win_set & my_set)

            # determine this functions composition
            # for e.g., game 1 has two matches
            # f(1) = f(2) + f(3)
            game_solution = 1 + sum(
                (solution[arr_idx + i] for i in range(1, n_matches + 1))
            )
            solution[arr_idx] = game_solution

            print(f"Game {game_id} has derived {game_solution} cards.")

        # With all dynamic programming solution set, now it is the time to calculate the total cards from original hand
        return sum(list(solution.values()))

    def get_points(self):
        total_score = 0
        for win_set, my_set in self.cards:
            win_numbers = win_set & my_set
            n_wins = len(win_numbers)
            score = (2 ** (n_wins - 1)) if n_wins > 0 else 0
            total_score += score
        self.total_score = total_score

    def win_set(self, card_id: int):
        return self.cards[card_id][0]

    def my_set(self, card_id: int):
        return self.cards[card_id][1]


if __name__ == "__main__":
    from pathlib import Path

    current_directory = Path(__file__).resolve().parent
    target_file = current_directory / "input.txt"

    with open(target_file, "r") as file_read:
        input_doc = file_read.read()

    #     input_doc = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    # Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    # Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    # """

    cards = ScratchCards()
    cards.parse(input_doc)
    print(cards.cards)
    print(cards.get_cards())
