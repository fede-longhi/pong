import pygame
from pygame.locals import *
from utils import *
import random

class Pala(pygame.sprite.Sprite):
	def __init__(self, x, y, height):
		self.image = load_image("imagenes/pala.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.speed = 0.5
		self.height = height
		
	def mover(self, time, ball, keys):
		pass
				
				
class Pala_Jugador(Pala):
	def __init__(self, x, y, height):
		self.image = load_image("imagenes/pala.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.speed = 0.5
		self.height = height
		
	def mover(self, time, ball, keys):
		if self.rect.top >= 0:
			if keys[K_UP]:
				self.rect.centery -= self.speed*time
				
		if self.rect.bottom <= self.height:
			if keys[K_DOWN]:
				self.rect.centery += self.speed*time
			
class Pala_IA_Facil(Pala):
	def __init__(self, x, y, height):
		self.image = load_image("imagenes/pala.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.speed = 0.5
		self.height = height
		
	def mover(self, time, ball, keys):
		retardo = random.randint(0,10)
		distancia = [ball.width-ball.width/5, ball.width-ball.width/4, ball.width-ball.width/3, ball.width/2, 0]
		eleccion = 0
		if retardo == 1:
			eleccion = 0
		if retardo == 2:
			eleccion = 1
		if retardo > 2 and retardo < 7:
			eleccion = 2 
		if retardo >= 7:
			eleccion = 3

		if ball.speed[0] >= 0 and ball.rect.centerx >= distancia[eleccion]:
			if self.rect.centery < ball.rect.centery:
				self.rect.centery += self.speed * time
			if self.rect.centery > ball.rect.centery:
				self.rect.centery -= self.speed * time
				
class Pala_IA_Dificil(Pala):
	def __init__(self, x, y, height):
		self.image = load_image("imagenes/pala.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.speed = 0.5
		self.height = height
		
	def mover(self, time, ball, keys):
		retardo = random.randint(0,10)
		distancia = [ball.width-ball.width/3, ball.width/2, 0]
		eleccion = 0
		if retardo == 1:
			eleccion = 0
		if retardo == 2:
			eleccion = 1
		if retardo > 2:
			eleccion = 2

		if ball.speed[0] >= 0 and ball.rect.centerx >= distancia[eleccion]:
			if self.rect.centery < ball.rect.centery:
				self.rect.centery += self.speed * time
			if self.rect.centery > ball.rect.centery:
				self.rect.centery -= self.speed * time	
