from base_solution import BaseSolution
import numpy as np

Q_NUM = 9
YEAR = 2021


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.data = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                self.data.append(list(map(int, [*line])))

    def pad_data(self):
        data = np.array(self.data)
        N = len(data)
        add_col = np.zeros(N)
        add_col[:] = float("inf")
        add_row = np.zeros(N + 2)
        add_row[:] = float("inf")

        data = np.c_[add_col, data, add_col]
        data = np.r_[[add_row], data, [add_row]]
        return data

    def solve_part_one(self):
        data = self.pad_data()
        points = 0
        self.low_points = []

        for i in range(1, len(data) - 1):
            for j in range(1, len(data[0]) - 1):
                if not (data[i][j] < data[i][j + 1] and data[i][j] < data[i][j - 1]):
                    continue
                if data[i][j] < data[i + 1][j] and data[i][j] < data[i - 1][j]:
                    points += data[i][j] + 1
                    self.low_points.append((i, j))
        return points

    def solve_part_two(self):
        data = self.pad_data()

        def calculate_basin_size(i, j, basin):
            check = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for point in check:
                x, y = point
                if point in basin:
                    continue
                if (data[i][j] < data[x][y]) and (data[x][y] < 9):
                    basin.append((x, y))
                    calculate_basin_size(x, y, basin)
            return len(basin)

        sizes = []
        for low in self.low_points:
            basin = [low]
            sizes.append(calculate_basin_size(low[0], low[1], basin))

        sizes.sort()
        val = sizes[-1] * sizes[-2] * sizes[-3]

        return val


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())
