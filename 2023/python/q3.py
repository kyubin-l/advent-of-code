import re
from typing import NamedTuple

from base_solution import BaseSolution


class Point(NamedTuple):
    row: int
    col: int

    def __repr__(self) -> str:
        return f"({self.row}, {self.col})"

    def get_neighbors(self, max_row: int, max_col: int) -> list["Point"]:
        """
        Get neighboring points of a given point.
        Includes coordinates of current point.
        """
        neighbors: list["Point"] = []
        for r in range(max(0, self.row - 1), min(max_row, self.row + 1) + 1):
            for c in range(
                max(
                    0,
                    self.col - 1,
                ),
                min(max_col, self.col + 1) + 1,
            ):
                neighbors.append(Point(r, c))
        return neighbors


class Solution(BaseSolution):
    def load(self) -> list[str]:
        with open(self.filename) as f:
            strings = f.read().splitlines()
        return strings

    def part_one(self) -> int:
        input = self.load()
        adjacent_points: set[Point] = set()
        rows, cols = len(input) - 1, len(input[0]) - 1

        for row, line in enumerate(input):
            for col, pattern in enumerate(line):
                if pattern == "." or pattern.isdigit():
                    continue
                symbol = Point(row, col)
                adjacent_points.update(symbol.get_neighbors(rows, cols))

        sum_part_numbers: list[int] = []
        for row, line in enumerate(input):
            for num in re.finditer(r"[\d]+", line):
                val = int(num.group())
                for col in range(num.start(), num.end()):
                    if Point(row, col) not in adjacent_points:
                        continue
                    sum_part_numbers.append(val)
                    break

        return sum(sum_part_numbers)

    def part_two(self) -> int:
        input = self.load()
        nums_adjacent_to_gear: dict[Point, list[int]] = {}
        rows, cols = len(input) - 1, len(input[0]) - 1

        for row, line in enumerate(input):
            for col, pattern in enumerate(line):
                if pattern != "*":
                    continue
                symbol = Point(row, col)
                nums_adjacent_to_gear[symbol] = []

        for row, line in enumerate(input):
            for num in re.finditer(r"[\d]+", line):
                val = int(num.group())
                for col in range(num.start(), num.end()):
                    # Check if there are any gears adjacent
                    neighbors = set(Point(row, col).get_neighbors(rows, cols))
                    gears_adjacent = neighbors.intersection(set(nums_adjacent_to_gear.keys()))
                    # If no gear or more than 1 gear
                    if len(gears_adjacent) != 1:
                        continue
                    gear = gears_adjacent.pop()
                    nums_adjacent_to_gear[gear].append(val)
                    break

        gear_ratio = 0
        for gear, neighbors in nums_adjacent_to_gear.items():
            if len(neighbors) != 2:
                continue
            gear_ratio += neighbors[0] * neighbors[1]

        return gear_ratio


if __name__ == "__main__":
    test_sol = Solution(3, test=True)
    assert test_sol.part_one() == 4361
    assert test_sol.part_two() == 467835

    sol = Solution(3, test=False)
    print(sol.part_one())
    print(sol.part_two())
