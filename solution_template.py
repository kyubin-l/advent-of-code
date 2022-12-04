from utils.base_solution import BaseSolution

Q_NUM = 1
YEAR = 1

class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        return super().load()

    def solve_part_one(self):
        pass

    def solve_part_two(self):
        pass
    

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    print(sol.solve_part_one())
    print(sol.solve_part_two())