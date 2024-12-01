from base_solution import BaseSolution


class Solution(BaseSolution):
    def load(self) -> list[list[str]]:
        space: list[list[str]] = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.strip()
                space.append([*line])
        return space

    def get_rows_and_cols_to_double(
        self, space: list[list[str]]
    ) -> tuple[list[int], list[int]]:
        # Check rows
        rows_to_double: list[int] = []
        cols_to_double: list[int] = []
        for i, line in enumerate(space):
            unique_in_col = set(line)
            if (len(unique_in_col) == 1) and (unique_in_col.pop() == "."):
                rows_to_double.append(i)

        for i in range(len(space[0])):
            col = [s[i] for s in space]
            unique_in_col = set(col)
            if (len(unique_in_col) == 1) and (unique_in_col.pop() == "."):
                cols_to_double.append(i)
        return rows_to_double, cols_to_double

    def part_one(self) -> int:
        space = self.load()
        rows_to_double, cols_to_double = self.get_rows_and_cols_to_double(space)
        galaxies: list[tuple[int, int]] = []

        for row, line in enumerate(space):
            for col, v in enumerate(line):
                if v == "#":
                    galaxies.append((row, col))
        total = 0

        for i, g1 in enumerate(galaxies):
            for g2 in galaxies[i + 1 :]:
                r2, r1 = max(g1[0], g2[0]), min(g1[0], g2[0])
                c2, c1 = max(g1[1], g2[1]), min(g1[1], g2[1])

                double_rows = len([r for r in rows_to_double if (r < r2) and (r > r1)])
                double_cols = len([c for c in cols_to_double if (c < c2) and (c > c1)])

                dr = r2 - r1 + double_rows
                dc = c2 - c1 + double_cols
                dist = dr + dc
                total += dist

        return total

    def part_two(self) -> int:
        space = self.load()
        rows_to_double, cols_to_double = self.get_rows_and_cols_to_double(space)
        galaxies: list[tuple[int, int]] = []

        for row, line in enumerate(space):
            for col, v in enumerate(line):
                if v == "#":
                    galaxies.append((row, col))
        total = 0

        for i, g1 in enumerate(galaxies):
            for g2 in galaxies[i + 1 :]:
                r2, r1 = max(g1[0], g2[0]), min(g1[0], g2[0])
                c2, c1 = max(g1[1], g2[1]), min(g1[1], g2[1])

                double_rows = len([r for r in rows_to_double if (r < r2) and (r > r1)])
                double_cols = len([c for c in cols_to_double if (c < c2) and (c > c1)])

                # -1 on the multiplier as the original empty row/col is included
                # in the r2 - r1 and c2 - c1
                dr = r2 - r1 + double_rows * (1000000 - 1)
                dc = c2 - c1 + double_cols * (1000000 - 1)
                dist = dr + dc
                total += dist

        return total


if __name__ == "__main__":
    test_sol = Solution(11, test=True)
    sol = Solution(11, test=False)

    assert test_sol.part_one() == 374
    print(sol.part_one())

    # assert test_sol.part_two() == 1030
    print(sol.part_two())
