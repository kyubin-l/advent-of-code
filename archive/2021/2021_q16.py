from base_solution import BaseSolution

Q_NUM = 16
YEAR = 2021


class Solution(BaseSolution):
    """
    Steps:
        1. Convert hexadecimal -> binary
        2. Decode:
            - First 3 bit: version
            - Next 3 bits: type ID
                - Type ID 4: Literal value
                - Any other one: operator
            - Subpacket can have many subpackets
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        with open(self.filename) as f:
            pattern = f.readline()
        self.bin = str(bin(int(pattern, 16)))
        self.bin = self.bin[2:]

    def solve_part_one(self):
        def literal_value(pattern: str):
            """
            Pattern: string after the first 6 chars
            """
            val = 0
            while True:
                s = pattern[:5]
                val += int(s[1:], 2)
                if s[0] == "0":
                    break
                pattern = pattern[5:]
            return val, pattern

        def sub_packet(pattern: str):
            """
            Pattern: string after first 6 chars
            """
            type_id = pattern[0]

            if type_id == "1":
                total_length = int(pattern[1:16], 2)
                pattern = pattern[16:]
            else:
                num_subpackets = int(pattern[1:12], 2)
                oattern = pattern[12:]

            pattern = pattern[1:]

            return

        i = 0
        while True:
            pass

        pass

    def solve_part_two(self):
        pass


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.bin)
