import operator
from collections import defaultdict
from dataclasses import dataclass
from functools import reduce


@dataclass
class Game:
    game_id: int
    draws: list[dict[str, int]]


class CubeGame:
    @staticmethod
    def _parse_one_line(line: str) -> Game:
        info, raw_draws = line.split(":")
        game_id = int(info.split()[1])
        draws = [
            {
                color: int(qty)
                for qty, color in (c.strip().split() for c in draw.split(","))
            }
            for draw in raw_draws.split(";")
        ]
        return Game(game_id=game_id, draws=draws)

    def parse(self, doc: str) -> list[Game]:
        return [self._parse_one_line(line) for line in doc.splitlines()]

    @staticmethod
    def _get_minimum_per_game(game: Game) -> dict[str, int]:
        bag_min = defaultdict(int)
        for draw in game.draws:
            for draw_color, draw_qty in draw.items():
                bag_min[draw_color] = max(bag_min[draw_color], draw_qty)
        return dict(bag_min)

    def _get_power_of_game(self, game: Game) -> int:
        bag_min = self._get_minimum_per_game(game)
        return reduce(operator.mul, bag_min.values())

    def get_games_power(self, games: list[Game]) -> int:
        powers = [self._get_power_of_game(game) for game in games]
        return sum(powers)

    @staticmethod
    def _assert_if_game_is_valid_with_bag(bag: dict[str, int], game: Game) -> bool:
        for draw in game.draws:
            for draw_color, draw_count in draw.items():
                if draw_count > bag.get(draw_color, 0):
                    return False
        return True

    def _check_games_validity(
        self, bag: dict[str, int], games: list[Game]
    ) -> list[bool]:
        return [self._assert_if_game_is_valid_with_bag(bag, game) for game in games]

    def get_valid_games_index(
        self, bag: dict[str, int], games: list[Game]
    ) -> list[int]:
        games_validity = self._check_games_validity(bag, games)
        valid_games = [game for game, valid in zip(games, games_validity) if valid]
        return [game.game_id for game in valid_games]


if __name__ == "__main__":
    from os import path
    from pathlib import Path

    path.dirname(__file__)
    target_file = Path(path.dirname(__file__), "input.txt")

    with open(target_file, "r") as file_read:
        input_doc = file_read.read()

    cubegame = CubeGame()
    games = cubegame.parse(input_doc)

    bag = {"red": 12, "green": 13, "blue": 14}

    valid_ids = cubegame.get_valid_games_index(bag, games)
    power = cubegame.get_games_power(games)

    print(valid_ids)
    print(f"{sum(valid_ids)=}")
    print(f"{power=}")
