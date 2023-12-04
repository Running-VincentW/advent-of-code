from typing import Tuple
import matplotlib.pyplot as plt
import networkx as nx


class ScratchCards:
    cards: list[Tuple[set, set]] = []
    total_score: int

    def parse(self, lines: str):
        for line in lines.splitlines():
            info, numbers = line.split(":")
            win_set, my_set = numbers.split("|")

            def make_set(xs: list[str]):
                return set((int(x) for x in xs))

            win_set = make_set(win_set.split())
            my_set = make_set(my_set.split())
            self.cards.append((win_set, my_set))
        self._get_points()

    def get_plot(self):
        G = nx.DiGraph()
        n_cards = len(self.cards)
        for idx, game in enumerate(reversed(self.cards)):
            arr_idx = n_cards - 1 - idx
            win_set, my_set = game
            n_matches = len(win_set & my_set)

            G.add_node(
                arr_idx,
                label=f"Card ID: {arr_idx}\nCards yield: {self.solution[arr_idx]}",
            )

            for i in range(1, n_matches + 1):
                next_idx = arr_idx + i
                G.add_edge(arr_idx, next_idx)

        pos = {node: (i, i) for i, node in enumerate(G.nodes())}
        labels = nx.get_node_attributes(G, "label")
        nx.draw(
            G,
            pos=pos,
            labels=labels,
            with_labels=True,
            node_size=500,
            node_color="skyblue",
            font_weight="bold",
            arrows=True,
            connectionstyle="arc3, rad=0.5",
        )
        plt.margins(0.2)
        plt.title("Solution Graph")
        plt.show()

    def get_cards(self) -> int:
        self.solution = {}

        n_cards = len(self.cards)
        for idx, game in enumerate(reversed(self.cards)):
            arr_idx = n_cards - 1 - idx
            win_set, my_set = game
            n_matches = len(win_set & my_set)

            # determine this functions composition
            # for e.g., game 1 has two matches
            # f(1) = f(2) + f(3)
            game_solution = 1 + sum(
                (self.solution[arr_idx + i] for i in range(1, n_matches + 1))
            )
            self.solution[arr_idx] = game_solution
            # print(f"Game {game_id} has derived {game_solution} cards.")

        # With all dynamic programming solution set, now it is the time to calculate the total cards from original hand

        return sum(list(self.solution.values()))

    def _get_points(self):
        total_score = 0
        for win_set, my_set in self.cards:
            win_numbers = win_set & my_set
            n_wins = len(win_numbers)
            score = (2 ** (n_wins - 1)) if n_wins > 0 else 0
            total_score += score
        self.total_score = total_score

    def _win_set(self, card_id: int):
        return self.cards[card_id][0]

    def _my_set(self, card_id: int):
        return self.cards[card_id][1]


if __name__ == "__main__":
    from pathlib import Path

    current_directory = Path(__file__).resolve().parent
    target_file = current_directory / "input.txt"

    with open(target_file, "r") as file_read:
        input_doc = file_read.read()

    cards = ScratchCards()
    cards.parse(input_doc)
    print(cards.get_cards())
    cards.get_plot()
