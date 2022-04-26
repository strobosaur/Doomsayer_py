import pygame
from settings import *
from debug import debug

class Player(pygame.sprite.Sprite):
  
  # CONSTRUCTOR
  def __init__(self,pos,groups):
    super().__init__(groups)
    self.image = pygame.image.load('sprites/droid/idle_d3_01.png').convert_alpha()
    self.rect = self.image.get_rect(topleft = pos)
    
    self.direction  = pygame.math.Vector2()
    self.speed = 1.25
    
  # GET INPUT METHOD
  def input(self):
    keys = pygame.key.get_pressed()
    
    # VERTICAL AXIS
    if keys[pygame.K_UP]:
      self.direction.y = -1
    elif keys[pygame.K_DOWN]:
      self.direction.y = 1
    else:
      self.direction.y = 0
      
    # HORIZONTAL AXIS
    if keys[pygame.K_RIGHT]:
      self.direction.x = 1
    elif keys[pygame.K_LEFT]:
      self.direction.x = -1
    else:
      self.direction.x = 0
      
  # MOVE METHOD
  def move(self,speed):
    
    # NORMALIZE MOVEMENT VECTOR
    if self.direction.magnitude() != 0:
      self.direction = self.direction.normalize()
      
    # UPDATE POSITION
    debug(self.direction * speed)
    self.rect.center += self.direction * speed
      
  # UPDATE
  def update(self):
    self.input()
    self.move(self.speed)