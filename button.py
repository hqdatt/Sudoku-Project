import pygame
class Button:

    def __init__(self, text, x_pos, y_pos, enabled, screen, font):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.font = font
        self.screen = screen
        self.draw()

    def draw(self):
        button_text = self.font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 50))
        if self.check_click():
            pygame.draw.rect(self.screen, 'dark gray', button_rect, 0, 5)
        else:
            pygame.draw.rect(self.screen, 'light grey', button_rect, 0, 5)

        pygame.draw.rect(self.screen, 'black', button_rect, 2, 5)
        
        text_x = self.x_pos + (button_rect.width - button_text.get_width()) / 2
        text_y = self.y_pos + (button_rect.height - button_text.get_height()) / 2

        self.screen.blit(button_text, (text_x, text_y))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 50))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
