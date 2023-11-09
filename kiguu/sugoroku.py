import os
import random
import sys
import pickle
own_ichi = 1
Robo63_ichi = 1
filerobo63 = str("robo63")
NoritsuguH = str("shuuekiP")
ts1 = str("trumpsai")
ts2 = str("trumpsai2")
from playsound import playsound
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
def awase():
	global num
	r = random.choice(num)
	num.remove(r)
	num = num
	r = str(r)
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
	while True:
		input("Enterを押すと"+player3+"さんサイコロを振れますよ")
		playsound("sai1.mp3")
		global own_ichi
		r2 = awase()
		detame = awase2(r2)
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
			break
		input("Enterを押すとRobo63さんのすごろくが振られます")
		playsound("sai2.mp3")
		global Robo63_ichi
		r63 = awase3()
		detame2 = awase4(r63)
		print("Robo63さんには、～"+ str(detame2) +"～の目が出ました")
		Robo63_ichi = Robo63_ichi + int(detame2)
		nokori2 = str(30 - Robo63_ichi)
		nokori2 = int(nokori2)
		if nokori2 > 0:
			print("あと残り～"+ str(nokori2) +"～こまです")
		else:
			print("Goal!!しました")
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
			break
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
playsound("opening.wav")
answer = input("ゲームを始めますか？ please input(y=yes,n=no) :y or n:")
y = "y"
n = "n"
if answer in y:
	player = name()
	a2 = kimari(player)
	j = sugoroku(a2,player)
	while "n" == j:
		player = name()
		a2 = kimari(player)
		j == sugoroku(a2,player)
else:	
	playsound("owariniitashimasu.mp3")
	print("Owari Ni Itashi Masu")
	playsound("shuuryoushimasu.mp3")
	playsound("count48.wav")
print("終了します。どうもありがとうございました。")
player = name()
robokashitsuke(player)
playsound("2023natsuba.mp3")
