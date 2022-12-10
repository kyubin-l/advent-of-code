from utils.base_solution import BaseSolution
import copy


Q_NUM = 10
YEAR = 2022

class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        # For noop, keep value 0
        self.tasks = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                if line.startswith('addx'):
                    _, val = line.split()
                    self.tasks.append(int(val))
                else:
                    self.tasks.append(0)

    def solve_part_one(self):
        tasks = copy.deepcopy(self.tasks)
        print(len(tasks))
        res = [1, 1] # starting 2 values are always 1, 1
        for i in range(len(tasks)):
            res.append(sum(tasks[:i+1]))

        return len(res)

        return sum([res[20], res[60], res[100], res[140], res[180], res[220]])

    def solve_part_two(self):
        pass
    

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())