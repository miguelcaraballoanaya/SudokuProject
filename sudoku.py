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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if main_screen == True:

                    if 100 <= x <= 230 and 450 <= y <= 515:
                        board = SudokuBoard.Board(720, 720, screen, "EASY")
                        screen.fill(bg_color)
                        board.draw()

                        difficulty_font = pygame.font.Font(None, 35)
                        difficulty_surface = difficulty_font.render("Difficulty: Easy", 0, (0, 0, 0))
                        difficulty_rect = difficulty_surface.get_rect(center=(400, 30))
                        screen.blit(difficulty_surface, difficulty_rect)

                        removed = 30
                        #sudoku_generator.generate_sudoku(9, removed)
                        #calling this function in any of the 3 difficulties freezes the program for some reason.

                        game_option_buttons()

                        main_screen = False

                    elif 295 <= x <= 425 and 450 <= y <= 515:
                        board = SudokuBoard.Board(720, 720, screen, "MEDIUM")
                        screen.fill(bg_color)
                        board.draw()

                        difficulty_font = pygame.font.Font(None, 35)
                        difficulty_surface = difficulty_font.render("Difficulty: Medium", 0, (0, 0, 0))
                        difficulty_rect = difficulty_surface.get_rect(center=(400, 30))
                        screen.blit(difficulty_surface, difficulty_rect)

                        removed = 40
                        #sudoku_solution = sudoku_generator.generate_sudoku(9, removed)
                        #print(sudoku_solution)  #this is a temporary check

                        game_option_buttons()

                        main_screen = False

                    elif 490 <= x <= 620 and 450 <= y <= 515:
                        board = SudokuBoard.Board(720, 720, screen, "HARD")
                        screen.fill(bg_color)
                        board.draw()

                        difficulty_font = pygame.font.Font(None, 35)
                        difficulty_surface = difficulty_font.render("Difficulty: Hard", 0, (0, 0, 0))
                        difficulty_rect = difficulty_surface.get_rect(center=(400, 30))
                        screen.blit(difficulty_surface, difficulty_rect)

                        removed = 50
                        #sudoku_generator.generate_sudoku(9, removed)

                        game_option_buttons()

                        main_screen = False
                    break  #added this because the execution was getting stuck in this conditional

                elif main_screen == False:
                    click = board.click(x, y)

                    if 135 <= x <= 265 and 730 <= y <= 795:
                        print("BUTTON 1 WORKS")  #this is a temporary check to make sure click detection works
                        pass

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
                        col, row = click
                        board.select(row, col)
                        selected_cell = sudoku_generator.Cell(5, row, col, screen)  #5 is a placeholder value
                        selected_cell.draw()  #this is not functioning properly







        pygame.display.update()

if __name__ == "__main__":
    main()
