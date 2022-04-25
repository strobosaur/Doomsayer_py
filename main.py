import pygame, sys
from settings import *
from debug import debug

# GAME CLASS
class Game:
  
  # CONSTRUCTOR
  def __init__(self):
    
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('DOOMSAYER')
    self.clock = pygame.time.Clock()
    
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
      pygame.display.update()
      self.clock.tick(FPS)
      
# RUN GAME
if __name__ == "__main__":
  game = Game()
  game.run()