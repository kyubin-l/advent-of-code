from base_solution import BaseSolution

Q_NUM = 2
YEAR = 2022


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matching = {"A": "X", "B": "Y", "C": "Z"}
        self.points = {"X": 1, "Y": 2, "Z": 3}
        # X: Z -> X wins Z
        self.wins = {"X": "Z", "Y": "X", "Z": "Y"}
        # X : Y: X losses to Y
        self.losses = {"X": "Y", "Y": "Z", "Z": "X"}

    def load(self):
        self.games = []
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.strip()
                p1, p2 = line.split()
                self.games.append((self.matching[p1], p2))

    def solve_part_one(self):
        games = self.games

        total_points = 0
        for game in games:
            p1, p2 = game
            total_points += self.points[p2]
            if p1 == p2:
                total_points += 3
                continue
            if self.wins[p2] == p1:
                total_points += 6

        return total_points

    def solve_part_two(self):
        """
        X: lose, Y: draw, Z: win
        """
        games = self.games
        total_points = 0

        for game in games:
            p1, p2 = game
            if p2 == "X":
                p2_new = self.wins[p1]
            elif p2 == "Y":
                p2_new = p1
                total_points += 3
            elif p2 == "Z":
                p2_new = self.losses[p1]
                total_points += 6
            total_points += self.points[p2_new]

        return total_points


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())
