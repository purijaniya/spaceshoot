import pygame
import random
from game.player import Player
from game.enemy import Enemy
from game.bullet import Bullet

class Game:
    def __init__(self, width, height, fps):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Space Shooter")
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.score = 0
        
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        
        # Create player
        self.player = Player(width // 2, height - 50)
        self.all_sprites.add(self.player)
        
        # Enemy spawn timer
        self.enemy_spawn_timer = 0
        self.enemy_spawn_rate = 30
    
    def spawn_enemy(self):
        x = random.randint(0, 760)
        enemy = Enemy(x, -40)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.shoot():
                        bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
                        self.all_sprites.add(bullet)
                        self.bullets.add(bullet)
    
    def update(self):
        self.all_sprites.update()
        
        # Spawn enemies
        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer >= self.enemy_spawn_rate:
            self.spawn_enemy()
            self.enemy_spawn_timer = 0
        
        # Check collisions
        for bullet in self.bullets:
            hit = pygame.sprite.spritecollide(bullet, self.enemies, True)
            if hit:
                bullet.kill()
                self.score += 10
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)