from utils.base_solution import BaseSolution
from collections import deque
import copy

Q_NUM = 15
YEAR = 2021


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.maze = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                self.maze.append([int(let) for let in [*line]])

    def solve_part_one(self, m):
        if not m:
            m = self.maze

        dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))

        R = len(m)

        def is_valid(row: int, col: int):
            return (0 <= row < R) and (0 <= col < R)

        def bfs(m):
            q = deque()

            start = ((0, 0), 0)  # position, risk
            q.append(start)

            risks = [[float("inf") for _ in range(R)] for _ in range(R)]

            while q:
                cur = q.popleft()
                pt = cur[0]

                if cur[1] > risks[pt[0]][pt[1]]:
                    continue

                for dr, dc in dirs:
                    row = pt[0] + dr
                    col = pt[1] + dc
                    if is_valid(row, col):
                        new_risk = cur[1] + m[row][col]
                        if new_risk < risks[row][col]:
                            risks[row][col] = new_risk
                            q.append(((row, col), new_risk))
            return risks

        risks = bfs(m)

        return risks[-1][-1]

    def solve_part_two(self):
        self.load()
        orig = self.maze
        R = len(orig)

        tmp = [m * 5 for m in orig]

        maze = []

        for _ in range(5):
            maze.extend(copy.deepcopy(tmp))

        for i in range(len(maze)):
            for j in range(len(maze[0])):
                val = (i // R) + (j // R)
                orig = maze[i][j]
                if orig + val >= 10:
                    new_val = val + orig - 9
                else:
                    new_val = val + orig
                maze[i][j] = new_val

        return self.solve_part_one(maze)


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    # print(sol.solve_part_one())
    print(sol.solve_part_two())
