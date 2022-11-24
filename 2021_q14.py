from utils.base_solution import BaseSolution
import string

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
        counts = {
            letter: 0 
            for letter in string.ascii_uppercase
        }
        def step_pair(pair, n):
            if pair not in self.insertions:
                return
            pattern = self.insertions[pair]
            
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
            
            for _ in range(n-1):
                pattern = step(pattern)
                
            for let in pattern:
                counts[let] += 1
                
        for i in range(len(poly)-1):
            step_pair(poly[i:i+2], step_count)
            
        print(counts)
                    

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    # print(sol.solve_part_one(40))
    print(sol.solve_part_two(40))