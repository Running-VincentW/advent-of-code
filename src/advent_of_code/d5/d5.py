import bisect
import numpy as np
from typing import Tuple


class SeedReader:
    mappings: list[Tuple[np.ndarray, np.ndarray, np.ndarray]]
    seeds: list[int] | np.ndarray
    height: list[int]

    def parse(self, input_doc: str):
        seeds, *blocks = input_doc.split("\n\n")

        seeds = list(map(int, seeds[7:].split()))
        self.seeds = seeds
        self.mappings = []

        for block in blocks:
            mapping = []
            for line in block.splitlines()[1:]:
                mapping.append(list(map(int, line.split())))

            dest, source, range_n = np.transpose(mapping)

            order = np.argsort(source)
            source = np.take_along_axis(source, order, axis=-1)
            dest = np.take_along_axis(dest, order, axis=-1)
            range_n = np.take_along_axis(range_n, order, axis=-1)
            self.mappings.append((source, dest, range_n))

        self._calculate_height_for_seeds()

    def _calculate_height_for_seed(self, seed_id: int) -> int:
        current_id = seed_id
        print(current_id, end="")
        for mapping in self.mappings:
            idx = bisect.bisect_left(mapping[0], current_id)
            # map_from_id matches source_from
            is_left_of_search = idx == len(mapping[0]) or current_id < mapping[0][idx]
            if is_left_of_search:
                idx = idx - 1

            # calculate if the map_from_id falls within this mapping range
            range_n = mapping[2][idx]
            map_from = mapping[0][idx]
            map_to = mapping[1][idx]
            map_from_limit = map_from + range_n
            is_within_source_range = (
                current_id >= map_from and current_id < map_from_limit
            )
            if is_within_source_range:
                map_offset = map_to - map_from
                current_id = current_id + map_offset
                print(f" + ( {map_to} - {map_from} ) ", end="")

            print(f" -> {current_id}", end="")

        print()
        return current_id

    def _calculate_height_for_seeds(self):
        self.height = []
        for seed_id in self.seeds:
            print(f"{seed_id=}")
            self.height.append(self._calculate_height_for_seed(seed_id))


if __name__ == "__main__":
    from pathlib import Path

    current_directory = Path(__file__).resolve().parent
    target_file = current_directory / "input.txt"

    with open(target_file, "r") as file_read:
        input_doc = file_read.read()
    #     input_doc = """seeds: 79 14 55 13

    # seed-to-soil map:
    # 50 98 2
    # 52 50 48

    # soil-to-fertilizer map:
    # 0 15 37
    # 37 52 2
    # 39 0 15

    # fertilizer-to-water map:
    # 49 53 8
    # 0 11 42
    # 42 0 7
    # 57 7 4

    # water-to-light map:
    # 88 18 7
    # 18 25 70

    # light-to-temperature map:
    # 45 77 23
    # 81 45 19
    # 68 64 13

    # temperature-to-humidity map:
    # 0 69 1
    # 1 0 69

    # humidity-to-location map:
    # 60 56 37
    # 56 93 4

    # """

    reader = SeedReader()
    reader.parse(input_doc)
    from pprint import pprint

    pprint(reader.seeds)
    print("-" * 5)
    # pprint(reader.mappings)
    # print("-" * 5)
    pprint(reader.height)
    print(f"{min(reader.height)=}")
