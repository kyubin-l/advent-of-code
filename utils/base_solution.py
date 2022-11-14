from abc import ABC, abstractmethod
import os

class BaseSolution(ABC):
    def __init__(self, q_num):
        self.q_num = q_num
        self.filename = os.path.join(os.getcwd(), 'inputs', f'{q_num}.txt')

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def solve(self):
        pass