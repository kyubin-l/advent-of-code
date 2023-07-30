from utils.base_solution import BaseSolution

Q_NUM = 8
YEAR = 2021


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        self.data = []
        with open(self.filename) as f:
            for line in f.readlines():
                pattern, output = line.strip().split("|")
                pattern = pattern.split()
                output = output.split()
                self.data.append([pattern, output])

    def solve_part_one(self):
        num = 0
        for entry in self.data:
            for output in entry[1]:
                if len(output) in [2, 3, 4, 7]:
                    num += 1
        return num

    def solve_part_two(self):
        """
        Number: length of string (1, 4, 7, 8) are unique, can be deduced automatically
        0: 6            5: 5
        1: 2            6: 6
        2: 5            7: 3
        3: 5            8: 7
        4: 4            9: 6

        All 10 inputs in the beginning are unique
        if length is 5, and contains 7, must be a 3
        if length if 6, and contains a 3, must be 9
        from the other two length 6s, if it contains a 7, must be a 0
        The last length 6 is a 6

        if length is 5 and contained within 6, must be 5
        the last length 5 one will be a 2

        """

        def sort_string(s: str) -> str:
            return "".join(sorted(s))

        def issubstring(s1: str, s2: str) -> bool:
            if set([*s1]).issubset(set([*s2])):
                return True
            return False

        sorted_data = []
        # Sort strings alphabetically
        for entry in self.data:
            entry_sorted = list(map(sort_string, entry[0]))
            output_sorted = list(map(sort_string, entry[1]))
            sorted_data.append([entry_sorted, output_sorted])

        total = 0

        for entry in sorted_data:
            mapping = {}
            # if the input is sorted by length, lengths would be
            # l = [2, 3, 4, 5, 5, 5, 6, 6, 6, 7]
            pattern, output = entry[0], entry[1]
            l = sorted(pattern, key=len)

            mapping[1] = l[0]
            mapping[7] = l[1]
            mapping[4] = l[2]
            mapping[8] = l[9]

            len5 = l[3:6]
            len6 = l[6:9]

            for val in len5:
                if issubstring(mapping[7], val):
                    mapping[3] = val
                    len5.remove(val)
                    break

            for val in len6:
                if issubstring(mapping[3], val):
                    mapping[9] = val
                    len6.remove(val)
                    break

            v1, v2 = len6[0], len6[1]

            if issubstring(mapping[7], v1):
                mapping[0] = v1
                mapping[6] = v2
            else:
                mapping[0] = v2
                mapping[6] = v1

            v1, v2 = len5[0], len5[1]

            if issubstring(v1, mapping[6]):
                mapping[5] = v1
                mapping[2] = v2
            else:
                mapping[5] = v2
                mapping[2] = v1

            s = ""

            for out in output:
                for key, val in mapping.items():
                    if val == out:
                        s += str(key)

            total += int(s)

        return total


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()

    print(sol.solve_part_one())
    print(sol.solve_part_two())
