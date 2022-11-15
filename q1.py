from utils.base_solution import BaseSolution

Q_NUM = 1
YEAR = 2021

class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.depths = []

    def load(self):
        with open(self.filename, 'r') as f:
            for line in f.readlines():
                self.depths.append(int(line.rstrip()))
        
    def solve(self):
        return self.count_increases(self.depths)        

    def solve_part_two(self):
        depth_sums = []
        for i in range(3, len(self.depths)+1):
            depth_sums.append(sum(self.depths[i-3:i]))
        return self.count_increases(depth_sums)

    def count_increases(self, depths):
        num_increases = 0
        for i in range(1, len(depths)):
            if depths[i] > depths[i-1]:
                num_increases += 1
        return num_increases
        
    
sol = Solution(Q_NUM, YEAR)
sol.load()
print(sol.solve())
print(sol.solve_part_two())

