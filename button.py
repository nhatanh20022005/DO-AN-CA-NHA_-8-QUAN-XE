
import pygame

class Button:
    def __init__(self, text, x, y, w, h, base_color, hover_color, font):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.base_color = base_color
        self.hover_color = hover_color
        self.font = font

    def draw(self, screen, mouse_pos):
        hover = self.rect.collidepoint(mouse_pos)
        color = self.hover_color if hover else self.base_color
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, border_radius=12)
        label = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(label, (self.rect.x + (self.rect.w - label.get_width()) // 2,
                            self.rect.y + (self.rect.h - label.get_height()) // 2))
        return hover
