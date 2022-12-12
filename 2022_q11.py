from utils.base_solution import BaseSolution
import copy
import heapq

Q_NUM = 11
YEAR = 2022

class Monkey:
    def __init__(
        self,
        number: int,
        levels: list = None,
        operation: str = None,
        test_val: int = None,
        test_true: int = None,
        test_false: int = None
        ) -> None:

        self.number = number
        self.levels = levels
        self.operation = operation
        self.test_val = test_val
        self.test_true = test_true
        self.test_false = test_false
        self.inspected = 0
    
    def __str__(self) -> str:
        return f'number: {self.number}, levels: {self.levels}'


    @classmethod
    def get_monkey(cls, monkey_list, number):
        for monkey in monkey_list:
            if monkey.number == number:
                return monkey

    def operate(self, old):
        return eval(self.operation)

    def throw_all(self, monkey_list, part=2):
        while self.levels:
            level = self.levels.pop(0)
            if self.number != 6:
                new_level = self.operate(level)
            else:
                new_level = level
            if part == 1:
                new_level = int(new_level/3)
            if new_level % self.test_val == 0:
                monkey = self.get_monkey(monkey_list, self.test_true)
                monkey.levels.append(new_level)
            else:
                monkey = self.get_monkey(monkey_list, self.test_false)
                monkey.levels.append(new_level)
            self.inspected += 1


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.monkey_list = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith('Monkey'):
                    monkey = Monkey(number=int(line.split()[-1][0]))
                if line.startswith('Starting items'):
                    items = line.split(':')[-1].strip()
                    levels = [int(it) for it in items.split(',')]
                    monkey.levels = levels
                if line.startswith('Operation'):
                    operation = line.split('=')[-1].strip()
                    monkey.operation = operation
                if line.startswith('Test'):
                    monkey.test_val = int(line.split()[-1])
                if line.startswith('If true'):
                    test_true = int(line.split()[-1])
                    monkey.test_true = test_true
                if line.startswith('If false'):
                    test_false = int(line.split()[-1])
                    monkey.test_false = test_false
                if not line:
                    self.monkey_list.append(monkey)
        self.monkey_list.append(monkey)

    def solve_part_one(self):
        monkey_list = copy.deepcopy(self.monkey_list)

        for _ in range(20):
            for monkey in monkey_list:
                monkey.throw_all(monkey_list, part=1)
            print([monkey.inspected for monkey in monkey_list])
        
        inspected = [monkey.inspected for monkey in monkey_list]
        inspected.sort()
        print(inspected)

        return inspected[-1] * inspected[-2]
        

    def solve_part_two(self):
        """
        Main issue is the old * old slowing things down a lot.
            - Need to find new method to keep worry levels low
            - 

        
        """
        monkey_list = copy.deepcopy(self.monkey_list)

        for _ in range(10000):
            for monkey in monkey_list:
                monkey.throw_all(monkey_list, part=2)
        
        inspected = [monkey.inspected for monkey in monkey_list]
        inspected.sort()
        print(inspected)

        return inspected[-1] * inspected[-2]

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())