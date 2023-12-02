from advent_of_code.d2 import CubeGame, Game


class TestCubeGame:
    def test_parse_one_line(self):
        test = (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        )
        uut = CubeGame()
        actual = uut._parse_one_line(test)

        assert actual == Game(
            game_id=4,
            draws=[
                {"green": 1, "red": 3, "blue": 6},
                {"green": 3, "red": 6},
                {"green": 3, "blue": 15, "red": 14},
            ],
        )

    def test_parse_all_lines(self):
        test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        uut = CubeGame()
        actual = uut.parse(test)

        assert len(actual) == 5
        assert actual[0] == Game(
            game_id=1,
            draws=[
                {"blue": 3, "red": 4},
                {"red": 1, "green": 2, "blue": 6},
                {"green": 2},
            ],
        )
        assert actual[1] == Game(
            game_id=2,
            draws=[
                {"blue": 1, "green": 2},
                {"green": 3, "blue": 4, "red": 1},
                {"green": 1, "blue": 1},
            ],
        )

    def test_get_valid_games(self):
        test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        uut = CubeGame()
        bag = {"red": 12, "green": 13, "blue": 14}
        games = uut.parse(test)
        actual = uut.get_valid_games_index(bag, games)

        assert set(actual) == set([1, 2, 5])

    def test_get_minimum_per_game(self):
        test = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        uut = CubeGame()
        game = uut._parse_one_line(test)
        bag = uut._get_minimum_per_game(game)

        assert bag == {"blue": 6, "green": 2, "red": 4}

    def test_get_games_power(self):
        test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        uut = CubeGame()
        games = uut.parse(test)
        power = uut.get_games_power(games)

        assert power == 2286
