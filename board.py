
import pygame

class Board:
    def __init__(self, screen, cell_size=40, board_size=8, spacing=150):
        self.screen = screen
        self.cell_size = cell_size
        self.board_size = board_size
        self.spacing = spacing
        self.piece = pygame.transform.scale(pygame.image.load("xe.png"), (cell_size, cell_size))

    def draw(self, x_start, y_start, positions):
        for r in range(self.board_size):
            for c in range(self.board_size):
                x = x_start + c * self.cell_size
                y = y_start + r * self.cell_size
                color = (255, 255, 255) if (r + c) % 2 == 0 else (55, 53, 62)
                pygame.draw.rect(self.screen, color, (x, y, self.cell_size, self.cell_size))
                if positions and (r, c) in positions:
                    self.screen.blit(self.piece, (x, y))
