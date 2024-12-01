from pathlib import Path

DIR = Path(__file__).parent


class BaseSolution:
    def __init__(self, q_num: int, test: bool = False) -> None:
        self.q_num = q_num
        if not test:
            self.filename = DIR.parent / "python" / "inputs" / f"q{q_num}.txt"
        else:
            self.filename = DIR.parent / "python" / "inputs" / f"q{q_num}_sample.txt"
