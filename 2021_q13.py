from utils.base_solution import BaseSolution
import numpy as np

Q_NUM = 13
YEAR = 2021


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.points = []
        self.commands = []
        with open(self.filename) as f:
            showing_points = True
            for line in f.readlines():
                line = line.rstrip()
                if not line:
                    showing_points = False
                    continue
                if showing_points:
                    point = tuple(map(int, line.split(',')))
                    self.points.append(point)
                else:
                    command = line.split()[-1]
                    axis, val = command.split('=')
                    self.commands.append((axis, int(val)))


    def solve_part_one(self):
        def fold_x(val):
            def mirror_x(point):
                new_x = 2 * val - point[0]
                return (new_x, point[1])
            
            top  = list(filter(lambda point: point[0] < val, self.points))
            bottom =  list(filter(lambda point: point[0] > val, self.points))
            bottom_mirrored = list(map(mirror_x, bottom))
            new = list(set(top + bottom_mirrored))
            return new
                
        fold = self.commands[0]
        folded = fold_x(fold[1])

        return len(folded)

    def solve_part_two(self):
        self.load()
        def fold_axis(val, axis):
            if axis == 'x':
                x = 0
            else:
                x = 1
            def mirror_along_axis(point):
                new_val = 2 * val - point[x]
                if not x:
                    return (new_val, point[1])
                else:
                    return (point[0], new_val)
            
            top  = list(filter(lambda point: point[x] < val, self.points))
            bottom =  list(filter(lambda point: point[x] > val, self.points))
            bottom_mirrored = list(map(mirror_along_axis, bottom))
            new = list(set(top + bottom_mirrored))
            return new

        for command in self.commands:
            axis, val = command
            self.points = fold_axis(val, axis)

        self.print_points()

    def print_points(self):
        max_x = max([point[0] for point in self.points])
        max_y = max([point[1] for point in self.points])
        grid = [
            [' ' for _ in range(max_x+1)]
            for _ in range(max_y+1)
        ]
        # grid = np.zeros((max_y+1, max_x+1))
        for point in self.points:
            x, y = point
            grid[y][x] = '@'

        for row in grid:
            print(row)

    

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())