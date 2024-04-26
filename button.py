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
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 69))
        if self.check_click():
            pygame.draw.rect(self.screen, 'dark gray', button_rect, 0, 5)
        else:
            pygame.draw.rect(self.screen, 'light grey', button_rect, 0, 5)

        pygame.draw.rect(self.screen, 'black', button_rect, 2, 5)
        self.screen.blit(button_text, (self.x_pos+18, self.y_pos+15))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 69))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
