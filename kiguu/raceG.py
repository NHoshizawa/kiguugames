# -*- coding: utf-8 -*-
import pickle
import pygame
import random
from pygame.locals import *
import sys
G_SIZE = 50
G2_SIZE =100
SCREEN = Rect(0, 0, 800, 800)   # 画面サイズ
num = [10,20,30,40,50,60,70,80,90,100]
card1=["c","d","h","s"]
card2=["1","2","3","4","5","6","7","8","9","10","11","12","13"]

# スプライトのクラス
class Sprite(pygame.sprite.Sprite):
    # スプライトを作成(画像ファイル名, 位置xy(x, y), 速さvxy(vx, vy), 回転angle)
    def __init__(self, filename, xy, vxy, angle=0):
        x, y = xy
        vx, vy = vxy
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (G_SIZE, G2_SIZE))
        if angle != 0: self.image = pygame.transform.rotate(self.image, angle)
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect = Rect(x, y, w, h)
        self.vx = vx
        self.vy = vy
        self.angle = angle
    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        # 壁と衝突時の処理(跳ね返り)
        if self.rect.left < 0 or self.rect.right > SCREEN.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCREEN.height:
            self.vy = -self.vy
        # 壁と衝突時の処理(壁を超えないように)
        self.rect = self.rect.clamp(SCREEN)
def slottrumpG():
	point = 10
	screen = pygame.display.set_mode(SCREEN.size)
	x,y,x2,y2,x3,y3,cardA,cardB,cardC,cardD,cardE,cardF = hikisuu()
	group = pygame.sprite.RenderUpdates()
	key = pygame.key.get_pressed()
	
	if key[pygame.K_LEFT]==1:
		if cardF==str(3):
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			print("あたり！！")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file) + '.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				print(hozon1)
				point = point + hozon1*100
				print("100倍の"+str(point)+"ポイントになりました。")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
		else:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			print("はずれ！！")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file) + '.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				point = point + hozon1 - 10
				print(str(point)+"ポイントになりました。")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
		n=1
		while (n):
			pygame.init()
			for event in pygame.event.get():
			# 終了用のイベント処理
				if event.type == QUIT:          # 閉じるボタンが押されたとき
					pygame.quit()
				if event.type == KEYDOWN:       # キーを押したとき
					if event.key == K_ESCAPE:   # Escキーが押されたとき
					 	pygame.quit()
			screen = pygame.display.set_mode(SCREEN.size)
	
			playerA = Sprite("./"+"kiguu1/"+cardA+cardB+".png",(0, 300), (0, 0), 0)
			playerB = Sprite("./"+"kiguu1/"+cardC+cardD+".png",(0, 200), (0, 0), 0)
			playerC = Sprite("./"+"kiguu1/"+cardE+cardF+".png",(0, 100), (0, 0), 0)
			group = pygame.sprite.RenderUpdates()
			group.add(playerA)
			group.add(playerB)
			group.add(playerC)
			clock = pygame.time.Clock()
			while(2):
				clock.tick(30)
				screen.fill((0, 63, 0)) 
				group.update()
				group.draw(screen)
				pygame.display.update()
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						return 0
					if event.type == KEYDOWN:
						if event.key == K_RETURN:
							pygame.quit()
							return 0
def hikisuu():
	x = random.choice(num)
	y = 10
	x2 = random.choice(num)
	y2 = 10
	x3 = random.choice(num)
	y3 = 1
	cardA = random.choice(card1)
	cardB = random.choice(card2)
	cardC = random.choice(card1)
	cardD = random.choice(card2)
	cardE = random.choice(card1)
	cardF = random.choice(card2)
	return x,y,x2,y2,x3,y3,cardA,cardB,cardC,cardD,cardE,cardF
def doing():
	global file1
	pygame.init()
	clock = pygame.time.Clock()
	clock.tick(30)  # フレームレート(30fps)
	while (3):
		pygame.init()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				n=0
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					pygame.quit()
					sys.exit()
					n=0
		screen = pygame.display.set_mode(SCREEN.size)
		x,y,x2,y2,x3,y3,cardA,cardB,cardC,cardD,cardE,cardF = hikisuu()
		playerA = Sprite("./"+"kiguu1/"+cardA+cardB+".png",(x, 300), (x, y), 0)
		x,y,x2,y2,x3,y3,cardA,cardB,cardC,cardD,cardE,cardF = hikisuu()
		playerB = Sprite("./"+"kiguu1/"+cardC+cardD+".png",(x2, 200), (x2, y2), 0)
		x,y,x2,y2,x3,y3,cardA,cardB,cardC,cardD,cardE,cardF = hikisuu()
		playerC = Sprite("./"+"kiguu1/"+cardE+cardF+".png",(x3, 100), (x3, y3), 0)
		group = pygame.sprite.RenderUpdates()
		group.add(playerA)
		group.add(playerB)
		group.add(playerC)
		screen.fill((0, 63, 0))
		# 画面の背景色
		# スプライトグループを更新
		group.update()
		# スプライトを描画
		group.draw(screen)
		# 画面更新 
		pygame.display.update()
		# イベント処理
		slottrumpG()
	pygame.quit()
doing()

