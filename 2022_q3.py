from utils.base_solution import BaseSolution
import string

Q_NUM = 3
YEAR = 2022


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        lower = [*string.ascii_lowercase]
        upper = [*string.ascii_uppercase]
        self.letters = lower + upper

    def load(self):
        self.items = []
        with open(self.filename) as f:
            for line in f.readlines():
                self.items.append(line.rstrip())

    def solve_part_one(self):
        def find_repeating(item: str):
            n = len(item)
            r_1 = item[: n // 2]
            r_2 = item[n // 2 :]
            return set(r_1).intersection(r_2).pop()

        points = 0
        for item in self.items:
            repeating = find_repeating(item)
            points += self.letters.index(repeating) + 1

        return points

    def solve_part_two(self):
        def find_repeating(s1: str, s2: str, s3: str):
            return set(s1).intersection(s2).intersection(s3).pop()

        points = 0
        for i in range(0, len(self.items), 3):
            repeating = find_repeating(
                self.items[i], self.items[i + 1], self.items[i + 2]
            )
            points += self.letters.index(repeating) + 1

        return points


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())
