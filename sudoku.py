import copy

import sudoku_generator
import SudokuBoard
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sudoku")
bg_color = (255, 255, 255)
screen.fill(bg_color)

def main_menu():
    welcome_font = pygame.font.Font(None, 85)
    mode_font = pygame.font.Font(None, 55)
    difficulty_font = pygame.font.Font(None, 35)

    welcome_surface = welcome_font.render("Welcome to Sudoku!", 0, (0, 0, 0))
    welcome_rect = welcome_surface.get_rect(center=(800 // 2, 800 // 5))
    screen.blit(welcome_surface, welcome_rect)

    mode_surface = mode_font.render("Select Difficulty:", 0, (0, 0, 0))
    mode_rect = mode_surface.get_rect(center=(800 // 2, 800 // 5 * 2.5))
    screen.blit(mode_surface, mode_rect)

    pygame.draw.rect(screen, (0, 0, 153), pygame.Rect(135, 470, 130, 65), 4)
    pygame.draw.rect(screen, (153, 204, 255), pygame.Rect(145, 480, 110, 45))

    pygame.draw.rect(screen, (0, 0, 153), pygame.Rect(335, 470, 130, 65), 4)
    pygame.draw.rect(screen, (153, 204, 255), pygame.Rect(345, 480, 110, 45))

    pygame.draw.rect(screen, (0, 0, 153), pygame.Rect(535, 470, 130, 65), 4)
    pygame.draw.rect(screen, (153, 204, 255), pygame.Rect(545, 480, 110, 45))

    easy_surf = difficulty_font.render("EASY", 0, (0, 0, 0))
    easy_rect = easy_surf.get_rect(center=(200, 500))
    screen.blit(easy_surf, easy_rect)

    medium_surf = difficulty_font.render("MEDIUM", 0, (0, 0, 0))
    medium_rect = medium_surf.get_rect(center=(400, 500))
    screen.blit(medium_surf, medium_rect)

    hard_surf = difficulty_font.render("HARD", 0, (0, 0, 0))
    hard_rect = hard_surf.get_rect(center=(600, 500))
    screen.blit(hard_surf, hard_rect)

def game_option_buttons():
    option_font = pygame.font.Font(None, 35)

    pygame.draw.rect(screen, (0, 0, 153), pygame.Rect(135, 730, 130, 65), 4)
    pygame.draw.rect(screen, (153, 204, 255), pygame.Rect(145, 740, 110, 45))

    pygame.draw.rect(screen, (0, 0, 153), pygame.Rect(335, 730, 130, 65), 4)
    pygame.draw.rect(screen, (153, 204, 255), pygame.Rect(345, 740, 110, 45))

    pygame.draw.rect(screen, (0, 0, 153), pygame.Rect(535, 730, 130, 65), 4)
    pygame.draw.rect(screen, (153, 204, 255), pygame.Rect(545, 740, 110, 45))

    reset_surf = option_font.render("RESET", 0, (0, 0, 0))
    reset_rect = reset_surf.get_rect(center=(200, 760))
    screen.blit(reset_surf, reset_rect)

    restart_surf = option_font.render("RESTART", 0, (0, 0, 0))
    restart_rect = restart_surf.get_rect(center=(400, 760))
    screen.blit(restart_surf, restart_rect)

    exit_surf = option_font.render("EXIT", 0, (0, 0, 0))
    exit_rect = exit_surf.get_rect(center=(600, 760))
    screen.blit(exit_surf, exit_rect)


def main():

    main_menu()
    main_screen = True
    game_end = False
    win = False

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if main_screen == True:

                    if 135 <= x <= 265 and 470 <= y <= 535:
                        board = SudokuBoard.Board(720, 720, screen, "EASY")
                        screen.fill(bg_color)
                        board.draw()

                        difficulty_font = pygame.font.Font(None, 35)
                        difficulty_surface = difficulty_font.render("Difficulty: Easy", 0, (0, 0, 0))
                        difficulty_rect = difficulty_surface.get_rect(center=(400, 30))
                        screen.blit(difficulty_surface, difficulty_rect)

                        removed = 30

                        sudoku_board, sudoku_solution = sudoku_generator.generate_sudoku(9, removed)
                        sudoku_board_initial = copy.deepcopy(sudoku_board)


                        row_index = 1
                        cells_list = []
                        for i in sudoku_board:
                            col_index = 1
                            for j in i:
                                cell = sudoku_generator.Cell(j, row_index, col_index, screen)
                                cell.draw()
                                if cell.value != 0:
                                    cell.changeable = False
                                cells_list.append(cell)
                                col_index += 1
                            row_index += 1

                        game_option_buttons()

                        main_screen = False

                    elif 335 <= x <= 465 and 470 <= y <= 535:
                        board = SudokuBoard.Board(720, 720, screen, "MEDIUM")
                        screen.fill(bg_color)
                        board.draw()

                        difficulty_font = pygame.font.Font(None, 35)
                        difficulty_surface = difficulty_font.render("Difficulty: Medium", 0, (0, 0, 0))
                        difficulty_rect = difficulty_surface.get_rect(center=(400, 30))
                        screen.blit(difficulty_surface, difficulty_rect)

                        removed = 40

                        sudoku_board, sudoku_solution = sudoku_generator.generate_sudoku(9, removed)
                        sudoku_board_initial = copy.deepcopy(sudoku_board)

                        row_index = 1
                        cells_list = []
                        for i in sudoku_board:
                            col_index = 1
                            for j in i:
                                cell = sudoku_generator.Cell(j, row_index, col_index, screen)
                                cell.draw()
                                if cell.value != 0:
                                    cell.changeable = False
                                cells_list.append(cell)
                                col_index += 1
                            row_index += 1

                        # print(sudoku_board)  #this is a temporary check
                        # print(sudoku_solution)  #this is a temporary check

                        game_option_buttons()

                        main_screen = False

                    elif 535 <= x <= 665 and 470 <= y <= 535:
                        board = SudokuBoard.Board(720, 720, screen, "HARD")
                        screen.fill(bg_color)
                        board.draw()

                        difficulty_font = pygame.font.Font(None, 35)
                        difficulty_surface = difficulty_font.render("Difficulty: Hard", 0, (0, 0, 0))
                        difficulty_rect = difficulty_surface.get_rect(center=(400, 30))
                        screen.blit(difficulty_surface, difficulty_rect)

                        removed = 50

                        sudoku_board, sudoku_solution = sudoku_generator.generate_sudoku(9, removed)
                        sudoku_board_initial = copy.deepcopy(sudoku_board)


                        row_index = 1
                        cells_list = []
                        for i in sudoku_board:
                            col_index = 1
                            for j in i:
                                cell = sudoku_generator.Cell(j, row_index, col_index, screen)
                                cell.draw()
                                if cell.value != 0:
                                    cell.changeable = False
                                cells_list.append(cell)
                                col_index += 1
                            row_index += 1

                        # print(sudoku_board)  # this is a temporary check
                        # print(sudoku_solution)  # this is a temporary check

                        game_option_buttons()

                        main_screen = False
                    break  #added this because the execution was getting stuck in this conditional

                elif main_screen == False:
                    if not any(0 in sublist for sublist in sudoku_board):
                        if sudoku_board == sudoku_solution:
                            game_end = True
                            win = True
                        else:
                            game_end = True
                    click = board.click(x, y)

                    if 135 <= x <= 265 and 730 <= y <= 795:
                        print("BUTTON 1 WORKS")  #this is a temporary check to make sure click detection works
                        screen.fill(bg_color)
                        board.draw()
                        screen.blit(difficulty_surface, difficulty_rect)
                        game_option_buttons()

                        row_index = 1
                        cells_list = []
                        for i in sudoku_board_initial:
                            col_index = 1
                            for j in i:
                                cell = sudoku_generator.Cell(j, row_index, col_index, screen)
                                cell.draw()
                                if cell.value != 0:
                                    cell.changeable = False
                                cells_list.append(cell)
                                col_index += 1
                            row_index += 1

                        print(sudoku_board)  #these are checks
                        print(sudoku_solution)


                    elif 335 <= x <= 465 and 730 <= y <= 795:
                        screen.fill(bg_color)
                        main()
                        break

                    elif 535 <= x <= 665 and 730 <= y <= 795:
                        pygame.quit()
                        sys.exit()

                    elif click is None:  #this is true if the user clicks outside the board space
                        print("CLICK IS NONE")  #this is a temporary check to make sure click detection works

                    elif click is not None:  #this is true if the user clicks a cell
                        print("CLICK IS NOT NONE")  #this is a temporary check to make sure click detection works
                        x, y = event.pos
                        col, row = click
                        board.select(row, col)
                        row_index = row - 1
                        col_index = col - 1

                        screen.fill(bg_color)
                        board.draw()
                        screen.blit(difficulty_surface, difficulty_rect)
                        game_option_buttons()

                        for i in cells_list:
                            i.draw()

                        pygame.draw.rect(screen, (255, 0, 0), ((72+(72*(col-1))), (72+(72*(row-1))), 72, 72), 2)
                        pygame.display.update()

                        cell = cells_list[(row-1)*9 + (col-1)]

                        print(click)
                        print(row_index, "", col_index)
                        print(cell.value)

                        if cell.value == 0:
                            while True:
                                enter = False
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_1:
                                            cell.sketched_value = 1
                                            cell.draw()
                                            pygame.display.update()
                                            enter = True
                                            break
                                        elif event.key == pygame.K_2:
                                            cell.sketched_value = 2
                                            cell.draw()
                                            enter = True
                                            break
                                        elif event.key == pygame.K_3:
                                            cell.sketched_value = 3
                                            cell.draw()
                                            pygame.display.update()
                                            enter = True
                                            break
                                        elif event.key == pygame.K_4:
                                            cell.sketched_value = 4
                                            cell.draw()
                                            pygame.display.update()
                                            enter = True
                                            break
                                        elif event.key == pygame.K_5:
                                            cell.sketched_value = 5
                                            cell.draw()
                                            pygame.display.update()
                                            enter = True
                                            break
                                        elif event.key == pygame.K_6:
                                            cell.sketched_value = 6
                                            cell.draw()
                                            pygame.display.update()
                                            enter = True
                                            break
                                        elif event.key == pygame.K_7:
                                            cell.sketched_value = 7
                                            cell.draw()
                                            pygame.display.update()
                                            enter = True
                                            break
                                        elif event.key == pygame.K_8:
                                            cell.sketched_value = 8
                                            cell.draw()
                                            pygame.display.update()
                                            enter = True
                                            break
                                        elif event.key == pygame.K_9:
                                            cell.sketched_value = 9
                                            cell.draw()
                                            pygame.display.update()
                                            enter = True
                                            break
                                        if event.key == pygame.K_RETURN:
                                            cell.value = cell.sketched_value
                                            cell.sketched_value = None
                                            if cell.value is not None:
                                                cell.draw()
                                                pygame.display.update()
                                            sudoku_board[row_index][col_index] = cell.value
                                            print("Enter")
                                            print(sudoku_board)
                                            enter = True
                                            break

                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        x, y = event.pos
                                        new_click = board.click(x, y)
                                        if click != new_click:
                                            screen.fill(bg_color)
                                            board.draw()
                                            screen.blit(difficulty_surface, difficulty_rect)
                                            game_option_buttons()

                                            for i in cells_list:
                                                i.draw()

                                            enter = True
                                        else:
                                            continue
                                if enter:
                                    break

                        elif cell.value != 0:
                            print("B")
                            pass

            elif event.type == pygame.KEYDOWN and main_screen == False:

                try:
                    row, col
                except NameError:
                    row, col = 1, 1

                board.select(row, col)

                row_index = row - 1
                col_index = col - 1

                screen.fill(bg_color)
                board.draw()
                screen.blit(difficulty_surface, difficulty_rect)
                game_option_buttons()

                for i in cells_list:
                    i.draw()

                pygame.draw.rect(screen, (255, 0, 0), ((72 + (72 * (col - 1))), (72 + (72 * (row - 1))), 72, 72), 2)
                pygame.display.update()

                cell = cells_list[(row - 1) * 9 + (col - 1)]

                if event.key == pygame.K_LEFT:
                    if col == 1:
                        pass
                    else:
                        col -= 1
                        board.select(row, col)

                elif event.key == pygame.K_RIGHT:
                    if col == 9:
                        pass
                    else:
                        col += 1
                        board.select(row, col)

                elif event.key == pygame.K_UP:
                    if row == 1:
                        pass
                    else:
                        row -= 1
                        board.select(row, col)

                elif event.key == pygame.K_DOWN:
                    if row == 9:
                        pass
                    else:
                        row += 1
                        board.select(row, col)

                if cell.value == 0:
                    while True:
                        enter = False
                        for event in pygame.event.get():
                            if event.key == pygame.K_1:
                                cell.sketched_value = 1
                                cell.draw()
                                pygame.display.update()
                                enter = True
                                break
                            elif event.key == pygame.K_2:
                                cell.sketched_value = 2
                                cell.draw()
                                enter = True
                                break
                            elif event.key == pygame.K_3:
                                cell.sketched_value = 3
                                cell.draw()
                                pygame.display.update()
                                enter = True
                                break
                            elif event.key == pygame.K_4:
                                cell.sketched_value = 4
                                cell.draw()
                                pygame.display.update()
                                enter = True
                                break
                            elif event.key == pygame.K_5:
                                cell.sketched_value = 5
                                cell.draw()
                                pygame.display.update()
                                enter = True
                                break
                            elif event.key == pygame.K_6:
                                cell.sketched_value = 6
                                cell.draw()
                                pygame.display.update()
                                enter = True
                                break
                            elif event.key == pygame.K_7:
                                cell.sketched_value = 7
                                cell.draw()
                                pygame.display.update()
                                enter = True
                                break
                            elif event.key == pygame.K_8:
                                cell.sketched_value = 8
                                cell.draw()
                                pygame.display.update()
                                enter = True
                                break
                            elif event.key == pygame.K_9:
                                cell.sketched_value = 9
                                cell.draw()
                                pygame.display.update()
                                enter = True
                                break
                            if event.key == pygame.K_RETURN:
                                cell.value = cell.sketched_value
                                cell.sketched_value = None
                                if cell.value is not None:
                                    cell.draw()
                                    pygame.display.update()
                                sudoku_board[row_index][col_index] = cell.value
                                print("Enter")
                                print(sudoku_board)
                                enter = True
                                break
                            else:
                                enter = True
                                break
                        if enter:
                            pygame.draw.rect(screen, (255, 0, 0),
                                             ((72 + (72 * (col - 1))), (72 + (72 * (row - 1))), 72, 72), 2)
                            pygame.display.update()
                            break

                elif cell.value != 0:
                    print("B")
                    pass


                board.select(row, col)
                screen.fill(bg_color)
                board.draw()
                screen.blit(difficulty_surface, difficulty_rect)
                game_option_buttons()

                for i in cells_list:
                    i.draw()

                pygame.draw.rect(screen, (255, 0, 0), ((72 + (72 * (col - 1))), (72 + (72 * (row - 1))), 72, 72), 2)
                pygame.display.update()

                cell = cells_list[(row - 1) * 9 + (col - 1)]



        pygame.display.update()


if __name__ == "__main__":
    main()
