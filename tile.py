import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
  def __init__(self,pos,groups):
    super().__init__(groups)
    self.image = pygame.image.load('tiles/bg_stone01_16x16_48x64.png').convert_alpha()
    self.rect = self.image.get_rect(topleft = pos)