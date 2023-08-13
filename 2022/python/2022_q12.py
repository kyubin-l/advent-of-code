from base_solution import BaseSolution
import string
import copy
from collections import deque

Q_NUM = 12
YEAR = 2022


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.letters = [*string.ascii_lowercase]

    def load(self):
        self.map = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                self.map.append([lvl for lvl in line])

        for r, line in enumerate(self.map):
            for c, lvl in enumerate(line):
                if lvl == "S":
                    self.start = (r, c)
                    self.map[r][c] = "a"
                if lvl == "E":
                    self.end = (r, c)
                    self.map[r][c] = "z"

    def solve_part_one(self, start=None):
        if not start:
            start = self.start
        map = copy.deepcopy(self.map)
        end = self.end
        rows, cols = len(map), len(map[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def oob(i, j):
            return i < 0 or i >= rows or j < 0 or j >= cols

        def bfs(map, start):
            queue = deque()
            queue.append((start, 1))
            visited = [[float("inf") for _ in range(cols)] for _ in range(rows)]

            while queue:
                cur = queue.popleft()
                if cur[0] == end:
                    return cur[1]
                r, c = cur[0]
                if cur[1] > visited[r][c]:
                    continue
                visited[r][c] = cur[1]
                idx = self.letters.index(map[r][c])
                valid = self.letters[: idx + 2]

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if oob(nr, nc):
                        continue
                    new = map[nr][nc]
                    if new not in valid:
                        continue
                    point = ((nr, nc), cur[1] + 1)
                    if point not in queue:
                        queue.append(point)
            return float("inf")

        return bfs(map, start) - 1

    def solve_part_two(self):
        map = copy.deepcopy(self.map)

        min_len = float("inf")

        for r, row in enumerate(map):
            for c, lvl in enumerate(row):
                if lvl == "a":
                    path = self.solve_part_one((r, c))
                    min_len = min(path, min_len)

        return min_len


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())
