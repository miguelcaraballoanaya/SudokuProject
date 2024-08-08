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


def main():

    main_menu()
    main_screen = True
    game_end = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and main_screen == True:
                x, y = event.pos

                if 100 <= x <= 230 and 450 <= y <= 515:
                    board = SudokuBoard.Board(720, 720, screen, "EASY")
                    screen.fill(bg_color)
                    board.draw()

                    difficulty_font = pygame.font.Font(None, 35)
                    difficulty_surface = difficulty_font.render("Difficulty: Easy", 0, (0, 0, 0))
                    difficulty_rect = difficulty_surface.get_rect(center=(400, 30))
                    screen.blit(difficulty_surface, difficulty_rect)

                    main_screen = False

                elif 295 <= x <= 425 and 450 <= y <= 515:
                    board = SudokuBoard.Board(720, 720, screen, "MEDIUM")
                    screen.fill(bg_color)
                    board.draw()

                    difficulty_font = pygame.font.Font(None, 35)
                    difficulty_surface = difficulty_font.render("Difficulty: Medium", 0, (0, 0, 0))
                    difficulty_rect = difficulty_surface.get_rect(center=(400, 30))
                    screen.blit(difficulty_surface, difficulty_rect)

                    main_screen = False

                elif 490 <= x <= 620 and 450 <= y <= 515:
                    board = SudokuBoard.Board(720, 720, screen, "HARD")
                    screen.fill(bg_color)
                    board.draw()

                    difficulty_font = pygame.font.Font(None, 35)
                    difficulty_surface = difficulty_font.render("Difficulty: Hard", 0, (0, 0, 0))
                    difficulty_rect = difficulty_surface.get_rect(center=(400, 30))
                    screen.blit(difficulty_surface, difficulty_rect)

                    main_screen = False

            elif event.type == pygame.MOUSEBUTTONDOWN and game_end == True:
                x, y = pygame.mouse.get_pos()
                if 295 <= x <= 425 and 440 <= y <= 505:
                    pass


        pygame.display.update()

if __name__ == "__main__":
    main()
