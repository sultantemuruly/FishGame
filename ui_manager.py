import pygame
import os

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 32)

    def draw(self, surface):
        surface.fill((0, 100, 200))
        
        title_text = self.font.render("FISHING GAME", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.width//2, self.height//2 - 50))
        
        prompt_text = self.small_font.render("Press SPACE to start", True, (255, 255, 255))
        prompt_rect = prompt_text.get_rect(center=(self.width//2, self.height//2 + 20))
        
        surface.blit(title_text, title_rect)
        surface.blit(prompt_text, prompt_rect)


class EndPanel:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 32)

    def draw(self, surface, score):
        surface.fill((0, 100, 200))
        
        end_text = self.font.render("Time's Up!", True, (255, 255, 255))
        end_rect = end_text.get_rect(center=(self.width//2, self.height//2 - 50))
        
        score_text = self.small_font.render(f"Your Score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(self.width//2, self.height//2))
        
        quit_text = self.small_font.render("Press ESC to Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(self.width//2, self.height//2 + 50))
        
        surface.blit(end_text, end_rect)
        surface.blit(score_text, score_rect)
        surface.blit(quit_text, quit_rect)
