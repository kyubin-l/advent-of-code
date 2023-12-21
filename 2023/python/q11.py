from base_solution import BaseSolution


class Solution(BaseSolution):
    def load(self) -> list[str]:
        with open(self.filename) as f:
            strings = f.readlines()
        return strings

    def part_one(self) -> int:
        ...

    def part_two(self) -> int:
        ...


if __name__ == "__main__":
    test_sol = Solution(11, test=True)
    sol = Solution(11, test=False)

    assert test_sol.part_one() == 0
    print(sol.part_one())

    assert test_sol.part_two() == 0
    print(sol.part_two())
