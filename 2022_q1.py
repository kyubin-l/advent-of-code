from utils.base_solution import BaseSolution

Q_NUM = 1
YEAR = 2022

class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.calories = []
        with open(self.filename) as f:
            elf = []
            for line in f.readlines():
                line = line.rstrip()
                if not line:
                    self.calories.append(elf)
                    elf = []
                else:
                    elf.append(int(line))

    def solve_part_one(self):
        cals = self.calories
        sums = []
        for elf in cals:
            sums.append(sum(elf))
        return max(sums)

    def solve_part_two(self):
        cals = self.calories
        sums = []
        for elf in cals:
            sums.append(sum(elf))
        sums.sort()
        return sums[-1] + sums[-2] + sums[-3]
    

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())