import pygame

class Cell:

    RED = (139,0,0)
    BLACK = (0, 0, 0)
    GRAY = (128,128,128)

    def __init__(self, value, row, col, screen) -> None:
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = 0
        self.editable = True if self.value == 0 else False
        
    
    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        if self.value != 0:
            font = pygame.font.SysFont('lato', 45)
            COLOR = self.RED if self.editable else self.BLACK
            text = font.render(str(self.value), True, COLOR)
            text_rect = text.get_rect(center = (self.col * 60 + 60 // 2, self.row * 60 + 60 // 2))
            self.screen.blit(text, text_rect)

        if self.sketched_value != 0:
            font = pygame.font.SysFont('lato', 25)
            COLOR = self.GRAY
            text = font.render(str(self.sketched_value), True, COLOR)
            text_rect = text.get_rect(center = (self.col * 60 + 45, self.row * 60 + 17))
            self.screen.blit(text, text_rect)

        if self.selected == True:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.col * 60, self.row * 60, 60, 60), 3)

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False
