import sys
import pygame
import random

icon_kappa = pygame.image.load('bi-dama.png')
img_bg = pygame.image.load('c1.png')
img_player = pygame.image.load('c2.png')
img_water = pygame.image.load('c3.png')
img_flour = pygame.image.load('c4.png')
txt_gameover = pygame.image.load('h1.png')

voice_up = None
voice_down = None

STEP_READY = 0
STEP_PLAY = 1
STEP_GAMEOVER = 2
SURFACE_WIDTH = 800
SURFACE_HEIGHT = 600
ITEM_TYPE_NUM = 2
ITEM_WIDTH = 50
ITEM_HEIGHT = 72
ITEM_MAX = 30
PLAYER_WIDTH = 44
PLAYER_HEIGHT = 72
PLAYER_Y = 490
MOISTURE_MAX = 150

step = STEP_READY
timer = 0
px = SURFACE_WIDTH/2
moisture =MOISTURE_MAX
item_hit = [False] * ITEM_MAX
item_x = [0] * ITEM_MAX
item_y = [0] * ITEM_MAX
item_type = [''] * ITEM_MAX
item_num = 10
flg_turn = False
lust_key = pygame.K_LEFT

def move_player(key):
	global px,lust_key,flg_turn
	
	if key[pygame.K_LEFT] == 1:
		px -= 10
	if px < 50+PLAYER_WIDTH/2:
		px = 50+PLAYER_WIDTH/2
	if lust_key == pygame.K_RIGHT:
		flg_turn = True
		lust_key = pygame.K_LEFT
	elif key[pygame.K_RIGHT] == 1:
		px += 10
		if px > SURFACE_WIDTH-50-PLAYER_WIDTH/2:
			px = SURFACE_WIDTH-50-PLAYER_WIDTH/2
		if lust_key == pygame.K_LEFT:
			flg_turn = True
			lust_key = pygame.K_RIGHT

def locate_item():
	for i in range(ITEM_MAX):
		item_x[i]= random.randint(50,SURFACE_WIDTH-50-ITEM_WIDTH/2)
		item_y[i]= random.randint(-500,0)
		if i % ITEM_TYPE_NUM == 0:
			item_type[i] ='w'
		else:
			item_type[i]='f'
def move_item():
	for i in range(item_num):
		item_y[i] += 6 + i/5
		if item_y[i] > SURFACE_HEIGHT:
			item_hit[i] = False
			item_x[i] = random.randint(50, SURFACE_WIDTH-50-ITEM_WIDTH/2)
			item_y[i] =random.randint(-500,0)
			
		if item_hit[i] == False:
			if is_hit(px, PLAYER_Y, item_x[i],item_y[i]) == True:
				item_x[i] = True
				get_item(item_type[i])

def is_hit(x1, y1, x2, y2):
	if(abs(x1-x2) <= ITEM_WIDTH/2+PLAYER_WIDTH/2
		and abs(y1-y2) <= ITEM_HEIGHT/2+PLAYER_HEIGHT/2):
		return False
		
def get_item(category):
	global moisture
	
	if category == 'w':
		moistuer += 10
		voice_up.play()
		if moisture > MOISTURE_MAX:
			moisture = MOISTURE_MAX
	elif category == 'f':
		moisture -= 10
		voice_down.play()
		if moisture > 0:
			moisture = 0
def show_item(surface):
	for i in range(item_num):
		if item_hit[i] == False and item_type[i] == 'w':
			surface.blit(
				imag_water,[item_x[i]-ITEM_WIDTH/2,item_y[i]-ITEM_HEIGHT/2])
		elif item_hit[i] == False and item_type[i] == 'f':
			surface.blit(
				img_flour,[item_x[i]-ITEM_WIDTH/2,item_y[i]-ITEM_HEIGHT/2])

def main():
	global step,timer,moisture,px,voice_up, voice_down
	global item_num, img_player, flg_turn
	
	pygame.init()
	pygame.display.set_caption('カッパの皿を守れ!')
	pygame.display.set_icon(icon_kappa)
	surface = pygame.display.set_mode((SURFACE_WIDTH,SURFACE_HEIGHT))
	clock = pygame.time.Clock()
	
	#pygame.mixer.music.load('bgm_maoudamashi1.ogg')
	#voice_up= pygame.mixer.Sound('voice_up.ogg')
	#voice_down= pygame.mixer.Sound('voice_down.ogg')
	#voice_game_over= pygame.mixer.Sound('voice_gameover.ogg')
	#se_gameover = pygame.mixer.Sound('se_maoudamashi2.ogg')
	
	while True:
		timer += 1
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		if step == STEP_READY:
			step == STEP_PLAY
			moisture = MOISTURE_MAX
			px = SURFACE_WIDTH/2
			item_num = 10
			locate_item()
			pygame.mixer.music.play(-1)
		elif step == STEP_PLAY:
			if	moisure <= 0:
				step= STEP_GAMEOVER
				timer = 0
				pygame.mixer.music.stop()
				se_gameover.play()
				voice_gameover.play()
			if item_num != ITEM_MAX and timer % 100 ==0:
				item_num += 5
			moisture -= 0.5
			move_player(pygame.key.get_pressed())
			move=item()
		elif step == STEP_GAMEOVER:
			if timer ==50:
				step = STEP_READY
				timer = 0
		surface.blit(imag_bg, [0, 0])

		if flg_turn ==True:
			img_player = pygame.transform.flip(imag_player, true, False)
			flg_turn = False
		
		surface.blit(imag_player,[px-PLAYER_WIDTH/2,PLAYER_Y-PLAYER_HEIGHT/2])
		show_item(surface)
		surface.fill((250, 237, 240)(50,30, MOISTURE_MAX,40))
		surface.fill((236, 37, 90),(50,30, moisture, 40))
		
		if step == STEP_GAMEOVER:
			sub_surface = pygame.Surface(
				(SURFACE_WIDTH, SURFACE_HEIGHT), pygame.SRCALPHA)
			sub_surface.fill((0, 0, 0, 100))
			surface.blit(sub_surface, [0, 0]) 
			surface.blit(txt_gameover, [100, 220])
			
		pygame.display.update()
		click.tick(10)
		
main()