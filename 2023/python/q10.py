from dataclasses import dataclass
from pathlib import Path
from typing import Any

from base_solution import BaseSolution


@dataclass
class Point:
    row: int
    col: int
    symbol: str
    loop: bool = False
    visited: bool = False

    @property
    def coordinates(self) -> tuple[int, int]:
        return (self.row, self.col)

    def get_all_neighbors(self) -> list[tuple[int, int]]:
        return [
            (self.row + 1, self.col),
            (self.row - 1, self.col),
            (self.row, self.col + 1),
            (self.row, self.col - 1),
        ]

    @property
    def connecting_points(self) -> list[tuple[int, int]]:
        if self.symbol == "S":
            return [
                (self.row + 1, self.col),
                (self.row - 1, self.col),
                (self.row, self.col + 1),
                (self.row, self.col - 1),
            ]
        elif self.symbol == "|":
            return [
                (self.row + 1, self.col),
                (self.row - 1, self.col),
            ]
        elif self.symbol == "-":
            return [
                (self.row, self.col + 1),
                (self.row, self.col - 1),
            ]
        elif self.symbol == "L":
            return [
                (self.row - 1, self.col),
                (self.row, self.col + 1),
            ]
        elif self.symbol == "J":
            return [
                (self.row - 1, self.col),
                (self.row, self.col - 1),
            ]
        elif self.symbol == "7":
            return [
                (self.row + 1, self.col),
                (self.row, self.col - 1),
            ]
        elif self.symbol == "F":
            return [
                (self.row + 1, self.col),
                (self.row, self.col + 1),
            ]
        elif self.symbol == ".":
            return [
                (self.row + 1, self.col),
                (self.row - 1, self.col),
                (self.row, self.col + 1),
                (self.row, self.col - 1),
            ]
        raise ValueError("Invalid symbol!")


class Solution(BaseSolution):
    def load(
        self, part: int = 1
    ) -> tuple[dict[tuple[int, int], Point], tuple[int, int]]:
        if part == 2:
            filename = Path(str(self.filename).replace("q10_sample", "q10_sample_2"))
        else:
            filename = self.filename
        grid: dict[tuple[int, int], Point] = {}
        starting_coordinates: tuple[int, int] = (-1, -1)
        with open(filename) as f:
            for row, line in enumerate(f.readlines()):
                for col, symbol in enumerate(line.strip()):
                    grid[(row, col)] = Point(row, col, symbol)
                    if symbol == "S":
                        starting_coordinates = (row, col)
        if starting_coordinates == (-1, -1):
            raise ValueError("Could not find starting point")
        return grid, starting_coordinates

    def part_one(self, part: int = 1) -> int:
        grid, starting_coordinates = self.load(part=part)
        point = grid[starting_coordinates]
        point.loop = True
        looped = False
        steps = 0
        while looped is False:
            for p in point.connecting_points:
                next_point = grid.get(p)
                if next_point is None:
                    continue
                if point.coordinates not in next_point.connecting_points:
                    continue
                if next_point.symbol == "S" and steps != 1:
                    looped = True
                    break
                if next_point.loop is True:
                    continue
                point = next_point
                point.loop = True
                steps += 1
                break

        self.grid = grid
        return (steps // 2) + (steps % 2)

    def get_pipes_in_loop_above(
        self, point: Point, grid: dict[tuple[int, int], Point]
    ) -> list[Point]:
        pipes: list[Point] = []
        row, col = point.row, point.col
        while True:
            row += 1
            point_above = grid.get((row, col))
            if point_above is None:
                break
            if point_above.loop is True:
                pipes.append(point_above)
        return pipes

    def within_loop(self, point: Point, grid: dict[tuple[int, int], Point]) -> bool:
        col = point.col
        pipes = self.get_pipes_in_loop_above(point, grid)
        if not pipes:
            return False
        right = 0
        left = 0
        for pipe in pipes:
            if pipe.col != col:
                raise ValueError("Columns not equal!")
            for coord in pipe.connecting_points:
                p = grid.get(coord)
                if p is None:
                    continue
                if p.loop is False:
                    continue
                if p.col == col - 1:
                    left += 1
                if p.col == col + 1:
                    right += 1
        if (right == 0) or (left == 0):
            return False
        crosses = min(right, left)
        if crosses % 2 == 0:
            return False
        else:
            return True

    def part_two(self) -> int:
        """
        From each point, as we go towards the edge, depending on how many times
        we cross the loop will determine whether we are enclosed are not.
        An odd number of crosses to the edge in any direction would mean it is
        inclosed. If we run into an edge, where we don't cross but go along,
        we would need to consider the concavity of the pipe.

        Below idea does not work because the outside part is not always connected
        vv

        Alternatively, the grid would consist of the area with the pipe, the area
        bound within the pipe, and the area bound outside the pipe.

        Could use a bfs algo to get all the points that are _outside_ the pipe

        Junk pipes can also be part of the _outside_ loop.
        """

        # Take the same grid from part 1, the pipes with form a loop have been
        # labelled with loop = True
        # Only need to check in one direction. If there is 1 crossing in one way,
        # no matter how many crossings are on the other sides, it is gauranteed
        # to be inside the loop. For this purpose, we'll go up.
        self.part_one(part=2)
        grid = self.grid
        looped = 0
        for point in grid.values():
            if point.loop is True:
                continue
            if self.within_loop(point, grid):
                looped += 1
        return looped


if __name__ == "__main__":
    test_sol = Solution(10, test=True)
    sol = Solution(10, test=False)

    assert test_sol.part_one() == 8
    print(sol.part_one())

    assert test_sol.part_two() == 10
    print(sol.part_two())
