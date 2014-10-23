#!/usr/bin/env python
# -*- coding: utf-8 -*-

#------ Modulos --------#
import sys, pygame, time
from pygame.locals import *
from bola import *
from pala import *
from utils import *

#------ Constantes --------#

WIDTH = 600
HEIGHT = 400

def main():
	
	clock = pygame.time.Clock()
	
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Pong")
	fondo = load_image("imagenes/fondo.jpg")
	
	bola = Bola(WIDTH, HEIGHT)
	pala_jug = Pala_Jugador(30, HEIGHT/2, HEIGHT)
	pala_cpu = Pala_IA_Dificil(WIDTH - 30, HEIGHT/2, HEIGHT)
		
	puntos = [0,-1] #hay que ver porque suma uno (es un problema de bola actualizar)
		
	gameOver = False
	pared = False
	
	while not gameOver:
		tiempo = clock.tick(60)
		keys = pygame.key.get_pressed()

		for event in pygame.event.get():
			if event.type == QUIT:
					sys.exit(0)
		
		puntos, pared = bola.actualizar(tiempo, pala_jug, pala_cpu, puntos)
		pala_jug.mover(tiempo, bola, keys)
		pala_cpu.mover(tiempo, bola, keys)
		
		p_jug, p_jug_rect = texto(str(puntos[0]), WIDTH/4, 40)
		p_cpu, p_cpu_rect = texto(str(puntos[1]), WIDTH-WIDTH/4, 40)
		
		if pared:
			bola.centrar()
		
		screen.blit(fondo, (0,0))
		screen.blit(pala_jug.image, pala_jug.rect)
		screen.blit(pala_cpu .image, pala_cpu.rect)
		screen.blit(bola.image, bola.rect)
		screen.blit(p_jug, p_jug_rect)
		screen.blit(p_cpu, p_cpu_rect)
		pygame.display.flip()

	return 0
			
				

	
if __name__ == "__main__":
	pygame.init()
	main()
