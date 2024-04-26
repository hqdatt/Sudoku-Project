import pygame
import sys
import sudoku_generator
from cell import Cell
from board import Board
from button import Button

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 540, 669
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up font
font = pygame.font.SysFont(None, 36)
smallfont = pygame.font.SysFont('Corbel', 35)

board = Board(540, 669, screen, "Easy")

# Main game loop
selected_row, selected_col = None, None
running = True
while running:
    # Handle events
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
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_BACKSPACE:
                        cell.set_sketched_value(0)
                        cell.set_cell_value(0)
                    elif event.key == pygame.K_RETURN:
                        cell.set_cell_value(cell.sketched_value)
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

    # Check if the board is full and correct
    if board.is_full():
        if board.check_board():
            print("Sudoku is correct")
        else:
            print("Incorrect Sudoku")

    # Fill the screen with white
    screen.fill(WHITE)

    board.draw()
    reset_button = Button("Reset", 20, 569, True, screen, smallfont)
    restart_button = Button("Restart", 200, 569, True, screen, smallfont)
    quit_button = Button("Quit", 380, 569, True, screen, smallfont)

    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
