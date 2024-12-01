from base_solution import BaseSolution

Q_NUM = 7
YEAR = 2021


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        with open(self.filename) as f:
            line = f.readline()
            self.positions = list(map(int, line.split(",")))
        return super().load()

    def solve_part_one(self):
        self.positions.sort()
        l = len(self.positions)
        mid_index = l // 2
        if l & 2 == 0:
            m1, m2 = self.positions[mid_index - 1], self.positions[mid_index]
            if m1 == m2:
                m = m1
            elif (m2 - m1) & 2 == 0:
                m = (m2 + m1) // 2
            else:
                if self.positions.count(m1) > self.positions.count(m2):
                    m = (m1 + m2) // 2
                else:
                    m = (m1 + m2) // 2 + 1
        else:
            m = self.positions[mid_index]

        total = 0
        for val in self.positions:
            total += abs(val - m)

        return total

    def solve_part_two(self):
        """
        using an iterative process. Start from the middle, move towards
        the direction that uses less fuel. Moving one step away from a point will
        cost additionally the total distance.
        e.g 1 -> 5 to 1 -> 6 costs 5 additional fuel
        moving one step closer saves a fuel amount equal to the original distance

        Positive number indicates that a move towards the right saves fuel
        """

        def calc_fuel(m, pos):
            d = abs(m - pos)
            fuel = 0
            for i in range(1, d + 1):
                fuel += i
            return fuel

        m = self.positions[len(self.positions) // 2]
        r_tot = 0
        l_tot = 0
        last_move = None

        while True:
            r = m + 1
            l = m - 1

            l_tot_prev = l_tot

            r_tot = 0
            l_tot = 0

            for val in self.positions:
                if r > val:
                    r_tot -= r - val
                else:
                    r_tot += (val - r) + 1

                if val <= l:
                    l_tot += (l - val) + 1
                else:
                    l_tot -= val - l

            if (r_tot <= 0) and (l_tot <= 0):
                break

            if r_tot > 0:
                m += 1
                if last_move == "l":
                    if r_tot < l_tot_prev:
                        m -= 1
                    break
                last_move = "r"
            else:
                m -= 1
                last_move = "l"

        total = 0
        for pos in self.positions:
            total += calc_fuel(m, pos)

        return m, total


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())
