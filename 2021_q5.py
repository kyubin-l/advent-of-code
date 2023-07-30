from utils.base_solution import BaseSolution

Q_NUM = 5
YEAR = 2021

"""
Data given in line segments
x1, y1 -> x2, y2
Assuming only positive numbers?
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "f({self.x}, {self.y})"


class Grid:
    def __init__(self, xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.grid = [[0 for _ in range(self.xmax + 1)] for _ in range(self.ymax + 1)]

    def mark_straight_line(self, p1, p2):
        """
        Assumings that either p1.x == p2.x
        or p1.y == p2.y
        """
        if (p1.x != p2.x) and (p1.y != p2.y):
            return

        if p1.x == p2.x:
            y1, y2 = sorted([p1.y, p2.y])
            for y in range(y1, y2 + 1):
                self.grid[p1.x][y] += 1
        else:
            x1, x2 = sorted([p1.x, p2.x])
            for x in range(x1, x2 + 1):
                self.grid[x][p1.y] += 1

    def mark_line(self, p1, p2):
        """
        Given that they are perfectly diagonal.
        Options:
            1. Top left -> bottom right (p2.x > p1.x, p2.y > p1.y)
            2. Bottom left -> top right (p2.x > p1.x, p2.y < p1.y)
            3. Top right -> bottom left (p2.x < p1.x, p2.y > p1.y)
            4. Bottom right -> top left (p2.x < p1.x, p2.y < p1.y)
        """

        if (p1.x == p2.x) or (p1.y == p2.y):
            self.mark_straight_line(p1, p2)
            return

        x_dir = 1 if p2.x > p1.x else -1
        y_dir = 1 if p2.y > p1.y else -1

        x_coords = list(range(p1.x, p2.x + x_dir, x_dir))
        y_coords = list(range(p1.y, p2.y + y_dir, y_dir))

        for x, y in zip(x_coords, y_coords):
            self.grid[x][y] += 1

    def calculate_double_crossed(self):
        total = 0
        for row in self.grid:
            total += sum(num > 1 for num in row)
        return total


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lines = []

    def load(self):
        with open(self.filename) as f:
            for line in f.readlines():
                p1, _, p2 = line.rstrip().split()
                p1_x, p1_y = list(map(int, p1.split(",")))
                p2_x, p2_y = list(map(int, p2.split(",")))
                p1 = Point(p1_x, p1_y)
                p2 = Point(p2_x, p2_y)
                self.lines.append((p1, p2))

    def initialise_grid(self):
        xmax = max(max(line[0].x, line[1].x) for line in self.lines)
        ymax = max(max(line[0].y, line[1].y) for line in self.lines)
        self.grid = Grid(xmax, ymax)

    def solve_part_one(self):
        for line in self.lines:
            self.grid.mark_straight_line(line[0], line[1])
        return self.grid.calculate_double_crossed()

    def solve_part_two(self):
        for line in self.lines:
            self.grid.mark_line(line[0], line[1])
        return self.grid.calculate_double_crossed()


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    sol.initialise_grid()
    print(sol.solve_part_one())
    sol.initialise_grid()
    print(sol.solve_part_two())
