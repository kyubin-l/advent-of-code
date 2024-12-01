from abc import ABC, abstractmethod
from pathlib import Path

DIR = Path(__file__).parent


class BaseSolution(ABC):
    def __init__(self, q_num, year):
        self.q_num = q_num
        self.filename = DIR.parent / "inputs" / f"{year}_q{q_num}.txt"

    @abstractmethod
    def load(self):
        pass

    # @abstractmethod
    # def solve(self):
    #     pass
