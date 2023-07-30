from utils.base_solution import BaseSolution
import string
from collections import defaultdict
from tqdm import tqdm

from functools import lru_cache

Q_NUM = 14
YEAR = 2021


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.insertions = {}
        with open(self.filename) as f:
            self.starting_string = f.readline().rstrip()
            f.readline()
            for line in f.readlines():
                line = line.rstrip()
                orig, insert = line.split(" -> ")
                replace = orig[0] + insert + orig[1]
                self.insertions[orig] = replace

    def solve_part_one(self, step_count):
        poly = self.starting_string

        def most_frequent(l):
            ch = max(set(l), key=l.count)
            return l.count(ch)

        def least_frequent(l):
            ch = min(set(l), key=l.count)
            return l.count(ch)

        def step(input_string):
            n = len(input_string)
            new_string = ""
            for i in range(n - 1):
                elem = input_string[i : i + 2]
                if elem in self.insertions:
                    if not new_string:
                        new_string = self.insertions[elem]
                        continue
                    new_string = new_string[:-1] + self.insertions[elem]
            return new_string

        for _ in range(step_count):
            poly = step(poly)

        return most_frequent(poly) - least_frequent(poly)
        # return poly

    def solve_part_two(self, step_count):
        """
        Find out how much each pair will grow in n number of steps
        Keep track of additional letters generated in dictionary.
        """
        sol.load()
        poly = self.starting_string
        pairs = self.insertions

        def add_dicts(
            d1: defaultdict, d2: defaultdict, d3: defaultdict = defaultdict(int)
        ):
            for key in d2.keys():
                d1[key] += d2[key]
            for key in d3.keys():
                d1[key] += d3[key]
            return d1

        @lru_cache(maxsize=None)
        def mutate(pat: str, n: int):
            """
            Gives how many extra letters a pair of letters generates, in n
            number of steps
            e.g. if AB -> ACB, mutate('AB', 1) returns {'C': 1}
            """
            d = defaultdict(int)

            if pat not in pairs:
                return d

            mut = pairs[pat]
            let = mut[1]
            d[let] += 1

            if n == 1:
                return d

            return add_dicts(d, mutate(mut[:2], n - 1), mutate(mut[1:], n - 1))

        total = defaultdict(int)
        for let in poly:
            total[let] += 1

        for i in range(len(poly) - 1):
            pat = poly[i : i + 2]
            res = mutate(pat, step_count)
            total = add_dicts(total, res)

        return max(total.values()) - min(total.values())


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    # print(sol.solve_part_one(10))
    print(sol.solve_part_two(40))
