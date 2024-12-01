import re
import math

from base_solution import BaseSolution


class Solution(BaseSolution):
    def load(self) -> tuple[list[int], list[int]]:
        with open(self.filename) as f:
            _times = re.findall(r"[\d]+", f.readline())
            times = [int(time) for time in _times]
            _distances = re.findall(r"[\d]+", f.readline())
            distances = [int(distance) for distance in _distances]
        return times, distances

    def part_one(self) -> int:
        times, distances = self.load()
        res = 1
        for t, d in zip(times, distances):
            count = 0
            for time_waited in range(t + 1):
                distance_travelled = (t - time_waited) * time_waited
                if distance_travelled > d:
                    count += 1
            res *= count
        return res

    def part_two(self) -> int:
        """
        Brute force method is too slow.
        If we say the total time is T, and the time waited is t,
        the total distance travelled is
        x = (T - t) * t

        we need this to be greater than a certain distance d,
        meaning we have to solve a quadratic formula for t,
        where
        (T - t) * t > d
        T * t - t ^ 2 > d
        0 > t^2 - T * t + d

        the quadratic formula for this is

        t1, t2 = (T +- sqrt(T ^ 2 - 4d)) / 2

        Where any times between t1 and t2 will give a value greater than d
        """
        times, distances = self.load()
        time = int("".join(str(t) for t in times))
        distance = int("".join(str(d) for d in distances))

        t1 = (time - math.sqrt(time**2 - 4 * distance)) / 2
        t2 = (time + math.sqrt(time**2 - 4 * distance)) / 2

        # For whole numbers, we round t1 up and t2 down

        t1 = math.ceil(t1)
        t2 = math.floor(t2)

        # Inclusive t1 and t2, so add 1
        return t2 - t1 + 1


if __name__ == "__main__":
    test_sol = Solution(6, test=True)

    assert test_sol.part_one() == 288
    assert test_sol.part_two() == 71503

    sol = Solution(6, test=False)
    print(sol.part_one())
    print(sol.part_two())
