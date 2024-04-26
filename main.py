import pygame
import sys
import constants as co
import sudoku_generator
from cell import Cell
from board import Board
from button import Button

main_menu = True
game_screen = False
win_screen = False
lose_screen = False
easy = False
medium = False
hard = False
board = None
running = True
selected_row = None
selected_col = None
resetter = False

def draw_text(text, font, text_col, x, y, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def actual_game(screen, board):
    global running
    global selected_row
    global selected_col
    global win_screen
    global lose_screen
    global game_screen
    global main_menu

    button_font = pygame.font.Font(None, 40)
    screen.fill((co.WHITE))
    board.draw()

    reset_button = Button("Reset", 20, 565, True, screen, button_font)
    restart_button = Button("Restart", 190, 565, True, screen, button_font)
    exit_button = Button("Exit", 360, 565, True, screen, button_font)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x < 540 and mouse_y < 540:
                new_selected_row, new_selected_col = board.click(mouse_x, mouse_y)

                if (new_selected_row, new_selected_col) != (selected_row, selected_col):
                    if selected_row is not None and selected_col is not None:
                        board.cells[selected_row][selected_col].deselect()
                    selected_row, selected_col = new_selected_row, new_selected_col
                    board.cells[selected_row][selected_col].select()

        elif event.type == pygame.KEYDOWN:
            if selected_row is not None and selected_col is not None:
                cell = board.cells[selected_row][selected_col]
                if cell.editable:
                    if event.unicode.isdigit() and int(event.unicode) in range(1, 10):
                        cell.set_sketched_value(int(event.unicode))
                        board.board[selected_row][selected_col] = int(event.unicode)
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_BACKSPACE:
                        cell.set_sketched_value(0)
                        cell.set_cell_value(0)
                        board.board[selected_row][selected_col] = 0
                    elif event.key == pygame.K_RETURN and cell.sketched_value != 0:
                        cell.set_cell_value(cell.sketched_value)
                        board.board[selected_row][selected_col] = cell.sketched_value
                        cell.set_sketched_value(0)

                elif event.key == pygame.K_UP:
                    if selected_row > 0:
                        new_selected_row -= 1
                        board.cells[selected_row][selected_col].deselect()
                        selected_row = new_selected_row
                        board.cells[selected_row][selected_col].select()
                elif event.key == pygame.K_DOWN:
                    if selected_row < 8:
                        new_selected_row += 1
                        board.cells[selected_row][selected_col].deselect()
                        selected_row = new_selected_row
                        board.cells[selected_row][selected_col].select()
                elif event.key == pygame.K_LEFT:
                    if selected_col > 0:
                        new_selected_col -= 1
                elif event.key == pygame.K_RIGHT:
                    if selected_col < 8:
                        new_selected_col += 1

    if board.is_full():
        if board.check_board():
            print("Sudoku is correct")
            game_screen = False
            win_screen = True
        else:
            print("Incorrect Sudoku")
            game_screen = False
            lose_screen = True

    global resetter

    if reset_button.check_click():
        board.reset_board()
    if restart_button.check_click():
        resetter = True
        game_screen = False
        main_menu = True
    if exit_button.check_click():
        pygame.quit()
        running = False

    pygame.display.flip()

def display_main_menu(screen):
    start_title_font = pygame.font.SysFont(None, 70)
    button_font = pygame.font.Font(None, 40)

    screen.fill((255, 255, 255))

    title_surface = start_title_font.render("Welcome to Sudoku", 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(center=(co.WIDTH // 2, co.HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    start_title_font = pygame.font.SysFont('lato', 50)

    title_surface2 = start_title_font.render("Select Game Mode:", 0, (0, 0, 0))
    title_rectangle2 = title_surface.get_rect(center=(co.WIDTH // 2 + 60, co.HEIGHT // 2 + 100))
    screen.blit(title_surface2, title_rectangle2)

    easy_button = Button("Easy", 20, 460, True, screen, button_font)
    medium_button = Button("Medium", 190, 460, True, screen, button_font)
    hard_button = Button("Hard", 360, 460, True, screen, button_font)

    global main_menu 
    global game_screen  
    global easy
    global hard
    global medium
    if easy_button.check_click():
        screen.fill((co.WHITE))
        main_menu = False
        game_screen = True
        easy = True
        medium = False
        hard = False
    if medium_button.check_click():
        screen.fill((co.WHITE))
        main_menu = False
        game_screen = True
        medium = True
        hard = False
        easy = False
    if hard_button.check_click():
        screen.fill((co.WHITE))
        main_menu = False
        game_screen = True
        hard = True
        medium = False
        easy = False
    pygame.display.flip()

# Initialize Pygame
def main():
    # # Main game loop

    pygame.init()
    screen = pygame.display.set_mode([co.WIDTH, co.HEIGHT])
    pygame.display.set_caption("Sudoku")
    # Arial font
    arial_font = pygame.font.SysFont("arialblack", 40)
    button_font = pygame.font.Font(None, 40)

    board = None
    global running
    global resetter
    global main_menu
    global win_screen
    global lose_screen
    global game_screen 

    while running:
        if main_menu:
            display_main_menu(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        if game_screen:
            if board == None or resetter:
                resetter = False
                if easy:
                    board = Board(co.WIDTH, co.HEIGHT, screen, "Easy")
                elif medium:
                    board = Board(co.WIDTH, co.HEIGHT, screen, "Medium")
                elif hard:
                    board = Board(co.WIDTH, co.HEIGHT, screen, "Hard")
            actual_game(screen, board)
        if win_screen:
            screen.fill((255, 255, 255))
            gator_win_img = pygame.image.load('Gator_winner.png').convert_alpha()
            gator_win_img = pygame.transform.scale(gator_win_img, (80 * 3, 80 * 3))
            screen.blit(gator_win_img, (150, 20))
            draw_text("Game Won!", arial_font, (0, 0, 0), 150, 300, screen)
            #Add exit button here on coords x = (width - 150) / 2 and y = 500

            exit_button = Button("Exit", (co.WIDTH - 150) / 2, 500, True, screen, button_font)

            if exit_button.check_click():
                pygame.quit()
                running = False

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        if lose_screen:
            screen.fill((255, 255, 255))
            gator_lose_img = pygame.image.load('Gator_loser.png').convert_alpha()
            gator_lose_img = pygame.transform.scale(gator_lose_img, (80 * 3, 80 * 3))
            screen.blit(gator_lose_img, (150, 20))
            draw_text("Game Over :(", arial_font, (0, 0, 0), 150, 300, screen)
            #Add restart button here on coords x = (width - 150) / 2 and y = 500

            restart_button = Button("Restart", (co.WIDTH - 150) / 2, 500, True, screen, button_font)

            if restart_button.check_click():
                lose_screen = False
                main_menu = True
                resetter = True

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

if __name__ == "__main__":
    main()
