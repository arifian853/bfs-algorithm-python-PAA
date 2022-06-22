import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1120,640),0,32)
Matrix = [[(-1,-1,-1,-1,-1) for x in range(25)] for x in range(20)]
vis = [[(-1,-1) for x in range(25)] for x in range(20)]
cor = ((0,0,0),(255,100,100),(255,0,0),(0,255,0))
myfont = pygame.font.SysFont("Segoe UI", 16)
i=0
j=0
k=0
p=-1
a = open('maps.txt', 'r')
for j in range(20):
	for x in range(25):
		save = a.readline()
		save = save.rstrip('\r')
		save = save.split()
		p=p+1
		print('%d %d %d %d %d %d' %(int(save[0]), int(save[1]), int(save[2]), int(save[3]), int(save[4]), p))
		tempo = []
		ka = int(save[0])
		tempo.append(ka)
		ka = int(save[1])
		tempo.append(ka)
		ka = int(save[2])
		tempo.append(ka)
		ka = int(save[3])
		tempo.append(ka)
		ka = int(save[4])
		tempo.append(ka)			
		Matrix[j][x] = tempo	
clock = pygame.time.Clock()
FPS = 60

def pathfind(posfimx, posfimy):
	fila = []
	fila.append((posfimy,posfimx))
	dx = (1, 0, -1, 0)
	dy = (0, 1, 0, -1)
	vis[posfimy][posfimx] = (-2, -2)
	while len(fila) != 0:		
		y = fila[0][0]
		x = fila[0][1]		
		lixo = fila.pop(0)
		for i in range(4):			
			xx = x+dx[i]
			yy = y+dy[i]
			if (xx < 0) or (xx > 24) or (yy < 0) or (yy > 19):				
					lixo = 0			
			else:
				if (Matrix[yy][xx][2] != 0) and (vis[yy][xx][0] == -1):					
					vis[yy][xx] = (y,x)					
					fila.append((yy, xx))

startFlag = 0
op=1
playtime=0
while 1:
	milliseconds = clock.tick(FPS)
	seconds = milliseconds / 250.0
	playtime += milliseconds /250.0
	background = pygame.Surface((screen.get_size()))
	background.fill((182,194,217))
	for event in pygame.event.get():
		if event.type == QUIT:
			a.close
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			if op == 1:
				posini = []
				posini.append(int(event.pos[0]/32))
				posini.append(int(event.pos[1]/32))
				startFlag = 1
			elif op == 2:
				posfim = []
				posfim.append(int(event.pos[0]/32))
				posfim.append(int(event.pos[1]/32))
		if event.type == KEYDOWN:
			if event.key == K_a:
				op = 1
			if event.key == K_f:
				op = 2
			if event.key == K_s:
				op = 3
				flag = 0

	if op == 3 and flag == 0:
		pathfind(posfim[0], posfim[1])
		print('-')
		routes = []
		while (posini[0] != posfim[0]) or (posini[1] != posfim[1]):
			print('-')
			novoy = vis[posini[1]][posini[0]][0]
			novox = vis[posini[1]][posini[0]][1]
			posini = (novox, novoy)		
			routes.append(posini)
		tempo = playtime
		flag = 1

	screen.lock()
	if startFlag != 0:
		pygame.draw.rect(background, (0, 255, 38), Rect((posini[0]*32,posini[1]*32), (32,32)))
	label = myfont.render("Tekan dimanapun = HIJAU = Posisi Awal", 1, (0, 0, 0))
	label2 = myfont.render("Tekan F lalu pilih Posisi Akhir", 1, (0,0,0))	
	label3 = myfont.render("Tekan S untuk Mulai", 1, (0,0,0))
	label4 = myfont.render("---------------------------------------------------", 1, (0,0,0))
	label5 = myfont.render("Arifian Saputra - 2001020029", 1, (0,0,0))
	label6 = myfont.render("Samuel Miskan Hanock - 2001020037", 1, (0,0,0))
	label7 = myfont.render("Perancangan dan Analisis Algoritma", 1, (0,0,0))
	i=25
	while i!=0:
		pygame.draw.line(background, (35,61,77), (i*32,0), (i*32,640))
		i=i-1

	i=20
	while i!=0:
		pygame.draw.line(background, (35,61,77), (0,i*32), (800,i*32))
		i=i-1

	for j in range(20):
		for x in range(25):
			if Matrix[j][x][0] != -1:
					pygame.draw.rect(background, cor[Matrix[j][x][4]], Rect((x*32,j*32), (32,32),))
	screen.unlock()
					
	if op == 3 and len(routes) != 0:
		if playtime >= 1.0:
			playtime = 0.0
			posini = routes[0]
			routes.pop(0)

	screen.blit(background, (0,0))
	screen.blit(label, (810, 0))
	screen.blit(label2, (810, 15))
	screen.blit(label3, (810, 30))
	screen.blit(label4, (810, 45))
	screen.blit(label5, (810, 120))
	screen.blit(label6, (810, 135))
	screen.blit(label7, (810, 165))
	pygame.display.update()