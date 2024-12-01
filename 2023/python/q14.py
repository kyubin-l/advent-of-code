from collections import defaultdict
from pprint import pprint

from base_solution import BaseSolution


class Solution(BaseSolution):
    def load(self) -> list[str]:
        rocks: list[str] = []
        with open(self.filename) as f:
            for line in f.readlines():
                rocks.append(line.strip())
        return rocks

    def part_one(self) -> int:
        rocks = self.load()
        max_score = len(rocks)
        col_scores: dict[int, int] = {i: max_score for i in range(len(rocks[0]))}
        load = 0
        for r, rock_row in enumerate(rocks):
            for i, rock in enumerate(rock_row):
                if rock == "#":
                    col_scores[i] = max_score - r - 1
                if rock == "O":
                    load += col_scores[i]
                    col_scores[i] -= 1
        return load

    def shift_west(
        self,
        round_rocks_by_row: dict[int, list[int]],
        rocks_by_row: dict[int, list[int]],
    ):
        for row in round_rocks_by_row.keys():
            rock_pos = rocks_by_row.get(row)
            cur_pos = round_rocks_by_row[row]
            if not rock_pos:
                new_pos = list(range(len(cur_pos)))
            else:
                new_pos: list[int] = []
                for p in cur_pos:
                    less_than = [r for r in rock_pos if r < p]
                    if not less_than:
                        next_west = 0
                    else:
                        next_west = max(less_than) + 1
                    while next_west in new_pos:
                        next_west += 1
                    new_pos.append(next_west)
            round_rocks_by_row[row] = new_pos
        return round_rocks_by_row

    def part_two(self) -> int:
        """
        1 cycle rolls north, then west, then south, then east

        There is not point change in the west/east cycles, but the position of the
        round rocks will change.
        """
        rocks = self.load()
        # Positions of solid rocks that do not move.
        rocks_by_col: dict[int, list[int]] = defaultdict(list)
        rocks_by_row: dict[int, list[int]] = defaultdict(list)

        round_rocks_by_col: dict[int, list[int]] = defaultdict(list)
        round_rocks_by_row: dict[int, list[int]] = defaultdict(list)

        for row, rock_row in enumerate(rocks):
            for col, rock in enumerate(rock_row):
                if rock == "#":
                    rocks_by_col[col].append(row)
                    rocks_by_row[row].append(col)
                if rock == "O":
                    round_rocks_by_col[col].append(row)3
                    round_rocks_by_row[row].append(col)

        print(rocks_by_row)
        print(round_rocks_by_row)
        for i in range(1_000_000):
            round_rocks_by_row = self.shift_west(round_rocks_by_row, rocks_by_row)
        print(round_rocks_by_row)

if __name__ == "__main__":
    test_sol = Solution(14, test=True)
    sol = Solution(14, test=False)

    # assert test_sol.part_one() == 136
    print(sol.part_one())

    assert test_sol.part_two() == 64
    print(sol.part_two())
