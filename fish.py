import pygame
import random
import os

class Fish:
    def __init__(self, width, height):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "fish_red.png")

        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(0, height - self.rect.height)

        self.dx = random.uniform(-3, 3)
        self.dy = random.uniform(-3, 3)

        if self.dx == 0 and self.dy == 0:
            self.dx = 1

        self.screen_width = width
        self.screen_height = height

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.x <= 0 or self.rect.x >= self.screen_width - self.rect.width:
            self.dx = -self.dx
        if self.rect.y <= 0 or self.rect.y >= self.screen_height - self.rect.height:
            self.dy = -self.dy

    def draw(self, surface):
        surface.blit(self.image, self.rect)
