from typing import Any
import re

from base_solution import BaseSolution


class Solution(BaseSolution):
    def load(self) -> list[str]:
        vals = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip()
                vals.append(line)
        return vals

    def get_num(self, line: str) -> int:
        nums = re.findall(r"[\d]+", line)
        print(nums)
        return nums[0][0] + nums[-1][-1]

    def part_one(self) -> int:
        input = self.load()
        sol = 0
        for line in input:
            num = self.get_num(line)
            print(line, num)
            sol += int(num)
        return sol
    
    def get_num_from_word(self, line: str) -> int:
        nums = re.findall(self.pattern, line)
        print(nums)

    def part_two(self) -> int:
        letters = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
        self.pattern = "|".join(letters)
        input = self.load()
        for line in input:
            num = self.get_num_from_word(line)


if __name__ == "__main__":
    sol = Solution(1)
    # print(sol.part_one())
    print(sol.part_two())

