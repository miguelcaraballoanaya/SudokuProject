import pygame

pygame.init()


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

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
        pass

    def click(self, row, col):
        if col <= self.width and row <= self.height:
            column = (col // (self.width / 10))
            row = (row // (self.height / 10))
            return row, column
        return None

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pygame.display.update()

    def find_empty(self):
        pass

    def check_board(self):
        pass