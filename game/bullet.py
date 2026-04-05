import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 7
    
    def update(self):
        self.rect.y -= self.speed
        
        # Remove if off screen
        if self.rect.bottom < 0:
            self.kill()
