from collections import defaultdict
import re

from base_solution import BaseSolution


class Solution(BaseSolution):
    def load(self) -> list[str]:
        with open(self.filename) as f:
            strings = f.read().splitlines()
        return strings
    
    def get_winning_card_count(self, card: str) -> int:
        _, raw_numbers = card.split(":")
        nums = re.findall(r"[\d]+|\|", raw_numbers)
        split_point = nums.index("|")
        winning_numbers = set(nums[:split_point])
        elf_numbers = set(nums[split_point + 1 :])
        wins = len(winning_numbers.intersection(elf_numbers))
        return wins

    def part_one(self) -> int:
        cards = self.load()
        points = 0
        for card in cards:
            wins = self.get_winning_card_count(card)
            points += 2 ** (wins - 1) if wins > 0 else 0
        return points

    def part_two(self) -> int:
        cards = self.load()
        # Start with one card each
        card_counts: dict[int, int] = defaultdict(lambda: 1)
        for i, card in enumerate(cards, 1):
            wins = self.get_winning_card_count(card)
            num_current_card = card_counts[i]
            for c in range(i + 1, i + wins + 1):
                card_counts[c] += num_current_card
        return sum(card_counts.values())


if __name__ == "__main__":
    test_sol = Solution(4, test=True)
    assert test_sol.part_one() == 13
    assert test_sol.part_two() == 30

    sol = Solution(4, test=False)
    print(sol.part_one())
    print(sol.part_two())
