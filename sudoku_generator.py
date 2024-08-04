class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.box_length = 3

    def get_board(self):
        return self.board

    def print_board(self):
        for i in self.board:
            print(i)

    def valid_in_row(self, row, num):
        for i in self.board[row]:
            if num == i:
                return False
        return True

    def valid_in_col(self, col, num):
        for j in range(9):
            if num == self.board[j][col]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(col_start, col_start + self.box_length):
            for j in range(row_start, row_start + self.box_length):
                if self.board[i][j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        pass

    def fill_box(self, row_start, col_start):
        pass

    def fill_diagonal(self):
        pass

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        pass


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
