import pygame
from pygame.locals import *
from utils import *

class Bola(pygame.sprite.Sprite):
	
	def __init__ (self, width, height):
		"""width, height son los limites donde rebota la bola"""
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("imagenes/ball.png", True)
		self.rect = self.image.get_rect()
		self.rect.centerx = width/2
		self.rect.centery = height/2
		self.speed = [0.5,-0.5]
		self.width = width
		self.height = height
		
	def actualizar (self, time, pala_jug, pala_cpu, puntos):
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time
		pared = False
		
		if self.rect.left <= 0:
			puntos[0] += 1
			pared = True
		if self.rect.right >= self.width:
			puntos[1] += 1
			pared = True
		
		if self.rect.left <= 0 or self.rect.right >= self.width:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if self.rect.top <= 0 or self.rect.bottom >= self.height:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time
		if pygame.sprite.collide_rect(self,pala_jug):
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if pygame.sprite.collide_rect(self, pala_cpu):
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
			
		return puntos, pared

	def centrar (self):
		self.rect.centerx = self.width/2
		self.rect.centery = self.height/2
