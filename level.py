import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
  
  # CONSTRUCTOR
  def __init__(self):
    
    # GET DISPLAY SURFACE
    self.display_surface = pygame.display.get_surface()
    
    # SPRITE GROUPS
    self.visible_sprites = pygame.sprite.Group()
    self.obstacle_sprites = pygame.sprite.Group()
    
    # SPRITE SETUP
    self.create_map()
    
  # CREATE MAP METHOD
  def create_map(self):
    for j, row in enumerate(GAME_MAP):
      for i, col in enumerate(row):
        x = i * TILESIZE
        y = j * TILESIZE
        if col == 'x':
          Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
        if col == 'p':
          Player((x,y),[self.visible_sprites])
    
  # RUN METHOD
  def run(self):
    
    # UPDATE AND DRAW SPRITES
    self.visible_sprites.draw(self.display_surface)