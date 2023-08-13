from base_solution import BaseSolution

Q_NUM = 2
YEAR = 2021


class Solution(BaseSolution):
    """
    down x INCREASES depth
    up x DECREASES depth
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.commands = []

    def load(self):
        with open(self.filename, "r") as f:
            for line in f.readlines():
                command, value = line.rstrip().split()
                self.commands.append((command, int(value)))

    def solve(self):
        self.depth = 0
        self.hor = 0
        for command in self.commands:
            self.execute_command(command)
        return self.depth * self.hor

    def solve_part_two(self):
        self.depth = 0
        self.hor = 0
        self.aim = 0
        for command in self.commands:
            self.execute_command_2(command)
        return self.depth * self.hor

    def execute_command(self, command):
        """
        Receives command as a tuple (command: str, val: int)
        """
        com, val = command[0], command[1]
        if com == "forward":
            self.hor += val
        elif com == "down":
            self.depth += val
        elif com == "up":
            self.depth -= val
        else:
            print("Invalid command")

    def execute_command_2(self, command):
        """
        Receives command as a tuple (command: str, val: int)
        """
        com, val = command[0], command[1]
        if com == "forward":
            self.hor += val
            self.depth += self.aim * val
        elif com == "down":
            self.aim += val
        elif com == "up":
            self.aim -= val
        else:
            print("Invalid command")


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve())
    print(sol.solve_part_two())
