import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.shoot_cooldown = 0
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 750:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 560:
            self.rect.y += self.speed
        
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def shoot(self):
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = 10
            return True
        return False
