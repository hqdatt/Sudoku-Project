import pygame
import sudoku_generator
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        if self.difficulty == "Easy":
            self.board = sudoku_generator.generate_sudoku(9, 30)
        elif self.difficulty == "Medium":
            self.board = sudoku_generator.generate_sudoku(9, 40)
        elif self.difficulty == "Hard":
            self.board = sudoku_generator.generate_sudoku(9, 50)
        self.cells = [[Cell(self.board[row][col], row, col, screen) for col in range(9)] for row in range(9)]
    
    def draw(self):
        for i in range(10):
            line_width = 4 if i % 3 == 0 else 1  # Thick lines for every third line
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 60), (540, i * 60), line_width)

    # Draw vertical lines
        for i in range(10):
            line_width = 4 if i % 3 == 0 else 1  # Thick lines for every third line
            pygame.draw.line(self.screen, (0, 0, 0), (i * 60, 0), (i * 60, 540), line_width)

        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        #draw bottom line
        pygame.draw.line(self.screen, (0, 0, 0), (0, ((row + 1) // 3) * 180), (540, ((row + 1) // 3) * 180), 4)

    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.deselect()
        self.selected_cell = self.cells[row][col]
        self.selected_cell.select()

    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            row = y // 60
            col = x // 60
            return row, col
        return None
    
    def clear(self):
        if self.selected_cell:
            self.selected_cell.set_value(0)

    def sketch(self, value):
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell:
            self.selected_cell.set_value(value)

    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                cell.value = 0
                cell.sketched_value = None

    def is_full(self) -> bool:
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True        

    def update_board(self):
        ...

    def find_empty(self):
        ...
    
    def check_board(self):
        for row in range(9):
            for col in range(9):
                num = self.board[row][col]
                if not self.is_valid(row, col, num):
                    return False
        return True

    def valid_in_row(self, row, num) -> bool:
        return num not in self.board[row]

    def valid_in_col(self, col, num) -> bool:
        return all(row[col] != num for row in self.board)

    def valid_in_box(self, row_start, col_start, num) -> bool:
        return all(
            self.board[row][col] != num
            for row in range(row_start, row_start + 3)
            for col in range(col_start, col_start + 3)
        )
    
    def is_valid(self, row, col, num) -> bool:
        return (
            self.valid_in_row(row = row, num = num) and 
            self.valid_in_col(col = col, num = num) and 
            self.valid_in_box(row_start = row - row % 3, col_start = col - col % 3, num = num)
        )
    


        
