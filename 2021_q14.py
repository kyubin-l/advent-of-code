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
                orig, insert = line.split(' -> ')
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
            new_string = ''
            for i in range(n-1):
                elem = input_string[i:i+2]
                if elem in self.insertions:
                    if not new_string:
                        new_string = self.insertions[elem]
                        continue
                    new_string = new_string[:-1] + self.insertions[elem]
            return new_string

        for _ in range(step_count):
            poly = step(poly)
            
        return most_frequent(poly) - least_frequent(poly)

    def solve_part_two(self, step_count):
        """
        Find out how much each pair will grow in n number of steps
        """
        poly = self.starting_string
        sol.load()
        pairs = self.insertions

        total_letters = defaultdict(int)


        @lru_cache
        def mutate(pattern, num):
            # print(total_letters)
            if pattern not in pairs:
                return


            mutation = pairs[pattern]
            let = mutation[1]
            total_letters[let] += 1
            if num == 1:
                return

            p1, p2 = mutation[:2], mutation[1:]
            mutate(p1, num-1)
            mutate(p2, num-1)

        
        for i in tqdm(range(len(poly)-1)):
            mutate(poly[i:i+2], step_count)

        print(total_letters)



if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    # print(sol.solve_part_one(40))
    print(sol.solve_part_two(40))