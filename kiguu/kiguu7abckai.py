# -*- coding: utf-8 -*-
import pickle
import random
import os
from playsound import playsound
import sys
own_ichi = 1
Robo63_ichi = 1
filerobo63 = str("robo63")
NoritsuguH = str("shuuekiP")
print("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください")
file = input("input:")
kigou=["♧","♠","♡","♦"]
np=["A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K "]
# スプライトのクラス
own_ichi = 1
Robo63_ichi = 1
filerobo63 = str("robo63")
NoritsuguH = str("shuuekiP")
ts1 = str("trumpsai")
ts2 = str("trumpsai2")
num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
with open(str(ts1) +'.pickle', mode='wb') as f:
		pickle.dump(num2, f)
num3 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num4 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
with open(str(ts2) +'.pickle', mode='wb') as f:
		pickle.dump(num4, f)
def kiguusecond(noritsugu):
	num0= [
		1,-2,3,-4,5,
		-6,7,-8,9,-10,
		11,-12,13
		]
def awase(numC):
	r = random.choice(numC)
	numC.remove(r)
	numC = numC
	r = str(r)
	print("配列のあまりの体力は " + str(len(numC)) + " です。")
	if(int(len(numC))==0):
		print("体力は０になりましてレースを終了いたします。")
		sys.exit()
	else:
		return r
def awase2(ra):
	global num2
	count = 0
	with open(str(ts1)+ '.pickle', 'rb') as f:
			num3 = pickle.load(f)
	num2 = num3
	while True or x> 0:
		r2 = random.choice(num2)
		x = len(num2)
		x = x - 1
		count = count + 1
		print("引いた数は"+str(r2)+"でした。"+str(count)+"回目の数合わせしてます．xの値は"+ str(ra)+"です")
		num2.remove(r2)
		num2 = num2
		if ra == str(r2):
			playsound("icchi.wav")
			print("ふっ、一致したぜ‼")
			with open(str(ts1)+ '.pickle', 'rb') as f:
				num3 = pickle.load(f)
			num3.remove(r2)
			with open(str(ts1)+'.pickle', mode='wb') as f:
				pickle.dump(num3, f)
			break
	
	return count
			
def awase3():
	global num3
	r3 = random.choice(num3)
	num3.remove(r3)
	num3 = num3
	r3 =str(r3)
	return r3
def awase4(rb):
	global num4
	count1 = 0
	with open(str(ts2) + '.pickle', 'rb') as f:
			num5 = pickle.load(f)
	num4 = num5
	while True or x2> 0:
		r4 = random.choice(num4)
		x2 = len(num4)
		x2 = x2 - 1
		count1 = count1 + 1
		print("引いた数は"+str(r4)+"でした。"+str(count1)+"回目の数合わせしてます．xの値は"+ str(rb)+"です")
		num4.remove(r4)
		num4 = num4
		if rb == str(r4):
			playsound("icchirobochan.wav")
			print("一致しました...。")
			with open(str(ts2) + '.pickle', 'rb') as f:
				num5 = pickle.load(f)
			num5.remove(r4)
			with open(str(ts2) +'.pickle', mode='wb') as f:
					pickle.dump(num5, f)
			break
	return count1
	
def starts(file1):
	if os.path.exists("./"+str(file1)+".pickle"):
	    print("ようこそすごろくへ、一着でGoal!!なされるとポイントが加算されます。負けるとポイントが減りますが...。")
	    with open(str(file1) + '.pickle', 'rb') as f:
	        hoyuup2 = pickle.load(f)
	    print("保有ポイントは"+str(hoyuup2)+"です。")
	else:
		print("kiguuシリーズにてゲームをしてファイルを作成してください。")
		end = input("何か押してエンターキーを押してください:")
		if end == end:
			sys.exit()
def bonus(file2,nokori):
	with open(str(file2) + '.pickle', 'rb') as f:
		hoyuup2 = pickle.load(f)
	r = nokori
	r = int(r)
	hoyuup = hoyuup2/(r/4)
	hoyuup = int(hoyuup)
	points = hoyuup2 + hoyuup
	with open(str(file2) +'.pickle', mode='wb') as f:
		pickle.dump(points, f)
	print(file2+"さんには、"+str(hoyuup)+"ボーナスポイントがkiguuのポイントの"+str(hoyuup2)+"ポイントに付加されます。")
def hunobonus(file9,nokori9):
	with open(str(file9) + '.pickle', 'rb') as f:
		hoyuup2 = pickle.load(f)
	r = nokori9
	r = int(r)
	hoyuup = hoyuup2/(r*2)
	hoyuup = int(hoyuup)
	points = hoyuup2 - hoyuup
	with open(str(file9) +'.pickle', mode='wb') as f:
		pickle.dump(points, f)
	with open(str(filerobo63) +'kanri.pickle', mode='wb') as f:
		pickle.dump(hoyuup, f)
	print(file9+"さんには、マイナス"+str(hoyuup)+"ポイントがkiguuのポイントの"+str(hoyuup2)+"ポイントに付加されます。")
def banmen(player1):
	print("OYMGSet...Don!!"+"□"*(own_ichi-1) + player1 +"□"*(30-own_ichi)+"Goal!!")
	print("OYMGSet...Don!!"+"□"*(Robo63_ichi-1) + "Robo63"+"□"*(30-Robo63_ichi)+"Goal!!") #後攻の格差是正
def name():
	string = """kiguuシリーズで作成済みの名前を入れてください。
	初めてのご起動の場合はsetup.pyをsugoroku.pyを実行する前に
	コマンドプロンプト内またはshel内にて実行してください。
	では、お楽しみください。
	kiguu内の名前入力
	:"""
	file = input(string)
	starts(file)
	return file
def kimari(player2):
	print(player2+"さんでよろしいですね")
	a1 = input("Y/N:")
	return a1
def game(player3):
	answer1,bairitsuQ = slottrumpG(file)
	input("Enterを押すと進行致します")
	while answer1 == 'p':
		answer1,bairitsuQ = slottrumpG(file)
		input("Enterを押すと"+player3+"さんサイコロを振れますよ")
		playsound("sai1.mp3")
		global own_ichi
		r2 = awase(num)
		detame = awase2(r2)*bairitsuQ
		print(player3+"さんには、～"+str(detame) + "～の目が出ました")
		own_ichi = own_ichi + int(detame)
		nokori = str(30 - own_ichi)
		nokori = int(nokori)
		if nokori > 0:
			print("あと残り～"+str(nokori)+"～こまです")
		else:
			print("Goal!!しました")
		if own_ichi > 30:
			own_ichi = 30
		banmen(player3)
		if own_ichi == 30:
			print(player3+"一着ボーナス獲得！")
			bonus(player3,nokori2)
			playsound("owariniitashimasu.mp3")
			print("Owari Ni Itashi Masu")
			playsound("sugoroku2.wav")
			playsound("shuuryoushimasu.mp3")
			print("終了します。どうもありがとうございました。もっと、どんどん資の産みを増やそう")
			sys.exit()
		input("Enterを押すとRobo63さんのすごろくが振られます")
		playsound("sai2.mp3")
		global Robo63_ichi
		r63 = awase3()
		detame2 = awase4(r63)*bairitsuQ
		print("Robo63さんには、～"+ str(detame2) +"～の目が出ました")
		Robo63_ichi = Robo63_ichi + int(detame2)
		nokori2 = str(30 - Robo63_ichi)
		nokori2 = int(nokori2)
		if nokori2 > 0:
			print("あと残り～"+ str(nokori2) +"～こまです")
			input("Enterを押すと進行致します")
		else:
			print("Goal!!しました")
			input("Enterを押すと進行致します")
		if Robo63_ichi > 30:
			Robo63_ichi = 30
		banmen(player3)
		if Robo63_ichi ==30:
			print("コンピュータ,一着ボーナス獲得")
			hunobonus(player3,nokori)
			with open(str(filerobo63) + 'kanri.pickle', 'rb') as f:
				hoyuup63 = pickle.load(f)
				hoyuup63 = int(hoyuup63)
				NoritsuguH_hoyuu = int(hoyuup63*1/5)
			with open(str(NoritsuguH) +'charge.pickle', mode='wb') as f:
				pickle.dump(NoritsuguH_hoyuu, f)
			with open(str(NoritsuguH) + '.pickle', 'rb') as f:
				ShuuekiP_NH = pickle.load(f)
			NoritsuguHoshizawa = NoritsuguH_hoyuu + ShuuekiP_NH
			hoyuu63 = int(hoyuup63) - int(NoritsuguH_hoyuu)
			with open(str(NoritsuguH) +'.pickle', mode='wb') as f:
				pickle.dump(NoritsuguHoshizawa, f)
			hoyuupcharge = int(hoyuu63)
			with open(str(filerobo63) +'charge.pickle', mode='wb') as f:
				pickle.dump(hoyuupcharge, f)
			with open(str(filerobo63) + '.pickle', 'rb') as f:
				roboenergy = pickle.load(f)
			roboenergy = roboenergy + hoyuupcharge
			with open(str(filerobo63) +'.pickle', mode='wb') as f:
				pickle.dump(roboenergy, f) 
			playsound("owariniitashimasu.mp3")
			print("Owari Ni Itashi Masu")
			playsound("sugoroku2.wav")
			playsound("shuuryoushimasu.mp3")
			print("終了します。毎度どうもありがとうございました。どんどん増やそうEmotionalPoint‼")
			sys.exit()
def robokashitsuke(name):
	name=str(name)
	robo63="robo63kashitsuke"
	with open(str(robo63) + '.pickle', 'rb') as f:
		robokashi = pickle.load(f)
		robokashi = int(robokashi)
	with open(str(name) + '.pickle', 'rb') as f:
		points = pickle.load(f)
		points = int(points)
	print("素人お笑いです。現在の"+ name +"様の保有ポイントは"+ str(points) +"です")
	print("現在robo63様よりの貸し付けは"+ str(robokashi) + "Pointとなります。")
	print("できる限りの返せる範囲内のpoint(数字入力)を入力してください。")
	if robokashi>0:
		rpoint =input("数値:")
		if rpoint.isdecimal():
			rpoint = str(rpoint)		
			rpoint = int(rpoint)
			if rpoint < robokashi or rpoint == robokashi:
				points = int(points)-int(rpoint)
				points = int(points)
				robokashi = int(robokashi)-int(rpoint)
				robokashi = int(robokashi)
				with open(str(name) +'.pickle', mode='wb') as f:
					pickle.dump(points, f)
				with open('robo63kashitsuke'+'.pickle', mode='wb') as f:
					pickle.dump(robokashi, f)
				print("ただ今のお貸し付けpoint残高は"+str(robokashi)+"pointです。")
				print("お手持ちのpointは"+str(points)+"となります。")
				print("robo63です。助かりました。どうもありがとうございます。")
				if int(robokashi) == 0:
					print("doumoarigatougozaimasu大感謝...。")
					sys.exit()
				else:
					print("omuriwonasarazuni...。またもお願いいたします。ごめんなさいどうもありがとうございます")
					sys.exit()
			else:
				print("数値の入力が正しくありません。")
		else:
			print("pointではありません。終了いたします。すみません。")
	else:
		print("robo63様よりお貸し付けはありません。どうもありがとうございます。")
def sugoroku(a3,player4):
	if a3 == "Y" or a3 == "y":
		print(player4+"さんで決まりました")
		banmen(player4)
		print("すごろく、OYMGSet...Don!!")
		game(player4)
	else:
		playsound("owariniitashimasuka.mp3")
		print("Owari Ni Itashi Masuka？")
		ans = input("Y/N:")
		if ans == "Y" or ans == "y":
			playsound("sugoroku2.wav")
			playsound("shuuryoushimasu.mp3")
			print("終了します。どうもありがとうございました。")
			sys.exit()
		else:
			return "n"
def picture(i1,q1):
	a1=np[i1]
	a1=str(a1)
	c1=kigou[q1]
	c1=str(c1)
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
	num2=[0,1,2,3,4,5,6,7,8,9,10,11,12,]
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
		print(str(cardE)+str(cardF)+"です")
		print(str(cardC)+str(cardD)+"です")
		print(str(cardA)+str(cardB)+"です")
		playsound("DownUpSE.wav")
		print("あたり！！")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			bairitsuP=100
			bairitsu=10
			point = point + hozon1*int(bairitsuP)
			print("やったー！！大当たりっ‼おめでとうございますっ‼なんと100倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'p',bairitsu
	
	elif cardF==cardD:
		print("あたり！！")
		playsound("start2.wav")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			bairitsuP=2
			bairitsu=2
			point = point + hozon1*int(bairitsuP)
			print("2倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'p',bairitsu
	elif cardD==cardB:
		print("あたり！！")
		playsound("start2.wav")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			bairitsuP=2
			bairitsu=2
			point = point + hozon1*int(bairitsuP)
			print("2倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'p',bairitsu
	elif cardF==cardB:
		print("あたり！！")
		playsound("start2.wav")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			bairitsuP=1.5
			bairitsu=1.5
			point = point + hozon1*int(bairitsuP)
			print("1.5倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'p',bairitsu
	elif cardE==cardC:
		print("あたり！！")
		playsound("start2.wav")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			bairitsuP=2
			bairitsu=0.5
			point = point + hozon1*int(bairitsuP)
			print("2倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'p',bairitsu
	elif cardC==cardA:
		print("あたり！！")
		playsound("start2.wav")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			bairitsuP=2
			bairitsu=0.5
			point = point + hozon1*int(bairitsuP)
			print("2倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'p',bairitsu
	elif cardE==cardA:
		print("あたり！！")
		playsound("start2.wav")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			bairitsuP=2
			bairitsu=0.5
			point = point + hozon1*int(bairitsuP)
			print("2倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'p',bairitsu
	elif cardE==cardC==cardA:
		print("あたり！！")
		playsound("start2.wav")
		with open(str(file1)+'.pickle', 'rb') as f:
			hozon1 = pickle.load(f)
			hozon1 = int(hozon1)
			print("現在は"+str(hozon1)+"pointsです。")
			bairitsuP=50
			bairitsu=15
			point = point + hozon1*int(bairitsuP)
			print("50倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'p',bairitsu
	else:
		print("はずれ！！")
		playsound("zannenn.wav")
		with open(str(file1)+'.pickle','rb') as f:
			hozon1 = pickle.load(f)
			print("現在は"+str(hozon1)+"です")
			bairitsuP=(1/3)
			bairitsu=0.7
			point = point + hozon1*bairitsuP
			point=int(point)
			print("獲得なさりましたkiguuポイントにプラスして元のポイントの(1/3)倍の"+str(point)+"ポイントになりました")
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(point, f)
		return 'p',bairitsu


playsound("openingkai.wav")
answer = input("ゲームを始めますか？ please input(y=yes,n=no) :y or n:")
y = "y"
n = "n"
if answer in y:
	player = name()
	a2 = kimari(player)
	answer1,bairits = slottrumpG(file)
	print("happy clafts!! Game Starts!!")
	input("Enterを押すと進行致します")
	while answer1 == 'p':
		j = sugoroku(a2,player)
	while "n" == j:
		player = name()
		a2 = kimari(player)
		j == sugoroku(a2,player)
	sys.exit()
else:	
	playsound("owariniitashimasu.mp3")
	print("Owari Ni Itashi Masu")
	playsound("shuuryoushimasu.mp3")
	playsound("count48.wav")
print("終了します。どうもありがとうございました。")
player = name()
robokashitsuke(player)
playsound("2023natsuba.mp3")
sys.exit()
