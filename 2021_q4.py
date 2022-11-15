from utils.base_solution import BaseSolution

Q_NUM = 4
YEAR = 2021


class Board:
    def __init__(self, board):
        self.board = board
        self.row_score = [0 for _ in range(5)]
        self.col_score = [0 for _ in range(5)]
        self.won = False

    def check_number(self, picked):
        for rownum, row in enumerate(self.board):
            for colnum, num in enumerate(row):
                if num != picked:
                    continue
                self.row_score[rownum] += 1
                self.col_score[colnum] += 1
                self.board[rownum][colnum] = None

    def check_win(self):
        return (5 in self.row_score) or (5 in self.col_score)

    def calc_score(self, val):
        num_total = 0
        for row in self.board:
            num_total += sum(num for num in row if num)
        return num_total * val


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.boards = []

    def load(self):
        with open(self.filename) as f:
            line = f.readline()
            self.nums = list(map(int, line.split(',')))
            f.readline()
            board = []
            for line in f.readlines():
                line = line.rstrip()
                if not line:
                    self.boards.append(Board(board))
                    board = []
                    continue
                board.append(list(map(int, line.split())))

    def solve_part_one(self):
        for random_num in self.nums:
            for board in self.boards:
                board.check_number(random_num)
                if board.check_win():
                    return board.calc_score(random_num)

    def solve_part_two(self):
        last_won = None
        last_val = None
        for random_num in self.nums:
            for board in self.boards:
                if board.won == True:
                    continue
                board.check_number(random_num)
                if board.check_win():
                    board.won = True
                    last_won = board
                    last_val = random_num
        return last_won.calc_score(last_val)
        

if __name__ == '__main__':
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    print(sol.solve_part_one())
    print(sol.solve_part_two())