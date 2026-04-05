import pygame
import sys
from game.game import Game

def main():
    pygame.init()
    
    # Game settings
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 60
    
    # Create game instance
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
    
    # Run game loop
    game.run()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
