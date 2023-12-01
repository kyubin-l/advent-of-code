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

    def _get_num(self, line: str) -> int:
        nums = re.findall(r"[\d]+", line)
        return int(nums[0][0] + nums[-1][-1])

    def part_one(self) -> int:
        input = self.load()
        sol = 0
        for line in input:
            num = self._get_num(line)
            sol += num
        return sol

    def _get_num_part_two(self, line: str) -> int:
        nums = re.findall(self.pattern, line)
        first_digit = self.letters.get(nums[0], nums[0][0])
        second_digit = self.letters.get(nums[-1], nums[-1][-1])
        return int(first_digit + second_digit)

    def part_two(self) -> int:
        self.letters = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        input = self.load()
        sum = 0
        self.pattern = rf"(?=({'|'.join(self.letters.keys())}|\d+))"
        for line in input:
            num = self._get_num_part_two(line)
            sum += num
        return sum


if __name__ == "__main__":
    sol = Solution(1)
    print(sol.part_one())
    print(sol.part_two())
