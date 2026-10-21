# -*- coding: utf-8 -*-
import pickle
import pygame
import random
from playsound import playsound
from pygame.locals import *
import sys
G_SIZE = 50
G2_SIZE =100
SCREEN = Rect(0, 0, 300, 300)   # 画面サイズ
num = [10,20,30,40,50,60,70,80,90,100]
card1=["c","d","h","s"]
card2=["1","2","3","4","5","6","7","8","9","10","11","12","13"]
print("push key left(←)stop loop")
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
def kiguu(i):
	c2 = i
	c2 = int(c2)
	kg = c2 % 2
	kg = int(kg)
	if kg == 0:
		c2=-c2
		return c2
	else:
		c2=c2
		return c2
def slottrumpG():
	screen = pygame.display.set_mode(SCREEN.size)
	x,y,x2,y2,x3,y3,cardA,cardB,cardC,cardD,cardE,cardF = hikisuu()
	n1=cardF
	n2=cardD
	n3=cardB
	point1=kiguu(n1)
	point2=kiguu(n2)
	point3=kiguu(n3)
	point = point1+point2+point3
	point = abs(point)
	group = pygame.sprite.RenderUpdates()
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]==1:
		if cardF==cardD==cardB:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			playsound("DownUpSE.wav")
			print("あたり！！")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file)+'.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				hozon1 = int(hozon1)
				print("現在は"+str(hozon1)+"pointsです。")
				point = point + hozon1*1000
				print("やったー！！大当たりっ‼おめでとうございますっ‼なんと1000倍の"+str(point)+"ポイントになりました")
				print("key's return to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
		
		elif cardF==cardD:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			print("あたり！！")
			playsound("start2.wav")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file)+'.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				hozon1 = int(hozon1)
				print("現在は"+str(hozon1)+"pointsです。")
				point = point + hozon1*2
				print("2倍の"+str(point)+"ポイントになりました")
				print("key's return to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
		elif cardD==cardB:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			print("あたり！！")
			playsound("start2.wav")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file)+'.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				hozon1 = int(hozon1)
				print("現在は"+str(hozon1)+"pointsです。")
				point = point + hozon1*2
				print("2倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
		elif cardF==cardB:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			print("あたり！！")
			playsound("start2.wav")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file)+'.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				hozon1 = int(hozon1)
				print("現在は"+str(hozon1)+"pointsです。")
				point = point + hozon1*2
				print("2倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
		elif cardE==cardC:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			print("あたり！！")
			playsound("start2.wav")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file)+'.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				hozon1 = int(hozon1)
				print("現在は"+str(hozon1)+"pointsです。")
				point = point + hozon1*2
				print("2倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
		elif cardC==cardA:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			print("あたり！！")
			playsound("start2.wav")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file)+'.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				hozon1 = int(hozon1)
				print("現在は"+str(hozon1)+"pointsです。")
				point = point + hozon1*2
				print("2倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
		elif cardE==cardA:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			print("あたり！！")
			playsound("start2.wav")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file)+'.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				hozon1 = int(hozon1)
				print("現在は"+str(hozon1)+"pointsです。")
				point = point + hozon1*2
				print("2倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
		elif cardE==cardC==cardA:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			print("あたり！！")
			playsound("start2.wav")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file)+'.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				hozon1 = int(hozon1)
				print("現在は"+str(hozon1)+"pointsです。")
				point = point + hozon1*500
				print("500倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
		else:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			print("はずれ！！")
			playsound("zannenn.wav")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file)+'.pickle','rb') as f:
				hozon1 = pickle.load(f)
				print("現在は"+str(hozon1)+"です")
				point = point + hozon1*(0.001)
				point=int(point)
				print("獲得なさりましたkiguuポイントにプラスして元のポイントの0.01倍の"+str(point)+"ポイントになりました")
				print("key's return to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
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
	
			playerA = Sprite("./"+"kiguu1/"+cardA+cardB+".png",(200,150), (0, 0), 0)
			playerB = Sprite("./"+"kiguu1/"+cardC+cardD+".png",(150,150), (0, 0), 0)
			playerC = Sprite("./"+"kiguu1/"+cardE+cardF+".png",(100,150), (0, 0), 0)
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
	x = 10
	y = random.choice(num)
	x2 = 10
	y2 = random.choice(num)
	x3 = 1
	y3 = random.choice(num)
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
		playerA = Sprite("./"+"kiguu1/"+cardA+cardB+".png",(200,y), (x, y), 0)
		x,y,x2,y2,x3,y3,cardA,cardB,cardC,cardD,cardE,cardF = hikisuu()
		playerB = Sprite("./"+"kiguu1/"+cardC+cardD+".png",(150,y2 ), (x2, y2), 0)
		x,y,x2,y2,x3,y3,cardA,cardB,cardC,cardD,cardE,cardF = hikisuu()
		playerC = Sprite("./"+"kiguu1/"+cardE+cardF+".png",(100,y3 ), (x3, y3), 0)
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

