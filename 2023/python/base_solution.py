from pathlib import Path

DIR = Path(__file__).parent


class BaseSolution:
    def __init__(self, q_num: int) -> None:
        self.q_num = q_num
        self.filename = DIR.parent / "python" / "inputs" / f"q{q_num}.txt"
