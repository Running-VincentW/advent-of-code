from dataclasses import dataclass
from collections import defaultdict
import string
from typing import Any, Tuple

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
    
@dataclass(frozen=True)
class PointData:
    n: int
    _id: int


class EngineParser:

    map_width: int
    map_height: int
    point_dict: dict[Point, PointData]
    char_pts : dict[Point, str]

    def parse_map(self, input_str):
        self.char_pts = {}
        self.point_dict = {}
        lines = input_str.strip().split('\n')

        x, y = 0, 0
        point_id = 0
        start_x = -1
        n = ""

        is_reading_num = False

        def register_number(x_from: int, x_to: int, y: int):
            nonlocal point_id, n, is_reading_num
            point_data = PointData(
                n=int(n), _id=point_id
            )
            for x in range (x_from, x_to + 1):
                self.point_dict[Point(x, y)] = point_data
            point_id += 1
            n = ""
            is_reading_num = False

        for y, line in enumerate(lines):
            is_reading_num = False
            for x, char in enumerate(line):
                
                if char not in string.digits and is_reading_num:
                    register_number(start_x, x-1, y)

                if char != '.':
                    point = Point(x, y)

                    if char in string.punctuation:
                        self.char_pts[point] = char
                    
                    elif char in string.digits:
                        if not is_reading_num:
                            start_x = x
                            is_reading_num = True
                        n = f"{n}{char}"

            if is_reading_num:
                register_number(start_x, x-1, y)

        self.map_width = x + 1
        self.map_height = y + 1


    def _get_surround_points(self, point: Point) -> list[Point]:
        def is_coordinate_valid(x:int , y:int):
            is_x_valid = x >= 0 and x < self.map_width
            is_y_valid = y >= 0 and y < self.map_height
            return is_x_valid and is_y_valid
        
        neighbour_pts: list[Point] = []
        for x_offset in range (-1, 2):
            for y_offset in range (-1, 2):
                if x_offset == 0 and y_offset == 0:
                    continue
                x, y = point.x + x_offset, point.y + y_offset
                if is_coordinate_valid(x, y):
                    neighbour_pts.append(Point(x, y))
        return neighbour_pts

    def get_engine_schematics(self) -> Tuple[list[int], list[int]]:
        registered_ids = []
        schematic_num : list[int] = []
        gear = []

        for point, char in self.char_pts.items():
            neighbour_pts = self._get_surround_points(point)
            neighbour_count = 0
            neighbour_ids = []
            neighbour_nums = []

            for n_pt in neighbour_pts:
                other_cell = self.point_dict.get(n_pt)
                if other_cell and other_cell._id not in neighbour_ids:
                    neighbour_ids.append(other_cell._id)
                    neighbour_nums.append(other_cell.n)
                    neighbour_count += 1

                if other_cell and other_cell._id not in registered_ids:
                    registered_ids.append(other_cell._id)
                    schematic_num.append(other_cell.n)
            
            is_gear = (char == "*" and neighbour_count == 2)
            if is_gear:
                gear.append(neighbour_nums[0] * neighbour_nums[1])

        return schematic_num, gear
    
    def get_engine_schematics_sum(self) -> int:
        schematic_num, _ = self.get_engine_schematics()
        return sum(schematic_num)
    
    def get_gear_sum(self) -> int:
        _ , gear = self.get_engine_schematics()
        return sum(gear)
    


if __name__ == "__main__":
    from os import path
    from pathlib import Path

    path.dirname(__file__)
    target_file = Path(path.dirname(__file__), "input.txt")

    with open(target_file, "r") as file_read:
        input_doc = file_read.read()

    engine_parser = EngineParser()
    engine_parser.parse_map(input_doc)

    print(f"{engine_parser.get_engine_schematics_sum()=}")
    print(f"{engine_parser.get_gear_sum()=}")
