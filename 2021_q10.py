from utils.base_solution import BaseSolution

Q_NUM = 10
YEAR = 2021

class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.lines = []
        with open(self.filename) as f:
            for line in f.readlines():
                self.lines.append(line.rstrip())

    def solve_part_one(self):
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>',
        }

        points = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }

        total_points = 0

        for pattern in self.lines:
            closing = []
            for sym in pattern:
                if sym in brackets.keys():
                    closing.append(brackets[sym])
                else:
                    if (not closing) or (sym != closing.pop()):
                        total_points += points[sym]
                        break    
        return total_points
        

    def solve_part_two(self):
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>',
        }

        points = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
        }

        scores = []
        for pattern in self.lines:
            invalid = False
            closing = []
            for sym in pattern:
                if sym in brackets.keys():
                    closing.append(brackets[sym])
                else:
                    if (not closing) or (sym != closing.pop()):
                        invalid = True
                        break
            if not invalid:    
                closing.reverse()
                score = 0
                for sym in closing:
                    score *= 5
                    score += points[sym]
                scores.append(score)

        scores.sort()

        return scores[len(scores)//2]
        

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())