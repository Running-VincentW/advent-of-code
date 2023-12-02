import re
from dataclasses import dataclass
import itertools
from functools import reduce
import operator


@dataclass
class Game:
    game_id: int
    draws: list[dict[str, int]]


test = "Game 1: 10 green, 9 blue, 1 red; 1 red, 7 green; 11 green, 6 blue; 8 blue, 12 green"


class CubeGame:
    def _parse_one_line(self, line: str) -> Game:
        info, games = line.split(":")
        game_id = int(info.split(" ")[1])
        games = games.split(";")
        draws = []
        for game in games:
            color_info = game.split(",")
            draw = {}
            for c in color_info:
                draw_n, draw_color = c.strip().split(" ")
                draw_n = int(draw_n)
                draw_color = draw_color
                draw[draw_color] = draw_n
            draws.append(draw)
        return Game(game_id=game_id, draws=draws)

    def parse(self, doc: str) -> list[Game]:
        return [self._parse_one_line(line) for line in doc.splitlines()]

    def _get_minimum_per_game(self, game: Game) -> dict[str, int]:
        bag_min = {}
        for draw in game.draws:
            for draw_color, draw_count in draw.items():
                # does the color in the bag exceed the amt in hand?
                bag_count = bag_min.get(draw_color, 0)
                new_bag_count = max(bag_count, draw_count)
                bag_min[draw_color] = new_bag_count

        return bag_min

    def _get_power_of_game(self, game: Game) -> int:
        bag_min = self._get_minimum_per_game(game)
        power = reduce(operator.mul, list(bag_min.values()))
        return power

    def get_games_power(self, games: list[Game]):
        powers = [self._get_power_of_game(game) for game in games]
        power = reduce(operator.add, powers)
        return power

    def _assert_if_game_is_valid_with_bag(
        self, bag: dict[str, int], game: Game
    ) -> bool:
        for draw in game.draws:
            for draw_color, draw_count in draw.items():
                # does the color in the bag exceed the amt in hand?
                bag_count = bag.get(draw_color, 0)
                if draw_count > bag_count:
                    return False
        return True

    def check_games_validity(self, bag: dict[str, int], games: list[Game]):
        return [self._assert_if_game_is_valid_with_bag(bag, game) for game in games]

    def get_valid_games_index(self, bag: dict[str, int], games: list[Game]):
        bool_mask = self.check_games_validity(bag, games)
        valid_games = list(itertools.compress(games, bool_mask))
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
