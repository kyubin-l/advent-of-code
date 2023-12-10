from base_solution import BaseSolution


class Solution(BaseSolution):
    def load(self) -> list[list[int]]:
        report: list[list[int]] = []
        with open(self.filename) as f:
            for line in f.readlines():
                int_lines: list[int] = [int(l) for l in line.split()]
                report.append(int_lines)
        return report

    def extrapolate_value(self, values: list[int]) -> int:
        if all([val == 0 for val in values]):
            return 0
        new = [b - a for b, a in zip(values[1:], values[:-1])]
        return values[-1] + self.extrapolate_value(new)

    def part_one(self) -> int:
        reports = self.load()
        total = 0
        for report in reports:
            total += self.extrapolate_value(report)
        return total

    def extrapolate_value_part_two(self, values: list[int]) -> int:
        if all([val == 0 for val in values]):
            return 0
        new = [b - a for b, a in zip(values[1:], values[:-1])]
        return values[0] - self.extrapolate_value_part_two(new)

    def part_two(self) -> int:
        reports = self.load()
        total = 0
        for report in reports:
            total += self.extrapolate_value_part_two(report)
            print(self.extrapolate_value_part_two(report))
        return total


if __name__ == "__main__":
    test_sol = Solution(9, test=True)
    sol = Solution(9, test=False)

    assert test_sol.part_one() == 114
    print(sol.part_one())

    assert test_sol.part_two() == 2
    print(sol.part_two())
