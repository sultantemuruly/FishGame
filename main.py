import pygame
import sys
import os
from fish import Fish
from bomb import Bomb
from rod import FishingRod
from ui_manager import Menu, EndPanel

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish Game")

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

clock = pygame.time.Clock()

STATE_MENU = "MENU"
STATE_GAME = "GAME"
STATE_END = "END"

game_state = STATE_MENU

menu = Menu(WIDTH, HEIGHT)
end_panel = EndPanel(WIDTH, HEIGHT)

fishes = []
rod = FishingRod(WIDTH//2, HEIGHT//2)

spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, 2000)

score = 0
time_left = 59
timer_event = pygame.USEREVENT + 2
pygame.time.set_timer(timer_event, 1000)

font = pygame.font.SysFont(None, 32)

running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if game_state == STATE_MENU:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = STATE_GAME
                fishes = [Fish(WIDTH, HEIGHT) for _ in range(5)]
                bombs = [Bomb(WIDTH, HEIGHT) for _ in range(5)]
                rod = FishingRod(WIDTH//2, HEIGHT//2)
                score = 0
                time_left = 59
        elif game_state == STATE_GAME:
            if event.type == spawn_event:
                if len(fishes) < 10:
                    fishes.append(Fish(WIDTH, HEIGHT))
                if len(bombs) < 5:
                    bombs.append(Bomb(WIDTH, HEIGHT))
            if event.type == timer_event:
                time_left -= 1
                if time_left <= 0:
                    game_state = STATE_END
        elif game_state == STATE_END:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

    if game_state == STATE_MENU:
        menu.draw(window)
        pygame.display.flip()
        continue

    elif game_state == STATE_GAME:
        rod.handle_input()

        for fish in fishes:
            fish.update()
        
        for bomb in bombs:
            bomb.update()

        for fish in fishes[:]:
            if rod.rect.colliderect(fish.rect):
                fishes.remove(fish)
                score += 1
        
        for bomb in bombs[:]:
            if rod.rect.colliderect(bomb.rect):
                bombs.remove(bomb)
                score -= 1

        window.blit(background_image, (0, 0))
        
        for fish in fishes:
            fish.draw(window)
        for bomb in bombs:
            bomb.draw(window)
        rod.draw(window)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        timer_text = font.render(f"Time: {time_left}", True, (255, 255, 255))
        
        window.blit(score_text, (10, 10))
        window.blit(timer_text, (WIDTH - 100, 10))

        pygame.display.flip()
        continue

    elif game_state == STATE_END:
        end_panel.draw(window, score)
        pygame.display.flip()
        continue

pygame.quit()
sys.exit()
