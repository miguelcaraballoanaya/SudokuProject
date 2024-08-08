import random
import pygame

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
        for i in range(9):
            if self.board[row][i] == num:
                return False

        for j in range(9):
            if self.board[j][col] == num:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    # def fill_box(self, row_start, col_start):
    #     nums = list(range(1,10))
    #     random.shuffle(nums)
    #     index = 0
    #     for i in range(row_start, row_start + 3):
    #         for j in range(col_start, col_start + 3):
    #             if self.valid_in_box(row_start, col_start, nums[index]):
    #                 self.board[i][j] = nums[index]
    #                 index += 1
    def fill_box(self, row_start, col_start):
        integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(col_start, col_start + 3):
            for y in range(row_start, row_start + 3):
                choice = random.choice(integer_list)
                self.board[y][x] = choice
                integer_list.remove(choice)
        print(self.board)

    # def fill_diagonal(self):
    #     for i in range(0,9,3):
    #         self.fill_box(i,i)
    def fill_diagonal(self):
        self.fill_box(0,0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

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

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

# we need to label a cell as either changeable or not user-changeable, thinking this section would be the best place
    def remove_cells(self):
        num = self.removed_cells
        rem_list = []
        while len(rem_list) < num:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)

            if (row, col) not in rem_list and self.board[row][col] != 0:
                self.board[row][col] = 0
                rem_list.append((row, col))

# I think we need two copies of the board, the original and the puzzle, so we can compare for the win condition
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

def generate_sudoku_solution(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    return board


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.width = 72  #changed these because the board does not take up the whole screen
        self.height = 72
        self.selected = False
        self.changeable = True
        self.sketched_value = None

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        font = pygame.font.Font(None, 30)
        x = self.col * self.width
        y = self.row * self.height

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, self.width, self.height), 2) #red color
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, self.width, self.height), 1) #black color

        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + self.width // 2 - text.get_width() // 2, y + self.height // 2 - text.get_height() // 2))
        elif self.sketched_value != 0:
            sketched_font = pygame.font.Font(None, 20)
            sketched_text = sketched_font.render(str(self.sketched_value), True, (128, 128, 128)) #grey color
            self.screen.blit(sketched_text, (x + 5, y + 5))