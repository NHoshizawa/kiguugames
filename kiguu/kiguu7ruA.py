# -*- coding: utf-8 -*-
import pickle
import pygame
import random
import os
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
def kanriup(file1):
    with open(str(file1) + 'kanri.pickle', 'rb') as f:
        hozon2 = pickle.load(f)
    hozon2 = int(hozon2)
    return hozon2
    
def kanri(file2):
    with open(str(file2) + '.pickle', 'rb') as f:
        hozon1 = pickle.load(f)
    hozon1 = int(hozon1)
    return hozon1
    
def kanri2(file3):
    print("現在の保有ポイント合計は...")
    with open(str(file3) + '.pickle', 'rb') as f:
        hozon1 = pickle.load(f)
    hozon1 = int(hozon1)
    total = int(point)
    print("合計で" + str(total) + "ポイントです")
def end(file4):
	if os.path.exists("./"+str(file4)+"kanri.pickle"): 
	    with open(str(file4) + 'kanri.pickle', 'rb') as f:
	        hozon2 = pickle.load(f)
	    hozon2 = int(hozon2)
	    with open(str(file4) + 'kiguu.pickle', 'rb') as f:
	        hozon1 = pickle.load(f)
	    hozon1 = int(hozon1)
	    hoyuup = hozon2 + hozon1
	    hoyuup = int(hoyuup)
	    if os.path.exists("./"+str(file4)+".pickle"):
	        with open(str(file4) + '.pickle', 'rb') as f:
	            hoyuup2 = pickle.load(f)
	        hoyuup2 = hoyuup2 + hoyuup
	        with open(str(file4) +'.pickle', mode='wb') as f:
	            pickle.dump(hoyuup2, f)
	        print("保有ポイントは"+str(hoyuup2)+"です。")
	        os.remove("./"+str(file4)+"kanri.pickle")
	        end = input("何か押してエンターキーを押してください:")
	        if end == end:
	            sys.exit()
	    else:
	        with open(str(file4) +'.pickle', mode='wb') as f:
	            pickle.dump(hoyuup, f)
	        print("保有ポイントは"+str(hoyuup)+"です。")
	        os.remove("./"+str(file4)+"kanri.pickle")
	        end = input("何か押してエンターキーを押してください:")
	        if end == end:
	            sys.exit()
	else:
	    with open(str(file4) + 'kiguu.pickle', 'rb') as f:
	        hozon1 = pickle.load(f)
	    hozon1 = int(hozon1)
	    hoyuup = hozon1
	    hoyuup = int(hoyuup)
	    if os.path.exists("./"+str(file4)+".pickle"):
	        with open(str(file4) + '.pickle', 'rb') as f:
	            hoyuup2 = pickle.load(f)
	        hoyuup2 = hoyuup2 + hoyuup
	        with open(str(file4) +'.pickle', mode='wb') as f:
	            pickle.dump(hoyuup2, f)
	        print("保有ポイントは"+str(hoyuup2)+"です。")
	        end = input("何か押してエンターキーを押してください:")
	        if end == end:
	            sys.exit()
	    else:
	        with open(str(file4) +'.pickle', mode='wb') as f:
	            pickle.dump(hoyuup, f)
	        print("保有ポイントは"+str(hoyuup)+"です。")
	        end = input("何か押してエンターキーを押してください:")
	        if end == end:
	            sys.exit()

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
def ru(file6): #random upのruとなります。
    if os.path.exists("./"+str(file6)+"kanri.pickle"): 
        point1 = kanri(file6)
        point8 = kanriup(file6)
        point7 = int(point1)+int(point8)
        print("つづけて、1～5倍運用挑戦しませんか？")
        answer = input("please input(y=yes,n=no) :y or n:")
        y = "y"
        n = "n"
        if answer in y:
            r2 = random.randint(1,3)
            r2 = int(r2)
            point1 = abs(point1)
            r3 = point7 * r2/3
            r3 = int(r3)
            print("現在の" + str(point7) + "ポイントの3分の"+str(r2)+",つまり"+str(r3)+"より持ちpoint数字内から無作為に選んだの値は")
            print("ランダムに出た、数字の傾向は、")
            for i in range(1,5):
                points = random.randint(0,point7)
                print(str(points))
            print("となります。次の数字は")
            points = random.randint(0,point7)
            print("high(1) or low(2)か?")
            number = input("choice,1 or 2:")
            number = int(number)
            horl = points - point7 * r2/3
            if number == 1 or number == 2:
                if horl > 0:
                    answer = 1
                    if number == answer:
                        r = random.randint(1,5)
                        r = int(r)
                        print("今回は当たれば"+str(r)+"倍になります")
                        point8a = int(point8) * r
                        print("値は"+str(points)+"でした。当たり!!"+str(point8)+"bet分が"+str(r)+"倍の"+str(point8a)+"pointになりました")
                        print(str(point8a) +"pointになりました。持ちpointはbet分が差し引かれた保有point+(bet point×2)")
                        print("外れたら運用分は0ポイントになります。")
                        with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                            pickle.dump(point1, f)
                        with open(str(file6) + 'kanri.pickle', mode='wb') as f:
                            pickle.dump(point8a, f)
                        return 'p'
                    else:
                        print("値は"+str(points)+"でした。当たりにならず!!")
                        point8 = 0
                        with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                            pickle.dump(point1, f)
                        with open(str(file6) + 'kanri.pickle', mode='wb') as f:
                            pickle.dump(point8, f) 
                        return 'e'
                elif horl < 0:
                    answer = 2
                    if number == answer:
                        r = random.randint(1,5)
                        r = int(r)
                        point8a = int(point8) * r
                        print("値は"+str(points)+"でした。当たり!!"+str(point8)+"bet分が"+str(r)+"倍になり、bet point控除後のpointに加算されます")
                        print(str(point8a) +"pointになります。現在持ちpointはbet分が差し引かれた保有point+(bet point×2)" )
                        print("外れたら運用分は0ポイントになります。")
                        with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                            pickle.dump(point1, f)
                        with open(str(file6) + 'kanri.pickle', mode='wb') as f:
                            pickle.dump(point8a, f)
                        return 'p'
                    else:
                        print("値は"+str(points)+"でした。当たりにならず!!")
                        point8 = 0
                        with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                            pickle.dump(point1, f)
                        with open(str(file6) + 'kanri.pickle', mode='wb') as f:
                            pickle.dump(point8, f)
                        print(str(point1)+"pointになります。")
                        return 'e'
                else:
                    print("値は"+str(points)+"でした。even!!")
                    point1 = int(point1)
                    with open(str(file6) +'.pickle', mode='wb') as f:
                        pickle.dump(point1, f)
                    return 'p'
            else:
                print("選択しなおしてね")
                with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                    pickle.dump(point1, f)
                return 'p' 
        elif answer in n:
            with open(str(file6) + 'kanri.pickle', mode='wb') as f:
                pickle.dump(point8, f)
            with open(str(file6) +'.pickle', mode='wb') as f:
                pickle.dump(point1, f)
            return 'e'
        else:
            print("選択は無効となりpointは保存されます。")
            with open(str(file6) +'.pickle', mode='wb') as f:
                pickle.dump(point1, f)
            return 'p'
    else:
        point1 = kanri(file6)
        point7 = int(point1)
        print("1～5倍運用挑戦しませんか？")
        answer = input("please input(y=yes,n=no) :y or n:")
        y = "y"
        n = "n"
        if answer in y:
            print("kiguuポイントは" + str(point1) + "ポイントあります")
            bet = input("持ちpointの中からいくら運用しますか？:")
            bet = str(bet)
            ans = "bet".isalpha()
            ans = str(ans)
            if ans == 'true':
                print("数字を入力してください")
                with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                    pickle.dump(point1, f)
                return 'p'
            else:
                bet = int(bet)
                if bet <= int(point1) and bet > 0:
                    point2 = point1 - bet
                    r2 = random.randint(1,3)
                    r2 = int(r2)
                    point1 = abs(point1) 
                    r3 = point7 * r2/3
                    r3 = int(r3)
                    print("現在の" + str(point7) + "ポイントの3分の"+str(r2)+",つまり"+str(r3)+"より持ちpoint数字内から無作為に選んだの値は")
                    print("ランダムに出た、数字の傾向は、")
                    for i in range(1,5):
                        points = random.randint(0,point7)
                        print(str(points))
                    print("となります。次の数字は")
                    points = random.randint(0,point7)
                    print("high(1) or low(2)か?")
                    number = input("choice,1 or 2:")
                    number = int(number)
                    horl = points - point7 * r2/ 3
                    if number == 1 or number == 2:
                        if horl > 0:
                            answer = 1
                            if number == answer:
                                r = random.randint(1,5)
                                r = int(r)
                                print("今回は当たれば"+str(r)+"倍になります")
                                point8 = int(bet) * r
                                print("値は"+str(points)+"でした。当たり!!"+ str(bet)+"bet分が"+str(r)+"倍になり持ちポイントは" + str(point8) + "になりました")
                                print("外れたら運用分は0ポイントになります。")
                                with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                                    pickle.dump(point2, f)
                                with open(str(file6) + 'kanri.pickle', mode='wb') as f:
                                    pickle.dump(point8, f)
                                return 'p'
                            else:
                                print("値は"+str(points)+"でした。当たりにならず!!") 
                                point8 = 0
                                with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                                    pickle.dump(point2, f)
                                with open(str(file6) + 'kanri.pickle', mode='wb') as f:
                                    pickle.dump(point8, f) 
                                return 'e'
                        elif horl < 0:
                            answer = 2
                            if number == answer:
                                r = random.randint(1,5)
                                r = int(r)
                                point8 = int(bet) * r
                                point8 = int(point8)
                                point1 = point1 - int(bet)
                                print("値は"+str(points)+"でした。当たり!!"+ str(bet)+"bet分が"+str(r)+"倍になり持ちポイントは" + str(point8) + "になりました")
                                print("外れたら運用分は0ポイントになります。")
                                with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                                    pickle.dump(point2, f)
                                with open(str(file6) + 'kanri.pickle', mode='wb') as f:
                                    pickle.dump(point8, f)
                                return 'p'
                            else:
                                print("値は"+str(points)+"でした。当たりにならず!!")
                                point8 = 0
                                with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                                    pickle.dump(point2, f)
                                with open(str(file6) + 'kanri.pickle', mode='wb') as f:
                                    pickle.dump(point8, f)
                                print(str(point2)+"pointになります。")
                                return 'e'
                        else:
                            print("値は"+str(points)+"でした。even!!")
                            point1 = int(point1)
                            p2 = point1
                            with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                                pickle.dump(point1, f)
                            return 'p'
                    else:
                        print("選択しなおしてね")
                        with open(str(file6) +'.pickle', mode='wb') as f:
                            pickle.dump(point1, f)
                        return 'p' 
        elif answer in n:
            with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                pickle.dump(point1, f)
            return 'e'
        else:
            print("選択は無効となりpointは保存されます。")
            with open(str(file6) +'kiguu.pickle', mode='wb') as f:
                pickle.dump(point1, f)
            return 'p'
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
				point = point + hozon1*10000
				print("やったー！！大当たりっ‼おめでとうございますっ‼なんと1000倍の"+str(point)+"ポイントになりました")
				print("key's return to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
			answer = ru(file)
			while answer == 'p':
				answer = ru(file)
			end(file)
		
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
				point = point + hozon1*40
				print("20倍の"+str(point)+"ポイントになりました")
				print("key's return to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
			answer = ru(file)
			while answer == 'p':
				answer = ru(file)
			end(file)
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
				point = point + hozon1*30
				print("10倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
			answer = ru(file)
			while answer == 'p':
				answer = ru(file)
			end(file)
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
				point = point + hozon1*20
				print("15倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
			answer = ru(file)
			while answer == 'p':
				answer = ru(file)
			end(file)
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
				point = point + hozon1*5
				print("15倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
			answer = ru(file)
			while answer == 'p':
				answer = ru(file)
			end(file)
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
				point = point + hozon1*5
				print("15倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
			answer = ru(file)
			while answer == 'p':
				answer = ru(file)
			end(file)
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
				point = point + hozon1*5
				print("15倍の"+str(point)+"ポイントになりました")
				print("key's Enter to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
			answer = ru(file)
			while answer == 'p':
				answer = ru(file)
			end(file)
		if cardE==cardC==cardA:
			print(cardE+cardF+"です")
			print(cardC+cardD+"です")
			print(cardA+cardB+"です")
			playsound("music0.wav")
			print("あたり！！")
			print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
			file = input("input:")
			with open(str(file)+'.pickle', 'rb') as f:
				hozon1 = pickle.load(f)
				hozon1 = int(hozon1)
				print("現在は"+str(hozon1)+"pointsです。")
				point = point + hozon1*500
				print("やったー！！大当たりっ‼おめでとうございますっ‼なんと1000倍の"+str(point)+"ポイントになりました")
				print("key's return to picture's window click please after keyDown at stop ← twice push key's Enter at end.")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point, f)
			answer = ru(file)
			while answer == 'p':
				answer = ru(file)
			end(file)
		
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
				point = point + hozon1*0.25
				print("獲得なさりましたkiguuポイントにプラスして元のポイントの0.25倍の"+str(point)+"ポイントになりました")
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

