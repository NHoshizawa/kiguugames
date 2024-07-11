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
playsound("opening.wav")
n = input("偶数0か奇数1か当たればpointを2倍に please select 0or1注0,1以外は終了:")
n = str(n)
print("行動力気持ちの縺れつり合い人生数理意思決定ディール無の境地!!")
print("kiguu87の数字の読み方愉しみ方。\9＝’q’uantum or 苦労、8＝破、7=転じて、\６＝無、５＝後、4＝資、３＝産、２＝受信、10=おわり\１＝送信、０＝目的や汚(けが)れ、１１＝一方通、\１２＝双方向、１３＝産みを送信,14=資を送信、\１５＝以後、１６＝色、000=おっさん01=老いる\DX=13Xなり、666=6＊3=18=3618寒いわ(笑)")

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

def kiguu(file5):
	if os.path.exists("./"+str(file5)+".pickle"): #前回からの続き
		c=int(cal(0))
		s=int(cal(1))
		h=int(cal(2))
		d=int(cal(3))
		o=c+s+h+d
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
					print("偶数であたり、2倍に!!")
					print(str(p1)+"point outputへ気持ちの器量に!!")
					point = p1
					with open(str(file5) + '.pickle', 'rb') as f:
						hozon1 = pickle.load(f)
					point = point + hozon1
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
				else:
					print("PointGet...そのままになります")
					playsound("guuhazure.wav")
					print(str(q)+"pointをoutputへ気持ちの器量に!!")
					point = q
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
					playsound("kisuuatari.wav")
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
					playsound("kisuuhazure.wav")
					print(str(q)+"pointをinputへ気持ちの器量に!!")
					point = q 
					with open(str(file5) + '.pickle', 'rb') as f:
						hozon1 = pickle.load(f)
					point = point + hozon1
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
			else:
				print("kiguu終了")
				point = 0
				with open(str(file5) + '.pickle', 'rb') as f:
					hozon1 = pickle.load(f)
				point = point + hozon1
				with open(str(file5) +'.pickle', mode='wb') as f:
					pickle.dump(point, f)
				return 'e'
	else:
		c=int(cal(0))
		s=int(cal(1))
		h=int(cal(2))
		d=int(cal(3))
		o=c+s+h+d
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
					playsound("guuatari.wav")
					print("偶数であたり、2倍に!!")
					print(str(p1)+"point outputへ気持ちの器量に!!")
					point = p1
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
				else:
					print("PointGet...そのままになります")
					playsound("guuhazure.wav")
					print(str(q)+"pointをoutputへ気持ちの器量に!!")
					point = q
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
			elif pz == 1 and n == '0' or pz== 1 and n == '1':
				if n == '1':
					p1 = q*2
					print("PointGet...")
					playsound("kisuuatari.wav")
					print("奇数であたり、2倍に!!")
					print(str(p1)+"pointをinputへ気持ちの器量に!!")
					point = p1
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
				else:
					print("PointGet...そのままになります")
					playsound("kisuuhazure.wav")
					print(str(q)+"pointをinputへ気持ちの器量に!!")
					point = q 
					with open(str(file5) +'.pickle', mode='wb') as f:
						pickle.dump(point, f)
					return 'p'
			else:
				print("kiguu終了")
				playsound("music0.wav")
				point = 0
				with open(str(file5) + '.pickle', 'rb') as f:
					hozon1 = pickle.load(f)
				point = point + hozon1
				with open(str(file5) +'.pickle', mode='wb') as f:
					pickle.dump(point, f)
				return 'e'
				
def du(file6):
	if os.path.exists("./"+str(file6)+"kanri.pickle"): 
		point1 = kanri(file6)
		point8 = kanriup(file6)
		print("2倍運用挑戦しませんか？")
		answer = input("please input(y=yes,n=no) :y or n:")
		y = "y"
		n = "n"
		if answer in y:
			print("現在の" + str(point1) + "ポイントの半分より持ちpoint数字内から無作為に選んだの値は")
			print("high(1) or low(2)か?")
			number = input("select,1 or 2:")
			number = int(number)
			point1 = abs(point1) 
			points = random.randint(0,point1)
			horl = points - point1 / 2
			if number == 1 or number == 2:
				if horl > 0:
					answer = 1
					if number == answer:
						point8 = int(point8) * 2
						playsound("2bai.wav")
						print("当たり!!"+ str(point8)+"pointになりました")
						print(str(point8) +"pointになりました。持ちpointはbet分が差し引かれた保有point+(bet point×2)")
						print("外れたら運用分は0ポイントになります。")
						with open(str(file6) +'.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						with open(str(file6) + 'kanri.pickle', mode='wb') as f:
							pickle.dump(point8, f)
						return 'p'
					else:
						playsound("zannenn.wav")
						print("当たりにならず!!")
						point8 = 0
						with open(str(file6) +'.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						with open(str(file6) + 'kanri.pickle', mode='wb') as f:
							pickle.dump(point8, f) 
						return 'e'
				elif horl < 0:
					answer = 2
					if number == answer:
						point8 = int(point8) * 2
						playsound("2bai.wav")
						game=int(point8)
						print("当たり!!" + str(game) + "bet分が2倍になり、bet point控除後のpointに加算されます")
						print(str(point8) +"pointになります。現在持ちpointはbet分が差し引かれた保有point+(bet point×2)" )
						print("外れたら運用分は0ポイントになります。")
						with open(str(file6) +'.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						with open(str(file6) + 'kanri.pickle', mode='wb') as f:
							pickle.dump(point8, f)
						return 'p'
					else:
						playsound("zannenn.wav")
						print("当たりにならず!!")
						point8 = 0
						with open(str(file6) +'.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						with open(str(file6) + 'kanri.pickle', mode='wb') as f:
							pickle.dump(point8, f)
						print(str(point1)+"pointになります。")
						return 'e'
				else:
					playsound("even.wav")
					print("even!!")
					point1 = int(point1)
					with open(str(file6) +'.pickle', mode='wb') as f:
						pickle.dump(point1, f)
					return 'p'
			else:
				print("選択しなおしてね")
				with open(str(file6) +'.pickle', mode='wb') as f:
					pickle.dump(point1, f)
				return 'p' 
		elif answer in n:
			playsound("ending.wav")
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
		print("2倍運用挑戦しませんか？")
		answer = input("please input(y=yes,n=no) :y or n:")
		y = "y"
		n = "n"
		if answer in y:
			print("現在のポイントは" + str(point1) + "ポイントあります")
			bet = input("持ちpointの中からいくらbetしますか？:")
			bet = str(bet)
			ans = "bet".isalpha()
			ans = str(ans)
			if ans == 'true':
				print("数字を入力してください")
				with open(str(file6) +'.pickle', mode='wb') as f:
					pickle.dump(point1, f)
				return 'p'
			else:
				bet = int(bet)
				if bet <= int(point1) and bet >= 0:
					point2 = point1 - bet
					print("現在の" + str(point1) + "ポイントの半分より持ちpoint数字内から無作為に選んだの値は")
					print("high(1) or low(2)か?")
					number = input("select,1 or 2:")
					number = int(number)
					point1 = abs(point1) 
					points = random.randint(0,point1)
					horl = points - point1 / 2
					if number == 1 or number == 2:
						if horl > 0:#33111
							answer = 1
							if number == answer:
								point8 = int(bet) * 2
								playsound("2bai.wav")
								print("当たり!!"+ str(bet)+"bet分が2倍になり持ちポイントは" + str(point8) + "になりました")
								print("外れたら運用分は0ポイントになります。")
								with open(str(file6) +'.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f)
								return 'p'
							else:
								playsound("zannenn.wav")
								print("当たりにならず!!") 
								point8 = 0
								with open(str(file6) +'.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f) 
								return 'e'
						elif horl < 0:
							answer = 2
							if number == answer:
								point8 = int(bet) * 2
								point8 = int(point8)
								point1 = point1 - int(bet)
								playsound("2bai.wav")
								print("当たり!!"+ str(bet)+"bet分が2倍になり持ちポイントは" + str(point8) + "になりました")
								print("外れたら運用分は0ポイントになります。")
								with open(str(file6) +'.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f)
								return 'p'
							else:
								playsound("zannenn.wav")
								print("当たりにならず!!")
								point8 = 0
								with open(str(file6) +'.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f)
								print(str(point1)+"pointになります。")
								return 'e'
						else:
							playsound("even.wav")
							print("even!!")
							point1 = int(point1)
							p2 = point1
							with open(str(file6) +'.pickle', mode='wb') as f:
								pickle.dump(point1, f)
							return 'p'
					else:
						print("選択しなおしてね")
						with open(str(file6) +'.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						return 'p' 
		elif answer in n:
			playsound("ending.wav")
			with open(str(file6) +'.pickle', mode='wb') as f:
				pickle.dump(point1, f)
			return 'e'
		else:
			print("選択は無効となりpointは保存されます。")
			with open(str(file6) +'.pickle', mode='wb') as f:
				pickle.dump(point1, f)
			return 'p'
while True:
	playsound("count48.wav")
	answer = kiguu(file)
	while answer == 'p':
		answer = du(file)
	end(file)