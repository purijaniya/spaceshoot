import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.direction = random.choice([-1, 1])
    
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.direction * 0.5
        
        # Bounce off edges
        if self.rect.left < 0 or self.rect.right > 800:
            self.direction *= -1
        
        # Remove if off screen
        if self.rect.top > 600:
            self.kill()
