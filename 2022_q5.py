from utils.base_solution import BaseSolution
from collections import namedtuple, deque
import re
import copy

Movement = namedtuple("Movement", "x, start, end")

Q_NUM = 5
YEAR = 2022

class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        stacks_raw = []
        self.tasks = []
        reading_stacks = True
        with open(self.filename) as f:
            for line in f.readlines():
                if not line.rstrip():
                    reading_stacks = False
                    continue
                if reading_stacks:
                    stacks_raw.append([*line])
                else:
                    numbers = [int(val) for val in re.findall(r"\d+", line)]
                    movement = Movement(x=numbers[0], start = numbers[1], end = numbers[2])
                    self.tasks.append(movement)

        self.stacks = {}
        for i, val in enumerate(stacks_raw[-1]):
            if val == ' ' or val == '\n':
                continue
            val = int(val)
            self.stacks[val] = [stack[i] for stack in stacks_raw[:-1] if stack[i] != ' ']
            self.stacks[val].reverse()
        
    def solve_part_one(self):
        tasks = copy.deepcopy(self.tasks)
        stacks = copy.deepcopy(self.stacks)

        for task in tasks:
            for _ in range(task.x):
                stacks[task.end].append(stacks[task.start].pop())

        return ''.join([stack[-1] for stack in stacks.values()])

    def solve_part_two(self):
        tasks = copy.deepcopy(self.tasks)
        stacks = copy.deepcopy(self.stacks)

        for task in tasks:
            stash = deque()
            for _ in range(task.x):
                stash.appendleft(stacks[task.start].pop())
            stacks[task.end].extend(stash)

        return ''.join([stack[-1] for stack in stacks.values()])


if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.stacks)
    # print(sol.tasks)
    print(sol.solve_part_one())
    print(sol.solve_part_two())
