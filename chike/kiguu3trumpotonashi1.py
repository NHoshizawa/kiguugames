import random
import pickle
import os
import sys
import pygame
from pygame.locals import *
SCREEN = Rect(0, 0, 600, 800)   #screenのサイズ
class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename,x,y):
	    
	    pygame.sprite.Sprite.__init__(self)
	    self.image = pygame.image.load(filename).convert_alpha()
	    w = self.image.get_width()
	    h = self.image.get_height()
	    self.rect = Rect(x, y, w, h)

def picture(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,):
	print("画像ウインドウを一度クリックしてエンターキーを一度押してお進みください")
	kigou=["c","s","h","d"]
	pygame.init
	c2 = kigou[c1]
	s2 = kigou[s1]
	h2 = kigou[h1]
	d2 = kigou[d1]
	c2 = str(c2)
	s2 = str(s2)
	h2 = str(h2)
	d2 = str(d2)
	screen = pygame.display.set_mode(SCREEN.size)
	ca = Sprite("./"+"kiguu1/"+c2+str(n1)+".png",50, 25)
	cb = Sprite("./"+"kiguu1/"+c2+str(n2)+".png",250, 25)
	cc = Sprite("./"+"kiguu1/"+c2+str(n3)+".png",450, 25)
	sa = Sprite("./"+"kiguu1/"+s2+str(n4)+".png",50, 225)
	sb = Sprite("./"+"kiguu1/"+s2+str(n5)+".png",250, 225)
	sc = Sprite("./"+"kiguu1/"+s2+str(n6)+".png",450, 225)
	ha = Sprite("./"+"kiguu1/"+h2+str(n7)+".png",50, 425)
	hb = Sprite("./"+"kiguu1/"+h2+str(n8)+".png",250, 425)
	hc = Sprite("./"+"kiguu1/"+h2+str(n9)+".png",450, 425)
	da = Sprite("./"+"kiguu1/"+d2+str(n10)+".png",50, 625)
	db = Sprite("./"+"kiguu1/"+d2+str(n11)+".png",250, 625)
	dc = Sprite("./"+"kiguu1/"+d2+str(n12)+".png",450, 625)
	group = pygame.sprite.RenderUpdates()
	group.add(ca)
	group.add(cb)
	group.add(cc)
	group.add(sa)
	group.add(sb)
	group.add(sc)
	group.add(ha)
	group.add(hb)
	group.add(hc)
	group.add(da)
	group.add(db)
	group.add(dc)
	clock = pygame.time.Clock()

	while True:
		clock.tick(30)#30fps
		screen.fill((0, 34, 0))
		group.draw(screen)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit();
				return 0
			elif event.type == KEYDOWN:
				if event.key == K_RETURN: 
					pygame.quit();
					return 0
num0= [
		1,-2,3,-4,5,
		-6,7,-8,9,-10,
		11,-12,13
		]
kigou=["c","s","h","d"]
kigou2=["クローバー","スペード","ハート","ダイヤ"]
#from playsound import playsound
game=0
dpz=0
i=0
print("トランプゲームkiguu copyrighted(produced) by NoritsuguHoshizawa")
print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
file = input("input:")
poi =[1,2,3,4,5,6,7,8,9,10,11,12,13]
poi2 =[1,2,3,4,5,6,7,8,9,10,11,12,13]
pw = random.choice(poi)
pw1 = random.choice(poi2)
#playsound("opening.wav")
n = input("偶数0か奇数1か当たればpointを2倍に please select 0or1注0,1以外は終了:")
n = str(n)
print("行動力気持ちの縺れつり合い人生数理意思決定ディール無の境地!!")
print("kiguu87の数字の読み方愉しみ方。! \r\n9＝’q’uantum or 苦労、8＝破、7=転じて、\r\n６＝無になれる資質、５＝後、4＝資、３＝産、２＝受信、10=おわり\r\n１＝送信、０＝目的や汚(けが)れ、１１＝一方通、\r\n１２＝双方向、１３＝産みを送信,14=資を送信、\r\n１５＝以後、１６＝色、000=おっさん01=老いる\r\nDX=13X just a waiting momentum.666=6＊3=18=3618寒いわ(笑)")
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
		with open(str(file4) + '.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
		hozon1 = int(hozon1)
		hoyuup = hozon2 + hozon1
		hoyuup = int(hoyuup)
		with open(str(file4) +'.pickle', mode='wb') as f:
			pickle.dump(hoyuup, f)
		print("保有ポイントは"+str(hoyuup)+"です。")
		os.remove("./"+str(file4)+"kanri.pickle")
		end = input("何か押してエンターキーを押してください:")
		if end == end:
			sys.exit()
	else:
		with open(str(file4) + '.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
		hozon1 = int(hozon1)
		hoyuup = hozon1
		hoyuup = int(hoyuup)
		with open(str(file4) +'.pickle', mode='wb') as f:
			pickle.dump(hoyuup, f)
		print("保有ポイントは"+str(hoyuup)+"です。")
		end = input("何か押してエンターキーを押してください:")
		if end == end:
			sys.exit()

#def picture(i1,q1):
	np=["A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K "]
	a1=np[i1]
	c1=kigou[q1]
	xy=["",
		"----------",
		"|        |",
		     a1     ,
		"|        |",
		     c1     ,
		"|        |",
		     a1     ,
		"|        |",
		"----------",
		""
		]
		
	for o in xy[0:]:
		print(o)
def trump():
	num= [
	1,-2,3,-4,5,
	-6,7,-8,9,-10,
	11,-12,13
	]
	rx = random.choice(num)
	ra = str(rx)
	rd = abs(rx)
	ra = int(ra)
	num.remove(ra)
	rx2 = random.choice(num)
	rb = str(rx2)
	re = abs(rx2)
	rb =int(rb)
	num.remove(rb)
	rx3 = random.choice(num)
	rc = str(rx3)
	rf = abs(rx3)
	rc = int(rc)
	return ra,rb,rc,rd,re,rf
def tensuu(i,tr,tr2,tr3):
	print("奇数は正で偶数は負になります。" + str(tr))
	print("奇数は正で偶数は負になります。"+str(tr2))	
	print("奇数は正で偶数は負になります。"+str(tr3))
	x = tr+tr2+tr3
	y = abs(x)
	y = int(y)
	if y <= 13 and y!= tr and y!= tr2 and y!= tr3:
		print(str(y) + "合計値の絶対値です。")
		if y != tr != tr2 != tr3:
			return y
	else:
		print(str(y) + "合計値の絶対値です。")
		print("合計値が13以上なので,13以下にします。")
		y = y - 13
		if y <= 13:
			if y != tr != tr2 != tr3:
				print(str(y) + "合計値の絶対値です。") 
				return y
			else:
				y = 0
				print("合計値の値が既に出ており"+str(y)+"の無効になります")
				return y
		else:
			y = y - 13
			if y != tr != tr2 != tr3:
				print(str(y) + "値は合計値の絶対値です。") 
				return y
			else:
				y = 0
				print("合計値の値が既に出ており"+ str(y) +"の無効になります")
				return y

def cal(i,trc,trc2,trc3):
	c2 = 0
	c2 = tensuu(i,trc,trc2,trc3)
	kig=kigou2[i]
	kg = c2 % 2
	kg = int(kg)
	if kg == 0:
		c2=-c2
		print(kig+ "偶数なので値がマイナスになります。"+str(c2))
		return c2
	else:
		c2=c2
		print(kig+"奇数なので値がプラスになります。"+str(c2))
		return c2

def kiguu(file5):
	if os.path.exists("./"+str(file5)+".pickle"): #前回からの続き
		i1=0
		i2=1
		i3=2
		i4=3
		c2 = trump()
		ca=c2[0]
		cb=c2[1]
		cc=c2[2]
		ten = cal(i1,ca,cb,cc)
		c = str(ten)
		c= int(c)
		cd=c2[3]
		ce=c2[4]
		cf=c2[5]
		s2 = trump()
		sa=s2[0]
		sb=s2[1]
		sc=s2[2]
		ten2=cal(i2,sa,sb,sc)
		s=str(ten2)
		s=int(s)
		sd=s2[3]
		se=s2[4]
		sf=s2[5]
		h2 = trump()
		ha=h2[0]
		hb=h2[1]
		hc=h2[2]
		ten3=cal(i3,ha,hb,hc)
		h=str(ten3)
		h=int(h)
		hd=h2[3]
		he=h2[4]
		hf=h2[5]
		d2 = trump()
		da=d2[0]
		db=d2[1]
		dc=d2[2]
		ten4=cal(i4,da,db,dc)
		print("トランプウインドウにマウスカーソルでアクティブにした後Escキーか閉じるボタンをご確認の上でトランプのウインドウをお閉じください。")
		d=str(ten4)
		d=int(d)
		dd=d2[3]
		de=d2[4]
		df=d2[5]
		picture(cd,ce,cf,sd,se,sf,hd,he,hf,dd,de,df)
		o = (c)+(s)+(h)+(d)
		q = abs(o)
		q = int(q)
		if q == 0:
			print("kiguuの結果が0pointなのでinputとoutputバランスよく!今日、一日気を休めてね")
			return 'e'
		else:
			print('トランプの４種類の各々の３枚の合計が')
			print(str(q)+'pointの結果となり。奇数か?、偶数か?、当たりかどうか、結果へ進みます。')
			pz = q % 2
			pz = int(pz)
			if pz == 0 and n == '0' or pz == 0 and n == '1':
				if n == '0': 
					p1 = q*2	
					print("PointGet...")
					#playsound("guuatari.wav")
					print("偶数であたり、2倍に!!")
					print(str(p1)+"point outputへ気持ちの器量に!!")
					point = p1
					#playsound("music0kai.wav")
					with open(str(file5) + '.pickle', 'rb') as f:
						hozon1 = pickle.load(f)
					point = point + hozon1
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
				else:
					print("PointGet...そのままになります")
					#playsound("guuhazure.wav")
					print(str(q)+"pointをoutputへ気持ちの器量に!!")
					point = q
					#playsound("music0kai.wav")
					with open(str(file5) + '.pickle', 'rb') as f:
						hozon1 = pickle.load(f)
					point = point + hozon1
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
			elif pz == 1 and n == '0' or pz== 1 and n == '1':
				if n == '1':
					p1 = q*2
					print("PointGet...")
					#playsound("kisuuatari.wav")
					print("奇数であたり、2倍に!!")
					print(str(p1)+"pointをinputへ気持ちの器量に!!")
					point = p1
					with open(str(file5) + '.pickle', 'rb') as f:
						hozon1 = pickle.load(f)
					point = point + hozon1
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
				else:
					print("PointGet...そのままになります")
					#playsound("kisuuhazure.wav")
					print(str(q)+"pointをinputへ気持ちの器量に!!")
					point = q 
					#playsound("music0kai.wav")
					with open(str(file5) + '.pickle', 'rb') as f:
						hozon1 = pickle.load(f)
					point = point + hozon1
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
			else:
				print("kiguu終了")
				point = 0
				#playsound("music0kai.wav")
				with open(str(file5) + '.pickle', 'rb') as f:
					hozon1 = pickle.load(f)
				point = point + hozon1
				with open(str(file5) +'.pickle', mode='wb') as f:
					pickle.dump(point, f)
				return 'e'
	else:
		i1=0
		i2=1
		i3=2
		i4=3
		c2 = trump()
		ca=c2[0]
		cb=c2[1]
		cc=c2[2]
		ten=cal(i1,ca,cb,cc)
		c=int(ten)
		
		s2 = trump()
		sa=s2[0]
		sb=s2[1]
		sc=s2[2]
		ten2=cal(i2,sa,sb,sc)
		s=int(ten2)
		h2 = trump()
		ha=h2[0]
		hb=h2[1]
		hc=h2[2]
		ten3=cal(i3,ha,hb,hc)
		h=int(ten3)
		d2 = trump()
		da=d2[0]
		db=d2[1]
		dc=d2[2]
		ten4=cal(i4,da,db,dc)
		d=int(ten4)
		picture(ca,cb,cc,sa,sb,sc,ha,hb,hc,da,db,dc,i1,i2,i3,i4)
		o = c+s+h+d
		q = abs(o)
		q = int(q)
		if q == 0:
			print('kiguuの結果が0pointなのでinputとoutputバランスよく!今日、一日気を休めてね')
			return 'e'
		else:
			print('トランプの４種類の各々の３枚の合計が')
			print(str(q)+'pointの結果となり。奇数か?、偶数か?、当たりかどうか、結果へ進みます。')
			pz = q % 2
			pz = int(pz)
			if pz == 0 and n == '0' or pz == 0 and n == '1':
				if n == '0': 
					p1 = q*2	
					print("PointGet...")
					#playsound("guuatari.wav")
					print("偶数であたり、2倍に!!")
					print(str(p1)+"point outputへ気持ちの器量に!!")
					point = p1
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
				else:
					print("PointGet...そのままになります")
					#playsound("guuhazure.wav")
					print(str(q)+"pointをoutputへ気持ちの器量に!!")
					point = q
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
			elif pz == 1 and n == '0' or pz== 1 and n == '1':
				if n == '1':
					p1 = q*2
					print("PointGet...")
					#playsound("kisuuatari.wav")
					print("奇数であたり、2倍に!!")
					print(str(p1)+"pointをinputへ気持ちの器量に!!")
					point = p1
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
				else:
					print("PointGet...そのままになります")
					#playsound("kisuuhazure.wav")
					print(str(q)+"pointをinputへ気持ちの器量に!!")
					point = q 
					##playsound("music0kai.wav")
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
			else:
				print("kiguu終了")
				point = 0
				#playsound("music0kai.wav")
				with open(str(file5) + '.pickle', 'rb') as f:
					hozon1 = pickle.load(f)
				point = point + hozon1
				with open(str(file5) +'.pickle', mode='wb') as f:
					pickle.dump(point, f)
				return 'e'
				
def ru(file6):
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
						#playsound("DownUpSE.wav")
						print("値は"+str(points)+"でした。当たり!!"+str(point8)+"bet分が"+str(r)+"倍の"+str(point8a)+"pointになりました")
						print(str(point8a) +"pointになりました。持ちpointはbet分が差し引かれた保有point+(bet point×2)")
						print("外れたら運用分は0ポイントになります。")
						with open(str(file6) +'kiguu.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						with open(str(file6) + 'kanri.pickle', mode='wb') as f:
							pickle.dump(point8a, f)
						return 'p'
					else:
						#playsound("zannenn.wav")
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
						#playsound("DownUpSE.wav")
						print("値は"+str(points)+"でした。当たり!!"+str(point8)+"bet分が"+str(r)+"倍になり、bet point控除後のpointに加算されます")
						print(str(point8a) +"pointになります。現在持ちpointはbet分が差し引かれた保有point+(bet point×2)" )
						print("外れたら運用分は0ポイントになります。")
						with open(str(file6) +'kiguu.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						with open(str(file6) + 'kanri.pickle', mode='wb') as f:
							pickle.dump(point8a, f)
						return 'p'
					else:
						#playsound("zannenn.wav")
						print("値は"+str(points)+"でした。当たりにならず!!")
						point8 = 0
						with open(str(file6) +'kiguu.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						with open(str(file6) + 'kanri.pickle', mode='wb') as f:
							pickle.dump(point8, f)
						print(str(point1)+"pointになります。")
						return 'e'
				else:
					#playsound("even.wav")
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
			#playsound("ending.wav")
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
			bet = input("持ちpointの中からいくらbetしますか？:")
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
				if bet <= int(point1) and bet >= 0:
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
								#playsound("DownUpSE.wav")
								print("値は"+str(points)+"でした。当たり!!"+ str(bet)+"bet分が"+str(r)+"倍になり持ちポイントは" + str(point8) + "になりました")
								print("外れたら運用分は0ポイントになります。")
								with open(str(file6) +'kiguu.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f)
								return 'p'
							else:
								#playsound("zannenn.wav")
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
								#playsound("DownUpSE.wav")
								print("値は"+str(points)+"でした。当たり!!"+ str(bet)+"bet分が"+str(r)+"倍になり持ちポイントは" + str(point8) + "になりました")
								print("外れたら運用分は0ポイントになります。")
								with open(str(file6) +'kiguu.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f)
								return 'p'
							else:
								#playsound("zannenn.wav")
								print("値は"+str(points)+"でした。当たりにならず!!")
								point8 = 0
								with open(str(file6) +'kiguu.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f)
								print(str(point2)+"pointになります。")
								return 'e'
						else:
							#playsound("even.wav")
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
			#playsound("ending.wav")
			with open(str(file6) +'kiguu.pickle', mode='wb') as f:
				pickle.dump(point1, f)
			return 'e'
		else:
			print("選択は無効となりpointは保存されます。")
			with open(str(file6) +'kiguu.pickle', mode='wb') as f:
				pickle.dump(point1, f)
			return 'p'
answer = kiguu(file)
while answer == 'p':
	answer = ru(file)
end(file)
