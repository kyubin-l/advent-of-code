from utils.base_solution import BaseSolution
import math

Q_NUM = 6
YEAR = 2021


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def load(self):
        self.days = [0 for _ in range(9)]
        with open(self.filename) as f:
            raw_data = f.readline().rstrip().split(',')
            vals = list(map(int, raw_data))  
        for val in vals:
            self.days[val] += 1      

    def solve_part_one(self, days):
        """
        After each day:
            - 0 spawns a new fish with value 8
            - Every other value decreases by 1
        Note: simple list comprehension too slow, modified to use dictionaries
        
        Thought (was overcomplicating, forget):
        Considering just the ones with count 1, total 168
        After day 1: nothing
        After day 2: 168 with count 8, 168 with count 6
        After day 6: 168 with count 8, 168 with count 2, 168 with count 6
        After day 8: 168 with count 8, 168 with count 6, 168 with count 6, 168 with count 4
        ...

        after n days:
        initial batch produces
        ((n-orig_days)//6)*orig_num
        2nd batch produces (spawned after orig_days):
        ((n-orig_days-2)//6)*orig_num
        3rd batch produces (spawned after orig_days + 8)
        ((n-()))
        """
        rep = self.days.pop(0)
        while days > 0:
            self.days[6] += rep
            self.days.append(rep)
            days -= 1
            if days:
                # Don't need to pop if it's the last day, keep
                rep = self.days.pop(0)

        return sum(self.days)
                    
    def solve_part_two(self, days):
        self.load()
        return self.solve_part_one(days)


if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one(80))
    print(sol.solve_part_two(256))

