from pathlib import Path

def get_filename(cur_file: str) -> str:
    dir = Path(cur_file).parent / "input.txt"
    return dir.__str__()
