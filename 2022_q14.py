from utils.base_solution import BaseSolution
import numpy as np

Q_NUM = 14
YEAR = 2022


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.lines = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                raw_points = line.split(" -> ")
                line = []
                for raw_point in raw_points:
                    point = tuple([int(coord) for coord in raw_point.split(",")])
                    line.append(point)
                self.lines.append(line)

    def _make_rocks(self):
        rocks = set()
        for line in self.lines:
            for p1, p2 in zip(line, line[1:]):
                dx = int((p2[0] - p1[0]) / abs(p2[0] - p1[0])) if p2[0] != p1[0] else 0
                dy = int((p2[1] - p1[1]) / abs(p2[1] - p1[1])) if p2[1] != p1[1] else 0

                while p1 != p2:
                    rocks.add(p1)
                    p1 = (p1[0] + dx, p1[1] + dy)
                rocks.add(p2)
        return rocks

    def solve_part_one(self):
        rocks = self._make_rocks()

        max_y = 0
        for rock in rocks:
            max_y = max(rock[1], max_y)

        start = (500, 0)

        def next_step(pos):
            if (pos[0], pos[1] + 1) not in rocks:
                return (pos[0], pos[1] + 1)

            if (pos[0] - 1, pos[1] + 1) not in rocks:
                return (pos[0] - 1, pos[1] + 1)

            if (pos[0] + 1, pos[1] + 1) not in rocks:
                return (pos[0] + 1, pos[1] + 1)

            return pos

        def oob(pos):
            if pos[1] > max_y:
                return True
            return False

        sand = start
        sand_count = 0
        while not oob(sand):
            next_sand = next_step(sand)
            if sand == next_sand:
                rocks.add(sand)
                sand_count += 1
                sand = start
                continue
            sand = next_sand

        return sand_count

    def print_cave(self, rocks):
        max_x, max_y = 0, 0
        min_x, min_y = float("inf"), float("inf")
        for rock in rocks:
            max_x = max(max_x, rock[0])
            max_y = max(max_y, rock[1])
            min_x = min(min_x, rock[0])
            min_y = min(min_y, rock[1])

        cave = [[" " for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

        for rock in rocks:
            cave[rock[1] - min_y][rock[0] - min_x] = "#"

        for line in cave:
            print(line)
        print("----------------------------------------------------")

    def solve_part_two(self):
        rocks = self._make_rocks()

        max_y = 0
        for rock in rocks:
            max_y = max(rock[1], max_y)

        max_y += 2

        start = (500, 0)

        def next_step(pos):
            if pos[1] + 1 == max_y:
                return pos

            if (pos[0], pos[1] + 1) not in rocks:
                return (pos[0], pos[1] + 1)

            if (pos[0] - 1, pos[1] + 1) not in rocks:
                return (pos[0] - 1, pos[1] + 1)

            if (pos[0] + 1, pos[1] + 1) not in rocks:
                return (pos[0] + 1, pos[1] + 1)

            return pos

        sand = start
        sand_count = 0
        while True:
            next_sand = next_step(sand)
            if next_sand == start:
                break
            if sand == next_sand:
                rocks.add(sand)
                sand_count += 1
                sand = start
                # self.print_cave(rocks)
                continue
            sand = next_sand

        return sand_count + 1


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())
