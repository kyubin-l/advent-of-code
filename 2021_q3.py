from utils.base_solution import BaseSolution
import math

Q_NUM = 3
YEAR = 2021


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nums = []

    def load(self):
        with open(self.filename, "r") as f:
            for line in f.readlines():
                val = line.rstrip()
                digits = list(map(int, [*val]))
                self.nums.append(digits)

    def solve(self):
        digit_sum = []
        for digit in range(len(self.nums[0])):
            digit_sum.append(sum(num[digit] for num in self.nums))
        threshold = len(self.nums) // 2
        self.gamma_list = ["1" if val >= threshold else "0" for val in digit_sum]
        self.epsilon_list = ["1" if val < threshold else "0" for val in digit_sum]

        gamma = "".join(self.gamma_list)
        epsilon = "".join(self.epsilon_list)

        power_consumption = int(gamma, 2) * int(epsilon, 2)
        return gamma, epsilon, power_consumption

    def solve_part_two(self):
        """
        Need to calculate new threshold every digit.
        For ox:
        - Use more common digit, if equal, use 1
        For co:
        - Use less common digit, if equal, use 0
        """
        ox_rating = self.nums.copy()
        co_rating = self.nums.copy()

        for i in range(len(self.nums[0])):
            threshold = math.ceil(len(ox_rating) / 2)
            num_ones = sum(rating[i] for rating in ox_rating)
            ox_val = 1 if num_ones >= threshold else 0

            ox_rating = [value for value in ox_rating if value[i] == ox_val]

            if len(ox_rating) == 1:
                break

        for i in range(len(self.nums[0])):
            """
            Possible that all the numbers have same value in a digit:
            would remove all numbers from list
            """
            threshold = math.ceil(len(co_rating) / 2)
            num_ones = sum(rating[i] for rating in co_rating)
            co_val = 1 if num_ones < threshold else 0

            co_rating = [value for value in co_rating if value[i] == co_val]

            if len(co_rating) == 1:
                break

        ox_rating = "".join(map(str, ox_rating[0]))
        co_rating = "".join(map(str, co_rating[0]))
        life_support_rating = int(ox_rating, 2) * int(co_rating, 2)

        return ox_rating, co_rating, life_support_rating


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve())
    print(sol.solve_part_two())
