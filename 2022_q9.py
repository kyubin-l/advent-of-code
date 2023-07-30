from utils.base_solution import BaseSolution
from collections import namedtuple
import itertools
import copy
import math

Move = namedtuple("Move", "dir x")

Q_NUM = 9
YEAR = 2022


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mapping = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    def load(self):
        self.moves = []
        with open(self.filename) as f:
            for line in f.readlines():
                dir, x = line.rstrip().split()
                self.moves.append(Move(dir=dir, x=int(x)))

    def solve_part_one(self):
        moves = copy.deepcopy(self.moves)
        positions = list(itertools.product([-1, 0, 1], repeat=2))

        def touching(H, T):
            for pos in positions:
                if (H[0] + pos[0], H[1] + pos[1]) == T:
                    return True
            return False

        def move_T(H, T):
            if abs(H[0] - T[0]) == 2:
                return ((H[0] + T[0]) // 2, H[1])
            elif abs(H[1] - T[1]) == 2:
                return (H[0], (H[1] + T[1]) // 2)
            return -1

        H = (0, 0)
        T = (0, 0)

        visited = set()
        visited.add(T)

        for move in moves:
            dir = self.mapping[move.dir]
            for _ in range(move.x):
                H = (H[0] + dir[0], H[1] + dir[1])
                if not touching(H, T):
                    T = move_T(H, T)
                    visited.add(T)

        return len(visited)

    def solve_part_two(self):
        moves = copy.deepcopy(self.moves)
        positions = list(itertools.product([-1, 0, 1], repeat=2))

        def touching(H, T):
            for pos in positions:
                if (H[0] + pos[0], H[1] + pos[1]) == T:
                    return True
            return False

        def move_T(H, T):
            if (abs(H[0] - T[0]) == 2) and (abs(H[1] - T[1]) == 2):
                return ((H[0] + T[0]) // 2, (H[1] + T[1]) // 2)
            if abs(H[0] - T[0]) == 2:
                return ((H[0] + T[0]) // 2, H[1])
            if abs(H[1] - T[1]) == 2:
                return (H[0], (H[1] + T[1]) // 2)

        rope = [(0, 0)] * 10  # index 0 is head, index 9 is tail

        visited = set()
        visited.add(rope[-1])

        for move in moves:
            dir = self.mapping[move.dir]
            for _ in range(move.x):
                H = rope[0]
                H = (H[0] + dir[0], H[1] + dir[1])
                rope[0] = H
                for i in range(1, len(rope)):
                    if touching(rope[i - 1], rope[i]):
                        continue
                    T = rope[i]
                    T = move_T(rope[i - 1], T)
                    rope[i] = T
                    if i == 9:
                        visited.add(T)

        return len(visited)


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())
