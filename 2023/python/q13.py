from base_solution import BaseSolution
import numpy as np


class Moutain:
    def __init__(self, pattern: list[str]) -> None:
        self.pattern = pattern
        self.transpose = ["".join(s) for s in zip(*self.pattern)]

        self.pattern_matrix = np.array(
            [[1 if val == "#" else 0 for val in s] for s in self.pattern]
        )
        self.transpose_matrix = np.array(
            [[1 if val == "#" else 0 for val in s] for s in self.transpose]
        )

    def horizontal_check(self, h1: int, h2: int) -> bool:
        top_reversed = self.pattern[: h1 + 1][::-1]
        bottom = self.pattern[h2:]

        for l1, l2 in zip(top_reversed, bottom):
            if l1 != l2:
                return False
        return True

    def vertical_check(self, v1: int, v2: int) -> bool:
        left_reversed = self.transpose[: v1 + 1][::-1]
        right = self.transpose[v2:]

        for l1, l2 in zip(left_reversed, right):
            if l1 != l2:
                return False
        return True

    def horizontal_check_part_two(self, h1: int, h2: int) -> bool:
        top_reversed = self.pattern_matrix[: h1 + 1][::-1]
        bottom = self.pattern_matrix[h2:]

        smaller_size = min(len(top_reversed), len(bottom))

        top_reversed = top_reversed[:smaller_size]
        bottom = bottom[:smaller_size]

        diff = top_reversed - bottom
        one_or_minus_one: list[bool] = []

        for row in diff:
            for num in row:
                one_or_minus_one.append(num in [1, -1])
        return sum(one_or_minus_one) == 1

    def vertial_check_part_two(self, h1: int, h2: int) -> bool:
        left = self.transpose_matrix[: h1 + 1][::-1]
        right = self.transpose_matrix[h2:]

        smaller_size = min(len(left), len(right))

        left = left[:smaller_size]
        right = right[:smaller_size]

        diff = left - right
        one_or_minus_one: list[bool] = []

        for row in diff:
            for num in row:
                one_or_minus_one.append(num in [1, -1])
        return sum(one_or_minus_one) == 1


class Solution(BaseSolution):
    def load(self) -> list[Moutain]:
        mountains: list[Moutain] = []
        mountain: list[str] = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    if not mountain:
                        continue
                    mountains.append(Moutain(mountain))
                    mountain = []
                else:
                    mountain.append(line)
            mountains.append(Moutain(mountain))
        return mountains

    def part_one(self) -> int:
        mountains = self.load()

        horizontal = 0
        vertical = 0

        for mountain in mountains:
            found = False
            for i, (l1, l2) in enumerate(zip(mountain.pattern, mountain.pattern[1:])):
                if l1 != l2:
                    continue
                if not mountain.horizontal_check(i, i + 1):
                    continue
                horizontal += i + 1
                found = True
                break

            if not found:
                for i, (l1, l2) in enumerate(
                    zip(mountain.transpose, mountain.transpose[1:])
                ):
                    if l1 != l2:
                        continue
                    if not mountain.vertical_check(i, i + 1):
                        continue
                    vertical += i + 1
                    break
        return 100 * horizontal + vertical

    def part_two(self) -> int:
        mountains = self.load()

        horizontal = 0
        vertical = 0

        for mountain in mountains:
            found = False
            for i, _ in enumerate(mountain.pattern[:-1]):
                if not mountain.horizontal_check_part_two(i, i + 1):
                    continue
                horizontal += i + 1
                found = True
                break

            if not found:
                for i, _ in enumerate(mountain.transpose[:-1]):
                    if not mountain.vertial_check_part_two(i, i + 1):
                        continue
                    vertical += i + 1
                    break
        res = 100 * horizontal + vertical
        return res


if __name__ == "__main__":
    test_sol = Solution(13, test=True)
    sol = Solution(13, test=False)

    assert test_sol.part_one() == 405
    print(sol.part_one())

    assert test_sol.part_two() == 400
    print(sol.part_two())
