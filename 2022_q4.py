from utils.base_solution import BaseSolution

Q_NUM = 4
YEAR = 2022


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.pairs = []

        def make_list(task: str):
            start, finish = task.split("-")
            start = int(start)
            finish = int(finish)
            return list(range(start, finish + 1))

        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                t_1, t_2 = line.split(",")
                self.pairs.append((make_list(t_1), make_list(t_2)))

    def solve_part_one(self):
        pairs = self.pairs

        def subset(s1: list, s2: list):
            return (set(s1) <= set(s2)) or (set(s2) <= set(s1))

        nums = 0
        for pair in pairs:
            if subset(pair[0], pair[1]):
                nums += 1

        return nums

    def solve_part_two(self):
        pairs = self.pairs

        def overlap(s1: list, s2: list):
            if set(s1).intersection(s2):
                return True
            return False

        num = 0
        for pair in pairs:
            if overlap(pair[0], pair[1]):
                num += 1

        return num


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())
