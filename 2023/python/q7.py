from collections import Counter
from dataclasses import dataclass
from typing import Any

from base_solution import BaseSolution

CARD_ORDER_ONE = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARD_ORDER_TWO = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def get_key_for_max_val(d: dict[Any, int]) -> Any:
    k = list(d.keys())
    v = list(d.values())
    return k[v.index(max(v))]


@dataclass
class Hand:
    hand: str
    bid: int

    def __gt__(self, other: "Hand") -> bool:
        hand_one = Counter(self.hand)
        hand_two = Counter(other.hand)
        if len(hand_one) != len(hand_two):
            # Non equal unique elements
            return len(hand_one) < len(hand_two)
        # Two pair and three of a kind, and full house and four of a kind have
        # the same number of unique
        max_occurence_hand_one = max(hand_one.values())
        max_occurence_hand_two = max(hand_two.values())
        if max_occurence_hand_one != max_occurence_hand_two:
            return max_occurence_hand_one > max_occurence_hand_two

        for first, second in zip(self.hand, other.hand):
            index_difference = CARD_ORDER_ONE.index(first) - CARD_ORDER_ONE.index(
                second
            )
            if index_difference != 0:
                return index_difference < 0
        raise ValueError("Two hands are perfectly equal!")


@dataclass
class JokerHand(Hand):
    def __gt__(self, other: Hand) -> bool:
        hand_one = Counter(self.hand)
        hand_two = Counter(other.hand)
        # If either contains jokers, can default to normal method
        if ("J" not in hand_one) and ("J" not in hand_two):
            return super().__gt__(other)
        # If there are jokers, these would turn into the card with the highest occurence
        # same check proceeds

        if "J" in hand_one:
            max_joker = hand_one.pop("J")
            if not hand_one:
                hand_one["A"] = 5
            else:
                hand_one_max = get_key_for_max_val(hand_one)
                hand_one[hand_one_max] += max_joker
        if "J" in hand_two:
            max_joker = hand_two.pop("J")
            if not hand_two:
                hand_two["A"] = 5
            else:
                hand_two_max = get_key_for_max_val(hand_two)
                hand_two[hand_two_max] += max_joker

        # From this point onewards it's the same as above
        if len(hand_one) != len(hand_two):
            # Non equal unique elements
            return len(hand_one) < len(hand_two)

        # Two pair and three of a kind, and full house and four of a kind have
        # the same number of unique.
        max_occurence_hand_one = max(hand_one.values())
        max_occurence_hand_two = max(hand_two.values())
        if max_occurence_hand_one != max_occurence_hand_two:
            return max_occurence_hand_one > max_occurence_hand_two

        for first, second in zip(self.hand, other.hand):
            index_difference = CARD_ORDER_TWO.index(first) - CARD_ORDER_TWO.index(
                second
            )
            if index_difference != 0:
                return index_difference < 0
        raise ValueError("Two hands are perfectly equal!")


class Solution(BaseSolution):
    def load(self, part: int) -> list[Hand | JokerHand]:
        output: list[Hand] = []
        with open(self.filename) as f:
            for line in f.readlines():
                hand, _bid = line.split()
                bid = int(_bid)
                if part == 1:
                    output.append(Hand(hand, bid))
                else:
                    output.append(JokerHand(hand, bid))
        return output

    def part_one(self) -> int:
        hands: list[Hand] = self.load(part=1)
        hands.sort()
        sol = 0
        for place, hand in enumerate(hands, 1):
            sol += place * hand.bid
        return sol

    def part_two(self) -> int:
        hands: list[Hand | JokerHand] = self.load(part=2)
        hands.sort()
        sol = 0
        for place, hand in enumerate(hands, 1):
            sol += place * hand.bid
        return sol


if __name__ == "__main__":
    test_sol = Solution(7, test=True)
    sol = Solution(7, test=False)

    assert test_sol.part_one() == 6440
    print(sol.part_one())

    assert test_sol.part_two() == 5905
    print(sol.part_two())
