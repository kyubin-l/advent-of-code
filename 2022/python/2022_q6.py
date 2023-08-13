from base_solution import BaseSolution

Q_NUM = 6
YEAR = 2022


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        with open(self.filename) as f:
            self.pattern = f.readline().rstrip()

    def solve_part_one(self):
        pattern = self.pattern

        for i in range(len(pattern) - 3):
            if len(set(pattern[i : i + 4])) == 4:
                return i + 4
        return

    def solve_part_two(self):
        pattern = self.pattern

        for i in range(len(pattern) - 13):
            if len(set(pattern[i : i + 14])) == 14:
                return i + 14
        return


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())
