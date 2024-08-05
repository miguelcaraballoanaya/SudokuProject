import pygame
from Cell import *
pygame.init()


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = self.cell_grid(9, 9, screen)

    def cell_grid(self, rows, col, screen):
        grid = []
        for r in range(rows):
            row = []
            for c in range(col):
                row.append(Cell(None, r, c, screen))
            grid.append(row)
        return grid

    def draw(self):
        boardsize = self.width / 10
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (boardsize + boardsize * i, boardsize),
                                 (boardsize + boardsize * i, 10*boardsize), 5)
                pygame.draw.line(self.screen, (0, 0, 0), (boardsize, boardsize + boardsize * i),
                                 (10*boardsize, boardsize + boardsize * i), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (boardsize + boardsize * i, boardsize),
                             (boardsize + boardsize * i, 10*boardsize), 2)
            pygame.draw.line(self.screen, (0, 0, 0), (boardsize, boardsize + boardsize * i),
                             (10*boardsize, boardsize + boardsize * i), 2)
        self.update_board()

    def select(self, row, col):
        # may need to change if this returns anything depending on how it's implemented
        self.cells[row][col].selected = True
        selected = self.cells[row][col].selected
        return selected

    def click(self, row, col):
        if col <= self.width and row <= self.height:
            column = int((col // (self.width / 10)))
            row = int((row // (self.height / 10)))
            self.select(row, column)
            return row, column
        return None

    def clear(self):
        # we are going to need a way to tell if these cells are filled by the user or program in the cell class
        if cell.changeable == True:
            cell.value = None

    def sketch(self, value):
        pass

    def place_number(self, value):
        cell.set_sell_value(value)

    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                if cell.changeable == True:
                    cell.value = None

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value is None:
                    return False
        return True

    def update_board(self):
        pygame.display.update()

    def find_empty(self):
        for row in self.cells:
            for cell in row:
                if cell.value is None:
                    cell_location = (cell.row, cell.col)
                    return cell_location

    def check_board(self):
        pass