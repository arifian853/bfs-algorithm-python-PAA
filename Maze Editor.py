import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1120,640),0,32)
maps = []
myfont = pygame.font.SysFont("Segoe UI", 15)
type = 0
types = ('Dinding', 'Pintu', 'Tempat Tidur', 'Kursi')
colors = ((0,0,0),(255,100,100),(255,0,0),(0,255,0))
x=0
Matrix = [[(-1,-1,-1,-1,-1) for x in range(20)] for x in range(25)]
print (Matrix[24][19])

def select(type):
	if type == 0:
		return (0,0,0)
	elif type == 1:
		return (1,1,1)
	elif type == 2:
		return (0,1,2)
	elif type == 3:
		return (0,1,3)

while 1:
	background = pygame.Surface((screen.get_size()))
	background.fill((182,194,217))
	for event in pygame.event.get():
		if event.type == QUIT:
			x=0
			y=0
			a = open('maps.txt', 'w')
			for x in range(20):
				for y in range(25):
					if y!=24:
						a.write(str(Matrix[y][x][0]))
						a.write(' ')
						a.write(str(Matrix[y][x][1]))
						a.write(' ')
						a.write(str(Matrix[y][x][2]))
						a.write(' ')
						a.write(str(Matrix[y][x][3]))
						a.write(' ')
						a.write(str(Matrix[y][x][4]))
						a.write('\n')
					else:
						a.write(str(Matrix[y][x][0]))
						a.write(' ')
						a.write(str(Matrix[y][x][1]))
						a.write(' ')
						a.write(str(Matrix[y][x][2]))
						a.write(' ')
						a.write(str(Matrix[y][x][3]))
						a.write(' ')
						a.write(str(Matrix[y][x][4]))
						a.write('\n')
			a.close()
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_a:
				type = 0
			elif event.key == K_s:
				type = 1
			elif event.key == K_d:
				type = 2
			elif event.key == K_f:
				type = 3
		if event.type == MOUSEBUTTONDOWN:
			posi = []
			posi.append(int(event.pos[0]/32))
			posi.append(int(event.pos[1]/32))
			ret = select(type)
			posi.append(ret[0])
			posi.append(ret[1])
			posi.append(ret[2])
			maps.append(posi)
			Matrix[posi[0]][posi[1]] = posi

	screen.lock()

	pygame.draw.rect(background, (0, 255, 38), Rect((0,0), (32,32)))
	i=25
	while i!=0:
		pygame.draw.line(background, (35,61,77), (i*32,0), (i*32,640))
		i=i-1

	i=20
	while i!=0:
		pygame.draw.line(background, (35,61,77), (0,i*32), (800,i*32))
		i=i-1

	x=0
	y=0
	for x in range(20):
		for y in range(25):			
			if Matrix[y][x][0]!=-1:
				pygame.draw.rect(background, colors[Matrix[y][x][4]], Rect((y*32,x*32), (32,32)))

	#Menampilkan tulisan + pilihan 
	label = myfont.render("A - Dinding", 1, (0,0,0))
	label2 = myfont.render("S - Pintu", 1, (0,0,0))	
	label3 = myfont.render("D - Tempat Tidur", 1, (0,0,0))	
	label4 = myfont.render("F - Kursi", 1, (0,0,0))
	label5 = myfont.render('Terpilih: ' + types[type], 1, (0,0,0))			
	
	screen.unlock()

	screen.blit(background, (0,0))
	screen.blit(label, (810, 0))
	screen.blit(label2, (810, 15))
	screen.blit(label3, (810, 30))
	screen.blit(label4, (810, 45))
	screen.blit(label5, (810, 60))

	pygame.display.update()