import pygame, sys
from settings import *
from debug import debug

from level import Level

# GAME CLASS
class Game:
  
  # CONSTRUCTOR
  def __init__(self):
    
    pygame.init()
    
    # SCREEN SETUP
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # WINDOW SETUP
    self.window_width = SCREEN_WIDTH * 3
    self.window_height = SCREEN_HEIGHT * 3    
    pygame.display.set_caption('DOOMSAYER')
    
    # CLOCK SETUP
    self.clock = pygame.time.Clock()
    
    # LEVEL SETUP
    self.level = Level()
    
  # RUN METHOD
  def run(self):
    
    # GAME LOOP
    while True:
      for event in pygame.event.get():
        
        # QUIT EVENT
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
          
      # UPDATE DISPLAY & CLOCK
      self.screen.fill((0,0,0))
      self.level.run()
      pygame.display.update()
      self.clock.tick(FPS)
      
# RUN GAME
if __name__ == "__main__":
  game = Game()
  game.run()