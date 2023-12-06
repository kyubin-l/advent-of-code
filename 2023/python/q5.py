from collections import defaultdict, OrderedDict
import re
from typing import Any

from base_solution import BaseSolution


class Solution(BaseSolution):
    def load(self) -> tuple[list[int], Any]:
        """
        Parse inputs to:
        {
            "seed-to-soil": list[tuple[int, int, int]],
            "soil-to-fertilizer": list[tuple[int, int, int]],
            ...
        }
        """
        with open(self.filename) as f:
            # first line contains seeds
            seeds = re.findall(r"[\d]+", f.readline())
            seeds = [int(seed) for seed in seeds]
            # Skip blank line
            key = ""
            mappings: dict[str, list[tuple[int, ...]]] = OrderedDict()
            for line in f.readlines():
                if line.strip() == "":
                    continue
                if "map" in line:
                    key = line.split()[0]
                    continue
                if key == "":
                    raise RuntimeError("No key set!")
                if key not in mappings:
                    mappings[key] = [tuple(int(val) for val in line.split())]
                else:
                    mappings[key].append(tuple(int(val) for val in line.split()))

        return seeds, mappings

    def get_destination_source(
        self, source: int, mapping: list[tuple[int, int, int]], reverse: bool = False
    ) -> int:
        """
        Give the destination value of a source given a mapping, where the mapping is a list of
        tuples with (destination range start, source range start, range length)
        """
        for desination_start, source_start, range_length in mapping:
            if reverse is True:
                desination_start, source_start = source_start, desination_start
            delta = source - source_start
            if delta >= 0 and delta <= range_length:
                return desination_start + delta
        return source

    def part_one(self) -> int | float:
        """
        destination range, source range, range length
        """
        seeds, mappings = self.load()
        min_land = float("inf")
        for seed in seeds:
            source = seed
            for mapping in mappings.values():
                source = self.get_destination_source(source, mapping)
            min_land = min(min_land, source)
        return min_land

    def get_destination_source_and_distance_to_next_range(
        self, source: int, mapping: list[tuple[int, int, int]], reverse: bool = False
    ) -> tuple[int, int]:
        """
        Give the destination value of a source given a mapping, where the mapping is a list of
        tuples with (destination range start, source range start, range length).

        Also returns the delta to the next range
        """
        range_starts: list[int] = []
        for desination_start, source_start, range_length in mapping:
            range_starts.append(source_start)
            if reverse is True:
                desination_start, source_start = source_start, desination_start
            delta = source - source_start
            if delta >= 0 and delta <= range_length:
                return desination_start + delta, range_length - delta

        possible_starts = [start for start in range_starts if start > source]
        # no possible starts means we're beyond the largest value, so we can
        # jump as much as we want
        if not possible_starts:
            jump = -1
        else:
            jump = min(possible_starts) - source
        return source, jump

    def check_seed_in_range_and_value_to_seed_range(
        self, value: int, seeds: list[int]
    ) -> tuple[bool, int]:
        seed_starts: list[int] = []
        for seed_start, range_length in zip(seeds[::2], seeds[1::2]):
            seed_starts.append(seed_start)
            delta = value - seed_start
            if delta >= 0 and delta <= range_length:
                return True, -1
        possible_starts = [start for start in seed_starts if start > value]
        if not possible_starts:
            jump = -1
        else:
            jump = min(possible_starts) - value
        return False, jump

    def part_two(self) -> int | float:
        """
        Testing brute force seed to desination and taking min is too slow.

        Map final destination -> seed, lowest destiation first, and see if this
        value is in range of seeds
        """
        seeds, mappings = self.load()
        # Land is the first index of mappings. Order this by the min value in land
        # for the humidity-to-location key
        _, humidity_to_location = mappings.popitem()
        # Reverse the other mappings (we want to go from soil -> seed)
        reversed_mappings = OrderedDict(reversed(list(mappings.items())))

        # Reversing and brute foring still is not fast enough.
        # Try keeping track of the next boundary for each, and the minimum of those
        # will the the next jump we can take on location.
        # i.e. at what point will delta 1 in location not result in delta 1 of seeds,
        # or what jump can we take to get to the range of available seeds?

        location = 0
        while True:
            jumps: list[int] = []
            humidity, jump = self.get_destination_source_and_distance_to_next_range(
                location, humidity_to_location, reverse=True
            )
            if jump < 0:
                raise ValueError("This part should never be -1")
            jumps.append(jump)
            source = humidity
            for mapping in reversed_mappings.values():
                source, jump = self.get_destination_source_and_distance_to_next_range(
                    source, mapping, reverse=True
                )
                if jump > 0:
                    jumps.append(jump)
            in_range, jump = self.check_seed_in_range_and_value_to_seed_range(source, seeds)
            if jump > 0:
                jumps.append(jump)
            if not in_range:
                location += min(jumps)
            else:
                return location


if __name__ == "__main__":
    test_sol = Solution(5, test=True)

    assert test_sol.part_one() == 35
    assert test_sol.part_two() == 46

    sol = Solution(5, test=False)
    print(sol.part_one())
    print(sol.part_two())
