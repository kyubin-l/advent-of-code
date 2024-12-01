from copy import deepcopy
from dataclasses import dataclass
import re
from typing import Iterator
from functools import cache

from base_solution import BaseSolution


@dataclass
class Pattern:
    pattern: str
    groups: list[int]


class Solution(BaseSolution):
    def load(self) -> list[Pattern]:
        res: list[Pattern] = []
        with open(self.filename) as f:
            for line in f.readlines():
                pattern, groups = line.strip().split()
                groups = [int(num) for num in groups.split(",")]
                # pattern = re.sub("\.+", ".", pattern)
                res.append(Pattern(pattern=pattern, groups=groups))
        return res

    def check_match(self, pattern: str, groups: list[int]) -> bool:
        pattern_grouped = re.findall(r"[#]+", pattern)
        groups_from_pattern = [len(g) for g in pattern_grouped]
        return groups == groups_from_pattern

    def pattern_iterator(self, pattern: str, max: int) -> Iterator[str]:
        unknowns = [i for i, c in enumerate(pattern) if c == "?"]
        num_bits = len(unknowns)
        num_combinations = 2 ** (num_bits)
        for i in range(num_combinations):
            current_pattern = pattern
            bits = [(i >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]
            if sum(bits) > max:
                continue
            for replace, replace_index in zip(bits, unknowns):
                if replace == 0:
                    continue
                current_pattern = (
                    current_pattern[:replace_index]
                    + "#"
                    + current_pattern[replace_index + 1 :]
                )
            yield current_pattern

    def part_one_old(self) -> int:
        res = self.load()
        # Brute force it, slow but works
        total = 0
        for pattern in res:
            current_interator = self.pattern_iterator(
                pattern.pattern, max=sum(pattern.groups)
            )
            for p in current_interator:
                if self.check_match(p, pattern.groups):
                    total += 1
        return total

    @cache
    def get_num_matches(self, pattern: str, groups: tuple[int]) -> int:
        if not groups:
            if "#" in pattern:
                return 0
            else:
                return 1
        if not pattern:
            return 0
        # Need to somehow make sure the remainder fits in the leftover pattern
        groups = deepcopy(groups)
        cur = groups[0]
        groups = groups[1:]
        # cur = groups.pop(0)

        tot = 0
        for i in range(len(pattern)):
            patt = pattern[i : i + cur]
            if len(patt) != cur:
                break
            if "." not in patt:
                if ((i == 0) or (pattern[i - 1] in [".", "?"])) and (
                    (i + cur) == len(pattern) or (pattern[i + cur] in [".", "?"])
                ):
                    if "#" in pattern[:i]:
                        break
                    new_pattern = pattern[i + cur + 1 :]
                    # print(pattern, new_pattern, cur, groups)
                    tot += self.get_num_matches(new_pattern, groups)
        return tot

    def part_one(self) -> int:
        res = self.load()
        # res = [Pattern(pattern='??#.#???#?', groups=[2, 1, 1])]
        total = 0
        for pattern in res:
            matches = self.get_num_matches(pattern.pattern, tuple(pattern.groups))
            total += matches

            # this_match = 0

            # current_interator = self.pattern_iterator(
            #     pattern.pattern, max=sum(pattern.groups)
            # )
            # for p in current_interator:
            #     if self.check_match(p, pattern.groups):
            #         this_match += 1

            # if matches != this_match:
            #     print(matches, this_match, pattern)

        return total

    def part_two(self) -> int:
        patterns = self.load()
        new_patterns: list[Pattern] = []

        for p in patterns:
            new_pattern = "?".join([p.pattern] * 5)
            new_groups = p.groups * 5
            new_patterns.append(Pattern(pattern=new_pattern, groups=new_groups))

        total = 0
        for pattern in new_patterns:
            matches = self.get_num_matches(pattern.pattern, tuple(pattern.groups))
            total += matches
        return total


if __name__ == "__main__":
    test_sol = Solution(12, test=True)
    sol = Solution(12, test=False)

    assert test_sol.part_one() == 21
    print(sol.part_one())

    assert test_sol.part_two() == 525152
    print(sol.part_two())
