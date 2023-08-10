import random
import pickle
import os
import sys
num0= [
		1,-2,3,-4,5,
		-6,7,-8,9,-10,
		11,-12,13
		]
kigou=["クローバー","スペード","ハート","ダイヤ"]
from playsound import playsound

i=0
print("トランプゲームkiguu produced by NoritsuguHoshizawa")
print("point保存する新規Point口座名(新規ファイル名)または、既存のPoint口座名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")	
file = input("input:")
playsound("opening.wav")
n = input("偶数0か奇数1か当たればpointを2倍に please select 0or1注0,1以外は終了:")
n = str(n)
print("行動力気持ちの縺れつり合い人生数理意思決定ディール無の境地!!")
print("kiguu87の数字の読み方愉しみ方。\9＝’q’uantum or 苦労、8＝破、7=転じて、\６＝無、５＝後、4＝資、３＝産、２＝受信、10=おわり\１＝送信、０＝目的や汚(けが)れ、１１＝一方通、\１２＝双方向、１３＝産みを送信,14=資を送信、\１５＝以後、１６＝色、000=おっさん01=老いる\DX=13Xなり、666=6＊3=18=3618寒いわ(笑)")
def kanri(file1):
	with open(str(file1) + '.pickle', 'rb') as f:
		hozon1 = pickle.load(f)
	return hozon1
def kanri2():
	print("現在の保有ポイント合計は...")
	with open(str(file) + '.pickle', 'rb') as f:
		hozon1 = pickle.load(f)
	kiguu87point = hozon1
	total = int(kiguu87point) + ten
	print("合計で" + str(total) + "ポイントです")	
def picture(i1,q1):
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
		
def tensuu(i):
		
	num= [
	1,-2,3,-4,5,
	-6,7,-8,9,-10,
	11,-12,13
	]
	r = random.choice(num)
	picture(num0.index(r),i)
	print("奇数は正で偶数は負になります。" + str(r))
	num.remove(r)
	num1=num
	r2=random.choice(num1)
	picture(num0.index(r2),i)
	print("奇数は正で偶数は負になります。"+str(r2))	
	num1.remove(r2)
	num2=num1
	r3 = random.choice(num2)
	picture(num0.index(r3),i)
	print("奇数は正で偶数は負になります。"+str(r3))
	x = r+r2+r3
	y = abs(x)
	y = int(y)
	if y <= 13 and y!= r and y!= r2 and y!= r3:
		print(str(y) + "合計値の絶対値です。")
		if y != r != r2 != r3:
			return y
	else:
		print(str(y) + "合計値の絶対値です。")
		print("合計値が13以上なので,13以下にします。")
		y = y - 13
		if y <= 13:
			if y != r != r2 != r3:
				print(str(y) + "合計値の絶対値です。") 
				return y
			else:
				y = 0
				print("合計値の値が既に出ており"+str(y)+"の無効になります")
				return y
		else:
			y = y - 13
			if y != r != r2 != r3:
				print(str(y) + "合計値の絶対値です。") 
				return y
			else:
				y = 0
				print("合計値の値が既に出ており"+ str(y) +"の無効になります")
				return y

def cal(i):
	c2 = 0
	c2 = tensuu(i)
	c2 = int(c2)
	kig=kigou[i]
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

def kiguu():
	c=int(cal(0))
	s=int(cal(1))
	h=int(cal(2))
	d=int(cal(3))
	o=c+s+h+d
	q = abs(o)
	q = int(q)
	if q == 0:
		print('kiguuの結果が0pointなのでinputとoutputバランスよく!今日、一日気を休めてね')
		return 0
	else:
		print('トランプの４種類の各々の３枚の合計が')
		print(str(q)+'pointの結果となり。奇数か?、偶数か?、当たりかどうか、結果へ進みます。')
		p1 = q % 2
		p1 = int(p1)
		if p1 == 0 and n == '0' or p1 == 0 and n == '1':
			if n == '0': 
				p = q*2	
				print("PointGet...")
				playsound("guuatari.wav")
				print("偶数であたり、2倍に!!")
				print(str(p)+"point outputへ気持ちの器量に!!")
				point = p
				playsound("music0.wav")
				return point
			else:
				print("PointGet...そのままになります")
				playsound("kisuuhazure.wav")
				print(str(q)+"pointをoutputへ気持ちの器量に!!")
				point = q
				playsound("music0.wav")
				return point
		elif p1 == 1 and n == '0' or p1== 1 and n == '1':
			if n == '1':
				p = q*2
				print("PointGet...")
				playsound("kisuuatari.wav")
				print("奇数であたり、2倍に!!")
				print(str(p)+"pointをinputへ気持ちの器量に!!")
				point = p
				playsound("music0.wav")
				return point
			else:
				print("PointGet...そのままになります")
				playsound("guuhazure.wav")
				print(str(q)+"pointをinputへ気持ちの器量に!!")
				point = q 
				playsound("music0.wav")
				return point
		else:
			print("kiguu終了")
			point = 0
			playsound("music0.wav")
			return point
			

def doubleup(point7,hoyuu):
	hoyuu = kanriq(file)
	hoyuu = int(hoyuu)
	if point7 == 0:
		with open(str(file) +'.pickle', mode='wb') as f:
			pickle.dump(point7, f)
		return 'e'
	else:
		print("保有point運用2倍にしますか？select y or n 注意y,n以外は終了")
		y = "y"
		n = "n"
		yn = input("please select y or n:")
		if yn in y:
			bet = input("持ちpointの中からいくらbetしますか？:")
			bet = str(bet)
			ans = "bet".isalpha()
			ans = str(ans)
			if ans == 'true':
				print("数字を入力してください")
				with open(str(file) +'.pickle', mode='wb') as f:
					pickle.dump(point7, f)
				return 'p'
			else:
				bet = int(bet)
				if bet <= int(point7) and bet >= 0:
					point9 = point7 - bet
					print("持ちpointの半分より持ちpoint数字内から無作為に選んだの値は,")
					print("high(1) or low(2)か?")
					number = input("select,1 or 2:")
					number = int(number)
					point7 = abs(point7)
					points = random.randint(0,point7)
					horl = points - point7 / 2
					if number == 1 or number == 2:
						if horl > 0:
							answer = 1
							if number == answer:
								point8 = int(bet) * 2
								point7 = point7 - int(bet) + point8
								point8 = int(point8)
								playsound("2bai.wav")
								print("当たり!!"+ str(bet) +"bet分が2倍になり、bet point控除後のpointに加算されます")
								print(str(point7) +"pointになりました。持ちpointはbet分が差し引かれた保有point+(bet point×2)")
								with open(str(file) +'.pickle', mode='wb') as f:
									pickle.dump(point7, f)
								return 'p'
							else:
								playsound("zannnenn.wav")
								print("当たりにならず!!")
								point9 = int(point9) 
								print(str(point9)+"pointになります。")
								with open(str(file) +'.pickle', mode='wb') as f:
									pickle.dump(point9, f)
								return 'p'
						elif horl < 0:
							answer = 2
							if number == answer:
								point8 = int(bet) * 2
								point8 = int(point8)
								point7 = point7 - int(bet) + point8
								playsound("2bai.wav")
								print("当たり!!" + str(bet) + "bet分が2倍になり、bet point控除後のpointに加算されます")
								print(str(point7) +"pointになります。現在持ちpointはbet分が差し引かれた保有point+(bet point×2)" )
								with open(str(file) +'.pickle', mode='wb') as f:
									pickle.dump(point7, f)
								return 'p'
							else:
								playsound("zannnenn.wav")
								print("当たりにならず!!")
								point9 = int(point9)
								print(str(point9)+"pointになります。")
								with open(str(file) +'.pickle', mode='wb') as f:
									pickle.dump(point9, f)
								return 'p'
						else:
							playsound("even.wav")
							print("even!!")
							point7 = int(point7)
							with open(str(file) +'.pickle', mode='wb') as f:
								pickle.dump(point7, f)
							return 'p'
					else:
						print("選択しなおしてね")
						with open(str(file) +'.pickle', mode='wb') as f:
							pickle.dump(point7, f)
						return 'p' 
				else:
					return 'p'
		elif yn in n:
			playsound("ending.wav")
			print("pointは保存されます。")
			if os.path.exists("./robo63.pickle"):
				print("robo63だよ。よく我慢できたな、きみをおうえんするよ！！")
				with open('robo63.pickle', 'rb') as f:
					pointrobo63 = pickle.load(f)
				robo63nokimochi = int(pointrobo63) * (1/10)
				robo63nokimochi = int (robo63nokimochi)
				pointrobo63= int(pointrobo63) * (9/10)
				with open('robo63.pickle', mode='wb') as f:
					pickle.dump(pointrobo63, f)
				print(str(robo63nokimochi)+"ポイントを分けてあげるよ。慈善レースに...。")
				point7 = int(robo63nokimochi) + int(point7)
				point7 = int(point7)
				with open(str(file) +'.pickle', mode='wb') as f:
					pickle.dump(point7, f)
				return 'e'
			else:
				return 'e'
		else:
			print("選択は無効となりpointはそのままになります。")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point7, f)
			return 'p'
def doubleup2(point7,hoyuu = 0):
	if point7 == 0:
		with open(str(file) +'.pickle', mode='wb') as f:
			pickle.dump(point7, f)
		return 'e'
	else:
		print(str(point7)+"pointから")
		print("保有point運用2倍にしますか？select y or n 注意y,n以外は終了")
		y = "y"
		n = "n"
		yn = input("please select y or n:")
		if yn in y:
			print("持ち"+str(point7)+"pointの中から、いくら保有point運用2倍にしたいですか？")
			bet = input("持ちpointの中からいくらbetしますか？:")
			bet = str(bet)
			ans = "bet".isalpha()
			ans = str(ans)
			if ans == 'true':
				print("数字を入力してください")
				with open(str(file) +'.pickle', mode='wb') as f:
					pickle.dump(point7, f)
				return 'p'
			else:
				bet = int(bet)
				if bet <= int(point7) and bet >= 0:
					point9 = point7 - bet
					print("持ちpointの半分より持ちpoint数字内から無作為に選んだの値は,")
					print("high(1) or low(2)か?")
					number = input("select,1 or 2:")
					number = int(number)
					point7 = abs(point7)
					points = random.randint(0,point7)
					horl = points - point7 / 2
					if number == 1 or number == 2:
						if horl > 0:
							answer = 1
							if number == answer:
								point8 = int(bet) * 2
								point7 = point7 - int(bet) + point8
								point8 = int(point8)
								playsound("2bai.wav")
								print("当たり!!"+ str(bet) +"bet分が2倍になり、bet point控除後のpointに加算されます")
								print(str(point7) +"pointになりました。持ちpointはbet分が差し引かれた保有point+(bet point×2)")
								with open(str(file) +'.pickle', mode='wb') as f:
									pickle.dump(point7, f)
								return 'p'
							else:
								playsound("zannnenn.wav")
								print("当たりにならず!!")
								point9 = int(point9) 
								print(str(point9)+"pointになります。")
								with open(str(file) +'.pickle', mode='wb') as f:
									pickle.dump(point9, f)
								return 'p'
						elif horl < 0:
							answer = 2
							if number == answer:
								point8 = int(bet) * 2
								point8 = int(point8)
								point7 = point7 - int(bet) + point8
								playsound("2bai.wav")
								print("当たり!!" + str(bet) + "bet分が2倍になり、bet point控除後のpointに加算されます")
								print(str(point7) +"pointになります。現在持ちpointはbet分が差し引かれた保有point+(bet point×2)" )
								with open(str(file) +'.pickle', mode='wb') as f:
									pickle.dump(point7, f)
								return 'p'
							else:
								playsound("zannnenn.wav")
								print("当たりにならず!!")
								point9 = int(point9)
								print(str(point9)+"pointになります。")
								with open(str(file) +'.pickle', mode='wb') as f:
									pickle.dump(point9, f)
								return 'p'
						else:
							playsound("even.wav")
							print("even!!")
							point7 = int(point7)
							with open(str(file) +'.pickle', mode='wb') as f:
								pickle.dump(point7, f)
							return 'p'
					else:
						print("選択しなおしてね")
						with open(str(file) +'.pickle', mode='wb') as f:
							pickle.dump(point7, f)
						return 'p'
		elif yn in n:
			playsound("ending.wav")
			print("pointは保存されます。")
			if os.path.exists("./robo63.pickle"):
				print("robo63だよ。よく我慢できたな、きみをおうえんするよ！！")
				with open(str(robo63) + '.pickle', 'rb') as f:
					pointrobo63 = pickle.load(f)
				robo63nokimochi = int(pointrobo63) * (1/10)
				robo63nokimochi = int(robo63nokimochi)
				pointrobo63= int(pointrobo63) * (9/10)
				with open('robo63.pickle', mode='wb') as f:
					pickle.dump(pointrobo63, f)
				print(str(robo63nokimochi)+"ポイントを分けてあげるよ。慈善レースにでも...。")
				point7 = int(robo63nokimochi) + int(point7)
				point7 = int(point7)
				with open(str(file) +'.pickle', mode='wb') as f:
					pickle.dump(point7, f)
				with open('robo63.pickle', mode='wb') as f:
					pickle.dump(point7, f)
				return 'e'
			else:
				return 'e'
		else:
			print("選択は無効となりpointは保存されます。")
			with open(str(file) +'.pickle', mode='wb') as f:
				pickle.dump(point7, f)
			return 'p'			
def kanriq(file1):
	with open(str(file1) + '.pickle', 'rb') as f:
		hozon1 = pickle.load(f)
	return hozon1
	

if os.path.exists("./"+str(file)+".pickle"):
	ten = kiguu()
	ten = int(ten)
	hoyuu2 = kanri(file)
	hoyuu2 = int(hoyuu2)
	kanri2()
	ten = ten + hoyuu2
	object = doubleup(ten,hoyuu2)
	while object == 'p':
		dp = kanriq(file)
		hoyuu3 = dp
		object = doubleup(dp,hoyuu3)
	end1 = input("終了は何か入力してenterを押してください:")
	if end1 == end1:
		sys.exit()
else:
	ten = kiguu()
	ten=int(ten)
	hoyuu2 = 0
	hoyuu2 = int(hoyuu2)
	print("現在の保有ポイント合計は...")
	total = hoyuu2 + ten
	print("合計で" + str(total) + "ポイントです")	
	ten = ten + hoyuu2
	object = doubleup2(ten,hoyuu2)
	while object == 'p':
		dp = kanriq(file)
		hoyuu3 = int(dp)
		object = doubleup(dp,hoyuu3)
	end1 = input("終了は何か入力してenterを押してください:")
	if end1 == end1:
		sys.exit()
