from utils.base_solution import BaseSolution

Q_NUM = 3
YEAR = 2021


def bin_to_dec(bin):
    '''
    converts binary to decimal, bin: str
    '''
    dec = 0
    n = len(bin)
    for i in range(n):
        dec += int(bin[i])*2**(n-i-1)
    return dec


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nums = []

    def load(self):
        with open(self.filename, 'r') as f:
            for line in f.readlines():
                val = line.rstrip()
                digits = list(map(int, [*val]))
                self.nums.append(digits)
    
    def solve(self):
        digit_sum = []
        for digit in range(len(self.nums[0])):
            digit_sum.append(sum(num[digit] for num in self.nums))
        gamma_list = ['1' if val > len(self.nums)//2 else '0' for val in digit_sum]
        epsilon_list = ['1' if val <= len(self.nums)//2 else '0' for val in digit_sum]

        gamma = ''.join(gamma_list)
        epsilon = ''.join(epsilon_list)

        power_consumption = bin_to_dec(gamma) * bin_to_dec(epsilon)
        return gamma, epsilon, power_consumption



sol = Solution(Q_NUM, YEAR)
sol.load()
print(sol.solve())
