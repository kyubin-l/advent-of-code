from utils.base_solution import BaseSolution

Q_NUM = 11
YEAR = 2021

class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.grid = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                vals = list(map(int, [*line]))
                self.grid.append(vals)

    def print_grid(self):
        for line in self.grid:
            print(line)

    def solve_part_one(self, num_steps, part_1=True):
        def get_neighbors(i, j):
            n = [
                (i-1, j-1),
                (i-1, j),
                (i-1, j+1),
                (i, j-1),
                (i, j+1),
                (i+1, j-1),
                (i+1, j),
                (i+1, j+1),
                ]
            return n

        def in_bound(i, j):
            return (0 <= i < len(self.grid)) and (0 <= j < len(self.grid[0]))

        def flash(i, j, flashed):
            """
            Modifies the neighbors and returns the number of total EXTRA flashes
            caused by this octopus flashing
            """
            self.grid[i][j] = 0
            flashed[i][j] = True
            extra_flashes = 0
            for point in get_neighbors(i, j):
                y, x = point[0], point[1]
                if (not in_bound(y, x)) or flashed[y][x]:
                    continue
                else:
                    self.grid[y][x] += 1
                    if self.grid[y][x] == 10:
                        extra_flashes += 1
                        extra_flashes += flash(y, x, flashed)

            return extra_flashes

        def step():
            flashed = [
                [False for _ in range(len(self.grid[0]))]
                for _ in range(len(self.grid))
            ]
            num_flashes = 0
            for i, row in enumerate(self.grid):
                for j, _ in enumerate(row):
                    if flashed[i][j]:
                        continue
                    self.grid[i][j] += 1
                    if self.grid[i][j] == 10:
                        num_flashes += 1
                        num_flashes += flash(i, j, flashed)

            return num_flashes


        if part_1:
            total_flashes = 0
            for _ in range(num_steps):
                num_flashes = step()
                total_flashes += num_flashes

            return total_flashes
            
        # Part 2
        else:
            i = 0
            grid_size = len(self.grid) * len(self.grid[0])
            while True:
                num_flashes = step()
                i += 1
                if num_flashes == grid_size:
                    self.print_grid()
                    print(f'All octopuses will flash at step {i}')
                    return i

    def solve_part_two(self):
        self.load()
        return self.solve_part_one(None, False)
    

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one(100))
    print(sol.solve_part_two())