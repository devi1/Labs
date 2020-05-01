import pygame, random, os


pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1' #чтобы центрилизировать окно запуска

def fucked1(a_x, a_y, x_t, y_t):
	if a_x >= x_t and a_x <= x_t + 70 and a_y >= y_t and a_y <= y_t +70:
		return 1
	else: return 0

def fucked2(a_x, a_y, x_t, y_t):
	if a_x >= x_t and a_x <= x_t + 70 and a_y >= y_t and a_y <= y_t +70:
		return 1
	else: return 0

w = 1000
h = 1000

screen = pygame.display.set_mode((w, h))
background = pygame.image.load('ground.jpg')

FPS = 60

clock = pygame.time.Clock() 

t1 = pygame.image.load('t1_up.png') 
t2 = pygame.image.load('t2_up.png') 

cnt1 = 3
cnt2 = 3
myfont = pygame.font.SysFont('Retro.ttf', 40)

arrow1 = pygame.Surface((15,15))

a1_x = 1100
a1_y = 1100
strike1 = False

arrow2 = pygame.Surface((15,15))

a2_x = 1100
a2_y = 1100
strike2 = False

x_t1 = 70 
y_t1 = 535

x_t2 = 860
y_t2 = 535

speed1 = 5
speed2 = 5

up = 'up'
down = 'down'
left = 'left'
right = 'right'

movement1 = False 
movement2 = False 

shoot_sound = pygame.mixer.music.load("crash.mp3")

pygame.display.update()

def end(l1, l2):
	myfont = pygame.font.SysFont('arial', 100)
	ending1 = myfont.render('GAME OVER', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	ending1_1 = myfont.render('P1 wins', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	ending2 = myfont.render('GAME OVER', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	ending1_2 = myfont.render('P2 wins', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	if l1 == 0:
		background = pygame.image.load('ground1.jpg')
		screen.blit(background,(0,0))
		screen.blit(ending2,(250, 200))
		screen.blit(ending1_2,(350, 300))
	if l2 == 0:
		background = pygame.image.load('ground1.jpg')
		screen.blit(background,(0,0))
		screen.blit(ending1,(250, 200))
		screen.blit(ending1_1,(350, 300))


play = True

while play:

	pygame.display.update()
	arrow1.fill((random.randint(0,255),random.randint(0,255),0))
	arrow2.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

	if movement1 == up:
		t1 = pygame.image.load('t1_up.png') 
		y_t1 -= speed1
		if strike1:
			a1_y-=20
			if a1_y < -10:
				strike1 = False

	if movement1 == down:
		t1 = pygame.image.load('t1_down.png')
		y_t1 += speed1
		if strike1:
			a1_y+=20
			if a1_y > h+10:
				strike1 = False

	if movement1 == right:
		t1 = pygame.image.load('t1_right.png')
		x_t1 += speed1
		if strike1:
			a1_x+=20
			if a1_x > w+10:
				strike1 = False

	if movement1 == left:
		t1 = pygame.image.load('t1_left.png')
		x_t1 -= speed1
		if strike1:
			a1_x-=20
			if a1_x < -10:
				strike1 = False


	if movement2 == up:
		t2 = pygame.image.load('t2_up.png')
		y_t2 -= speed2
		if strike2:
			a2_y-=20
			if a2_y < -10:
				strike2 = False

	if movement2 == down:
		t2 = pygame.image.load('t2_down.png')
		y_t2 += speed2
		if strike2:
			a2_y+=20
			if a2_y > h+10:
				strike2 = False

	if movement2 == right:
		t2 = pygame.image.load('t2_right.png')
		x_t2 += speed2
		if strike2:
			a2_x += 20
			if a2_x > w+10:
				strike2 = False

	if movement2 == left:
		t2 = pygame.image.load('t2_left.png')
		x_t2 -= speed2
		if strike2:
			a2_x-=20
			if a2_x < -10:
				strike2 = False



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit()
			if event.key == pygame.K_LSHIFT:
				speed1 = 10
			if event.key == pygame.K_SPACE:
				pygame.mixer.music.play()
				if strike1 == False:
					strike1 = True
					if movement1 == up:
						a1_x = x_t1 + 32
						a1_y = y_t1
					if movement1 == down:
						a1_x = x_t1 + 32
						a1_y = y_t1 + 70
					if movement1 == right:
						a1_x = x_t1 + 70
						a1_y = y_t1 + 32
					if movement1 == left:
						a1_x = x_t1 
						a1_y = y_t1 + 32
			if event.key == pygame.K_LCTRL:
				x_t1 = a1_x
				y_t1 = a1_y
				strike1 = False

		#if event.type == pygame.KEYUP:
			#if event.key in [pygame.K_LSHIFT]:
				#speed1 = 5
				
			if event.key == pygame.K_RETURN:
				pygame.mixer.music.play()
				if strike2 == False:
					strike2 = True
					if movement2 == up:
						a2_x = x_t2 + 32
						a2_y = y_t2
					if movement2 == down:
						a2_x = x_t2 + 32
						a2_y = y_t2 + 70
					if movement2 == right:
						a2_x = x_t2 + 70
						a2_y = y_t2 + 32
					if movement2 == left:
						a2_x = x_t2 
						a2_y = y_t2 + 32

			if event.key == pygame.K_RCTRL:
				x_t2 = a2_x
				y_t2 = a2_y
				strike2 = False

			if event.key == pygame.K_d:  
				movement1 = right
			if event.key == pygame.K_a:
				movement1 = left
			if event.key == pygame.K_w: 	
				movement1 = up
			if event.key == pygame.K_s:
				movement1 = down
			if event.key == pygame.K_LALT:
				movement1 = False

			if event.key == pygame.K_RIGHT:
				movement2 = right
			if event.key == pygame.K_LEFT:
				movement2 = left
			if event.key == pygame.K_UP:
				movement2 = up
			if event.key == pygame.K_DOWN:
				movement2 = down
			if event.key == pygame.K_KP0:
				movement2 = False

	if fucked1(a1_x, a1_y, x_t2, y_t2):
		cnt2 -= 1
		strike1 = False
		pygame.mixer.music.play()
		x_t2 = 860
		y_t2 = 535

	if fucked2(a2_x, a2_y, x_t1, y_t1):
		cnt1 -= 1
		strike2 = False
		pygame.mixer.music.play()
		x_t1 = 70
		y_t1 = 535

	if x_t1 > w + 60:
		x_t1 = 0 - 60
	if x_t1 < 0 -60:
		x_t1 = w + 60
	if y_t1 > w + 60:
		y_t1 = 0 - 60
	if y_t1 < 0 -60:
		y_t1 = w + 60
                                             
	if x_t2 > w + 60:
		x_t2 = 0 - 60
	if x_t2 < 0 -60:
		x_t2 = w + 60
	if y_t2 > w + 60:
		y_t2 = 0 - 60
	if y_t2 < 0 -60:
		y_t2 = w + 60

	if strike1 == False:
		a1_x = 1100
		a1_y = 1100
	if strike2 == False:
		a2_x = 1100
		a2_y = 1100

	string1 = myfont.render("P1:" + str(cnt1), True, (255,255,255))
	string2 = myfont.render("P2:" + str(cnt2), True, (255,255,255))

	screen.blit(background, (0,0))
	screen.blit(string1, (70, 70))
	screen.blit(string2, (840, 70))
	screen.blit(t1, (x_t1, y_t1))
	screen.blit(t2, (x_t2, y_t2))
	clock.tick(FPS)
	screen.blit(arrow1, (a1_x,a1_y))
	screen.blit(arrow2, (a2_x,a2_y))

	pygame.display.set_caption("TANK MOTHERF*CKER")
	end(cnt1, cnt2)
	pygame.display.flip()




pygame.quit()