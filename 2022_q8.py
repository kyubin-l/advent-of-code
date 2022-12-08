from utils.base_solution import BaseSolution
import copy
from collections import namedtuple

Q_NUM = 8
YEAR = 2022


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.forest = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                self.forest.append([int(tree) for tree in line])

    def solve_part_one(self):

        def visible_in_direction(height, trees):
            return all([height > tree for tree in trees])

        forest = copy.deepcopy(self.forest)
        visible = 0
        R = len(forest)
        C = len(forest[0])
        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0 or r == R - 1 or c == C - 1:
                    visible += 1
                else:
                    height = forest[r][c]
                    dirs = [
                        forest[r][:c],
                        forest[r][c + 1:],
                        [forest[row][c] for row in range(r)],
                        [forest[row][c] for row in range(r + 1, R)]
                    ]
                    if any([visible_in_direction(height, dir) for dir in dirs]):
                        visible += 1

        return visible

    def solve_part_two(self):
        forest = copy.deepcopy(self.forest)
        R = len(forest)
        C = len(forest[0])

        def calculate_visibility(height, trees):
            visibility = 0
            for tree in trees:
                if height > tree:
                    visibility += 1
                elif height <= tree:
                    visibility += 1
                    break
            return visibility

        visibility = 0
        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0 or r == R - 1 or c == C - 1:
                    continue
                else:
                    height = forest[r][c]
                    dirs = [
                        forest[r][c - 1::-1],
                        forest[r][c + 1:],
                        [forest[row][c] for row in range(r - 1, -1, -1)],
                        [forest[row][c] for row in range(r + 1, R)]
                    ]
                    new_visibility = 1
                    for dir in dirs:
                        new_visibility *= calculate_visibility(height, dir)

                    visibility = max(visibility, new_visibility)

        return visibility
    

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())