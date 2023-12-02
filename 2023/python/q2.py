from collections import defaultdict

from base_solution import BaseSolution


class Solution(BaseSolution):
    def load(self) -> list[str]:
        with open(self.filename) as f:
            strings = f.read().splitlines()
        return strings

    def _process_game_part_one(self, game: str, limits: dict[str, int]) -> tuple[int, bool]:
        """
        Determine if the game is possible given the limits
        Example game:
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

        returns:
            (game_id, possible): returns the game id and whether the game is possible
            given the limits
        """
        game_id, rounds = game.split(":")
        id_number = int(game_id.split()[-1])
        for round in rounds.split(";"):
            valid = self._process_round_part_one(round, limits)
            if not valid:
                return (id_number, False)
        return (id_number, True)

    def _process_round_part_one(self, round: str, limits: dict[str, int]) -> bool:
        """
        Determine if the round is possible based on limits
        Example round:
        3 blue, 4 red
        """
        cubes = round.split(",")
        for cube in cubes:
            cube = cube.strip()
            count = int(cube.split()[0])
            color = cube.split()[-1]
            if count > limits[color]:
                return False
        return True

    def part_one(self) -> int:
        games = self.load()
        game_limits = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        id_sums = 0
        for game in games:
            game_id, valid = self._process_game_part_one(game, game_limits)
            if not valid:
                continue
            id_sums += game_id
        return id_sums
    
    def _get_game_power(self, game: str) -> int:
        # Game id and different rounds are irrelevant for this part - we just
        # need to know the largest occurance of the cubes for each color
        rounds = game.split(":")[-1].strip()
        all_cubes_in_round = rounds.replace(";", ",")
        cubes: dict[str, int] = defaultdict(int)

        for cube in all_cubes_in_round.split(","):
            cube = cube.strip()
            count = int(cube.split()[0])
            color = cube.split()[-1]
            cubes[color] = max(cubes[color], count)
        power = 1
        for occurance in cubes.values():
            power *= occurance
        return power

    def part_two(self) -> int:
        games = self.load()
        powers = 0
        for game in games:
            powers += self._get_game_power(game)
        return powers


if __name__ == "__main__":
    test_sol = Solution(2, test=True)
    assert test_sol.part_one() == 8
    assert test_sol.part_two() == 2286

    sol = Solution(2, test=False)
    print(sol.part_one())
    print(sol.part_two())
