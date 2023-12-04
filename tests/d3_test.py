from advent_of_code.d3 import EngineParser, Point, PointData

test_map = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


class TestEngineParser:
    def test_read_int_from_map(self):
        uut = EngineParser()
        uut.parse_map(test_map)

        assert list(uut.point_dict.items()) == [
            (Point(x=0, y=0), PointData(n=467, _id=0)),
            (Point(x=1, y=0), PointData(n=467, _id=0)),
            (Point(x=2, y=0), PointData(n=467, _id=0)),
            (Point(x=5, y=0), PointData(n=114, _id=1)),
            (Point(x=6, y=0), PointData(n=114, _id=1)),
            (Point(x=7, y=0), PointData(n=114, _id=1)),
            (Point(x=2, y=2), PointData(n=35, _id=2)),
            (Point(x=3, y=2), PointData(n=35, _id=2)),
            (Point(x=6, y=2), PointData(n=633, _id=3)),
            (Point(x=7, y=2), PointData(n=633, _id=3)),
            (Point(x=8, y=2), PointData(n=633, _id=3)),
            (Point(x=0, y=4), PointData(n=617, _id=4)),
            (Point(x=1, y=4), PointData(n=617, _id=4)),
            (Point(x=2, y=4), PointData(n=617, _id=4)),
            (Point(x=7, y=5), PointData(n=58, _id=5)),
            (Point(x=8, y=5), PointData(n=58, _id=5)),
            (Point(x=2, y=6), PointData(n=592, _id=6)),
            (Point(x=3, y=6), PointData(n=592, _id=6)),
            (Point(x=4, y=6), PointData(n=592, _id=6)),
            (Point(x=6, y=7), PointData(n=755, _id=7)),
            (Point(x=7, y=7), PointData(n=755, _id=7)),
            (Point(x=8, y=7), PointData(n=755, _id=7)),
            (Point(x=1, y=9), PointData(n=664, _id=8)),
            (Point(x=2, y=9), PointData(n=664, _id=8)),
            (Point(x=3, y=9), PointData(n=664, _id=8)),
            (Point(x=5, y=9), PointData(n=598, _id=9)),
            (Point(x=6, y=9), PointData(n=598, _id=9)),
            (Point(x=7, y=9), PointData(n=598, _id=9)),
        ]

    def test_get_engine_schematics(self):
        uut = EngineParser()
        uut.parse_map(test_map)

        assert uut.get_engine_schematics_sum() == 4361

    def test_get_gear_sum(self):
        uut = EngineParser()
        uut.parse_map(test_map)

        assert uut.get_gear_sum() == 467835
