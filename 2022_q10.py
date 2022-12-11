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
        """
        if noop i.e. 0, cycle value is previous calue
        else:
            cycle value is previous value, and the next value is previous value
            plus the new value
        """
        tasks = copy.deepcopy(self.tasks)
        x = []  # Keeping values during cycle
        X = 1
                
                
        for val in tasks:
            # Keeping values in x during that cycle, index 0 -> 1st cycle
            x.append((X, X))
            # If val == 0, it's a noop, so just continue
            if val:
                x.append((X, X + val))
                X += val
                
        self.x = x
        print(x)
        return sum(x[i][0] * (i + 1) for i in [19, 59, 99, 139, 179, 219])
                

    def solve_part_two(self):
        tasks = copy.deepcopy(self.tasks)
        
        CRT = []
        row = []
        x = self.x # x holds values at end of cycle, not during

        for i in range(len(x)):
            X = x[i][0]
            if len(row) == 40:
                CRT.append(row)
                row = []

            if len(row) in [X-1, X, X+1]:
                row.append('#')
            else:
                row.append('.')
                
        CRT.append(row)

        for row in CRT:
            print(row)

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())