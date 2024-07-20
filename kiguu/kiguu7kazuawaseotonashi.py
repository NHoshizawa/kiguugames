# -*- coding: utf-8 -*-
import pickle
import random
import os
#from playsound import playsound
import sys
print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
file = input("input:")
kigou=["クローバー","スペード","ハート","ダイヤ"]
np=["A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K "]
# スプライトのクラス
def picture(i1,q1):
	a1=np[i1]
	c1=kigou[q1]
	xy=["----------",
		"|        |",
		     a1     ,
		"|        |",
		     c1     ,
		"|        |",
		     a1     ,
		"|        |",
		"----------",
		]
		
	for o in xy[0:]:
		print(o)
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
def hikisuu():
	num=[0,1,2,3]
	num2=[0,1,2,3,4,5,6,7,8,9,10,11,12]
	cardA = random.choice(num)
	cardA=int(cardA)
	cardB = random.choice(num2)
	cardB=int(cardB)
	cardC = random.choice(num)
	cardC=int(cardC)
	cardD = random.choice(num2)
	cardD=int(cardD)
	cardE = random.choice(num)
	cardE=int(cardE)
	cardF = random.choice(num2)
	cardF=int(cardF)
	return cardA,cardB,cardC,cardD,cardE,cardF		
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
def slottrumpG(file1):
	cardA,cardB,cardC,cardD,cardE,cardF = hikisuu()
	picture(cardF,cardE)
	picture(cardD,cardC)
	picture(cardB,cardA)
	n1=cardF
	n2=cardD
	n3=cardB
	point1=kiguu(n1)
	point2=kiguu(n2)
	point3=kiguu(n3)
	point = point1+point2+point3
	point = abs(point)
	if cardF==cardD==cardB:
		print(cardE+cardF+"です")
		print(cardC+cardD+"です")
		print(cardA+cardB+"です")
		#playsound("DownUpSE.wav")
		print("あたり！！")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			point = point + hozon1*1000
			print("やったー！！大当たりっ‼おめでとうございますっ‼なんと1000倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'e'
	
	elif cardF==cardD:
		print("あたり！！")
		#playsound("start2.wav")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			point = point + hozon1*20
			print("20倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'e'
	elif cardD==cardB:
		print("あたり！！")
		#playsound("start2.wav")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			point = point + hozon1*10
			print("10倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'e'
	elif cardF==cardB:
		print("あたり！！")
		#playsound("start2.wav")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			point = point + hozon1*15
			print("15倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'e'
	else:
		print("はずれ！！")
		#playsound("zannenn.wav")
		with open(str(file1)+'.pickle','rb') as f:
			hozon1 = pickle.load(f)
			print("現在は"+str(hozon1)+"です")
			point = point + hozon1*0.5
			print("獲得なさりましたkiguuポイントにプラスして元のポイントの0.5倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'e'
def ru(file6):
	if os.path.exists("./"+str(file6)+"kanri.pickle"): 
		point1 = kanri(file6)
		point8 = kanriup(file6)
		point7 = int(point1)+int(point8)
		print("random倍運用挑戦しませんか？")
		answer = input("please input(y=yes,n=no) :y or n:")
		y = "y"
		n = "n"
		if answer in y:
			r2 = random.randint(1,3)
			r2 = int(r2)
			point1 = abs(point1) 
			points = random.randint(0,point7)
			print("現在の" + str(point7) + "ポイントの3分の"+str(r2)+"より持ちpoint数字内から無作為に選んだの値は")
			print("high(1) or low(2)か?")
			number = input("select,1 or 2:")
			number = int(number)
			horl = points - point7 * r2/3
			if number == 1 or number == 2:
				if horl > 0:
					answer = 1
					if number == answer:
						r = random.randint(0,100)
						r = int(r)
						point8 = int(point8) * r
						#playsound("2bai.wav")
						print("値は"+str(points)+"でした。当たり!!" +str(r)+"倍の"+str(point8)+"pointになりました")
						print(str(point8) +"pointになりました。持ちpointはbet分が差し引かれた保有point+(bet point×2)")
						print("外れたら運用分は0ポイントになります。")
						with open(str(file6) +'.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						with open(str(file6) + 'kanri.pickle', mode='wb') as f:
							pickle.dump(point8, f)
						return 'p'
					else:
						#playsound("zannenn.wav")
						print("値は"+str(points)+"でした。当たりにならず!!")
						point8 = 0
						with open(str(file6) +'.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						with open(str(file6) + 'kanri.pickle', mode='wb') as f:
							pickle.dump(point8, f) 
						return 'e'
				elif horl < 0:
					answer = 2
					if number == answer:
						r = random.randint(0,100)
						r = int(r)
						game=int(point8)
						point8 = int(point8) * r
						#playsound("2bai.wav")
						print("値は"+str(points)+"でした。当たり!!" + str(game) + "bet分が"+str(r)+"倍になり、bet point控除後のpointに加算されます")
						print(str(point8) +"pointになります。現在持ちpointはbet分が差し引かれた保有point+(bet point×2)" )
						print("外れたら運用分は0ポイントになります。")
						with open(str(file6) +'.pickle', mode='wb') as f:
							pickle.dump(point1, f)
						with open(str(file6) + 'kanri.pickle', mode='wb') as f:
							pickle.dump(point8, f)
						return 'p'
					else:
						#playsound("zannenn.wav")
						print("値は"+str(points)+"でした。当たりにならず!!")
						point8 = 0
						with open(str(file6) +'.pickle', mode='wb') as f:
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
				with open(str(file6) +'.pickle', mode='wb') as f:
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
		print("random倍運用挑戦しませんか？")
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
					r2 = random.randint(1,3)
					r2 = int(r2)
					point1 = abs(point1) 
					points = random.randint(0,point7)
					print("現在の" + str(point7) + "ポイントの3分の"+str(r2)+"より持ちpoint数字内から無作為に選んだの値は")
					print("high(1) or low(2)か?")
					number = input("select,1 or 2:")
					number = int(number)
					horl = points - point7 * r2/ 3
					if number == 1 or number == 2:
						if horl > 0:
							answer = 1
							if number == answer:
								r = random.randint(0,100)
								r = int(r)
								point8 = int(bet) * r
								#playsound("2bai.wav")
								print("値は"+str(points)+"でした。当たり!!"+ str(bet)+"bet分が"+str(r)+"倍になり持ちポイントは" + str(point8) + "になりました")
								print("外れたら運用分は0ポイントになります。")
								with open(str(file6) +'.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f)
								return 'p'
							else:
								#playsound("sadmusic.wav")
								print("値は"+str(points)+"でした。当たりにならず!!") 
								point8 = 0
								with open(str(file6) +'.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f) 
								return 'e'
						elif horl < 0:
							answer = 2
							if number == answer:
								r = random.randint(0,100)
								r = int(r)
								point8 = int(bet) * r
								point8 = int(point8)
								point1 = point1 - int(bet)
								#playsound("2bai.wav")
								print("値は"+str(points)+"でした。当たり!!"+ str(bet)+"bet分が"+str(r)+"倍になり持ちポイントは" + str(point8) + "になりました")
								print("外れたら運用分は0ポイントになります。")
								with open(str(file6) +'.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f)
								return 'p'
							else:
								#playsound("zannenn.wav")
								print("値は"+str(points)+"でした。当たりにならず!!")
								point8 = 0
								with open(str(file6) +'.pickle', mode='wb') as f:
									pickle.dump(point2, f)
								with open(str(file6) + 'kanri.pickle', mode='wb') as f:
									pickle.dump(point8, f)
								print(str(point1)+"pointになります。")
								return 'e'
						else:
							#playsound("even.wav")
							print("値は"+str(points)+"でした。even!!")
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
			#playsound("ending.wav")
			with open(str(file6) +'.pickle', mode='wb') as f:
				pickle.dump(point1, f)
			return 'e'
		else:
			print("選択は無効となりpointは保存されます。")
			with open(str(file6) +'.pickle', mode='wb') as f:
				pickle.dump(point1, f)
			return 'p'
answer = slottrumpG(file)
while answer == 'p':
	answer = slottrumpG(file)
end(file)
