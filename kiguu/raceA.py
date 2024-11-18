import os
import random
import sys
import pickle
playerA=str("playerA")
playerB=str("playerB")
playerC=str("playerC")
playerD=str("playerD")
Aenergy=0
Benergy=0
Cenergy=0
Denergy=0
hoyuuA=0
hoyuuB=0
hoyuuC=0
hoyuuD=0
hoyuupA=0
hoyuupB=0
hoyuupC=0
hoyuupD=0
ichiA0=0
ichiB0=0
ichiC0=0
ichiD0=0
filePlayerA=str("playerA")
filePlayerB=str("playerB")
filePlayerC=str("playerC")
filePlayerD=str("playerD")
playerA1=str("playerA")
playerB1=str("playerB")
playerC1=str("playerC")
playerD1=str("playerD")
numA=0
numB=0
ichiABCD=0
own_ichi = 0
ichiA=0
ichiB=0
ichiC=0
ichiD=0
Robo63_ichi = 0
filerobo63 = str("robo63")
NoritsuguH = str("shuuekiP")
tsnum1 = str("trumpsai")
tsnum2 = str("trumpsai2")
tsnum3 = str("trumpsai3")
tsnum4 = str("trumpsai4")
tsnum5 = str("trumpsai5")
tsnum6 = str("trumpsai6")
from playsound import playsound
num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
with open(str(tsnum1) +'.pickle', mode='wb') as f:
		pickle.dump(num2, f)
num3 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num4= [1,2,3,4,5,6,7,8,9,10,11,12,13]
num5 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num6 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num7 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num8 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num9 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num10 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num11 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num12 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#awase2用
numPLA = [1,2,3,4,5,6,7,8,9,10,11,12,13]
numPLB = [1,2,3,4,5,6,7,8,9,10,11,12,13]
numPLC = [1,2,3,4,5,6,7,8,9,10,11,12,13]
numPLD = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#awase用
numPLA1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
numPLB1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
numPLC1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
numPLD1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
player="ふっ、一致したぜ‼"
playerSE="icchi.wav"
robo63="一致しました...。"
robo63SE="icchirobochan.wav"
with open(str(tsnum2) +'.pickle', mode='wb') as f:
		pickle.dump(num4, f)
with open(str(tsnum3) +'.pickle', mode='wb') as f:
		pickle.dump(num6, f)
with open(str(tsnum4) +'.pickle', mode='wb') as f:
		pickle.dump(num8, f)
with open(str(tsnum5) +'.pickle', mode='wb') as f:
		pickle.dump(num10, f)
with open(str(tsnum6) +'.pickle', mode='wb') as f:
		pickle.dump(num12, f)
def kiguusecond(noritsugu):
	num0= [
		1,-2,3,-4,5,
		-6,7,-8,9,-10,
		11,-12,13
		]
def player3456(player3,nokori,hoyuuABCD,hoyuupABCD,filePlayerABCD,ABCDenergy,playerABCD1,numE,ichiABCD,ichix0,tsnum,numABCD,numABCD1):
	#playerABCD
	global ichiA,ichiB,ichiC,ichiD
	ichix0 = awase(numE)
	detame2 = awase3(ichix0,tsnum,numABCD,numABCD1)
	print(playerABCD1+"さんには、～"+ str(detame2) +"～の目が出ました")
	ichiABCD = ichiABCD + int(detame2)
	nokori2 = str(30 - ichiABCD)
	nokori2 = int(nokori2)
	if nokori2 > 0:
		print("あと残り～"+str(nokori2)+"～こまです")
	else:
		print(playerABCD1+",Goal!!しました")
	if ichiABCD > 30:
		ichiABCD = 30
	banmen(player3,ichiABCD)
	if ichiABCD ==30:
		print(playerABCD1+",一着ボーナス獲得")
		hunobonus(player3,nokori,playerABCD1)
		with open(str(playerABCD1) + 'kanri.pickle', 'rb') as f:
			hoyuupABCD = pickle.load(f)
			hoyuupABCD = int(hoyuupABCD)
			NoritsuguH_hoyuu = int(hoyuupABCD*1/5)
		with open(str(NoritsuguH) +'charge.pickle', mode='wb') as f:
			pickle.dump(NoritsuguH_hoyuu, f)
		with open(str(NoritsuguH) + '.pickle', 'rb') as f: #setup.pyにて0ポイントで初期化後にて。
			ShuuekiP_NH = pickle.load(f)
		NoritsuguHoshizawa = NoritsuguH_hoyuu + ShuuekiP_NH
		hoyuuABCD = int(hoyuupABCD) - int(NoritsuguH_hoyuu)
		with open(str(NoritsuguH) +'.pickle', mode='wb') as f:
			pickle.dump(NoritsuguHoshizawa, f)
		hoyuupcharge = int(hoyuuABCD)
		with open(str(filePlayerABCD) +'charge.pickle', mode='wb') as f:
			pickle.dump(hoyuupcharge, f)
		with open(str(filePlayerABCD) + '.pickle', 'rb') as f:
			ABCDenergy = pickle.load(f)
		ABCDenergy = ABCDenergy + hoyuupcharge
		with open(str(filePlayerABCD) +'.pickle', mode='wb') as f:
			pickle.dump(ABCDenergy, f) 
		playsound("owariniitashimasu.mp3")
		print("Owari Ni Itashi Masu")
		playsound("race2.wav")
		playsound("shuuryoushimasu.mp3")
		print("終了します。毎度どうもありがとうございました。どんどん増やそうEmotionalPoint‼")
		return 0
	komasuu=int(ichiABCD)
	return komasuu
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
def awase2(ra,runnerSE,runner2,tsnumB,num0,numA1):
	count = 0
	with open(str(tsnumB)+ '.pickle', 'rb') as f:
			numA1 = pickle.load(f)
	num0 = numA1
	while True or x> 0:
		r2 = random.choice(num0)
		x = len(num0)
		x = x - 1
		count = count + 1
		print("引いた数は"+str(r2)+"でした。"+str(count)+"回目の数合わせしてます．xの値は"+ str(ra)+"です")
		num0.remove(r2)
		num0 = num0
		if ra == str(r2):
			playsound(runnerSE)
			print(runner2)
			with open(str(tsnumB)+ '.pickle', 'rb') as f:
				numA1 = pickle.load(f)
			numA1.remove(r2)
			with open(str(tsnumB)+'.pickle', mode='wb') as f:
				pickle.dump(numA1, f)
			break
	return count
def awase3(ra,tsnumA,num0,numA1):
	count = 0
	with open(str(tsnumA)+ '.pickle', 'rb') as f:
			numA1 = pickle.load(f)
	num0 = numA1
	while True or x> 0:
		r2 = random.choice(num0)
		x = len(num0)
		x = x - 1
		count = count + 1
		print("引いた数は"+str(r2)+"でした。"+str(count)+"回目の数合わせしてます．xの値は"+ str(ra)+"です")
		num0.remove(r2)
		num0 = num0
		if ra == str(r2):
			with open(str(tsnumA)+ '.pickle', 'rb') as f:
				numA1 = pickle.load(f)
			numA1.remove(r2)
			with open(str(tsnumA)+'.pickle', mode='wb') as f:
				pickle.dump(numA1, f)
			break
	return count
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
	r = nokori #robo63のみになっている
	r = int(r)
	r2 = int(random.randint(1, r))
	hoyuup = hoyuup2/(r2/2)
	hoyuup = int(hoyuup)
	points = hoyuup2 + hoyuup
	with open(str(file2) +'.pickle', mode='wb') as f:
		pickle.dump(points, f)
	print(file2+"さんには、"+str(hoyuup)+"ボーナスポイントがkiguuのポイントの"+str(hoyuup2)+"ポイントに付加されます。")
def hunobonus(file9,nokori9,filerX): #自らのポイントを相手の、のこり駒数で割ったポイントで自らのポイントから除算して保存し、仮に相手のポイントを一時、管理する。
	with open(str(file9) + '.pickle', 'rb') as f:
		hoyuup2 = pickle.load(f)
	r = nokori9
	r = int(r)
	r2 = int(random.randint(1, 2*r))
	hoyuup = hoyuup2/(r2)
	hoyuup = int(hoyuup)
	points = hoyuup2 - hoyuup
	with open(str(file9) +'.pickle', mode='wb') as f:
		pickle.dump(points, f)
	with open(str(filerX) +'kanri.pickle', mode='wb') as f:
		pickle.dump(hoyuup, f)
	print(file9+"さんには、マイナス"+str(hoyuup)+"ポイントがkiguuのポイントの"+str(hoyuup2)+"ポイントに付加されます。")
	with open(str(filerX) + 'kanri.pickle', 'rb') as f:
		hoyuup63 = pickle.load(f)
	hoyuup63 = int(hoyuup63)
	NoritsuguH_hoyuu = int(hoyuup63*2/5)
	with open(str(NoritsuguH) +'charge.pickle', mode='wb') as f:
		pickle.dump(NoritsuguH_hoyuu, f)
	with open(str(NoritsuguH) + '.pickle', 'rb') as f: #初期化はsetupにて0(Point)代入済み
		ShuuekiP_NH = pickle.load(f)
	NoritsuguHoshizawa = NoritsuguH_hoyuu + ShuuekiP_NH
	hoyuu63 = int(hoyuup63) - int(NoritsuguH_hoyuu)
	with open(str(NoritsuguH) +'.pickle', mode='wb') as f:
		pickle.dump(NoritsuguHoshizawa, f)
	hoyuupcharge = int(hoyuu63)
	with open(str(filerX) +'charge.pickle', mode='wb') as f:
		pickle.dump(hoyuupcharge, f)
	with open(str(filerX) + '.pickle', 'rb') as f:
		roboenergy = pickle.load(f)
	roboenergy = roboenergy + hoyuupcharge
	with open(str(filerX) +'.pickle', mode='wb') as f:
		pickle.dump(roboenergy, f)
def banmen(player1,ichiABCD):
	print("_____さぁっ...‼決まるか！？_____")
	print("OYMGSet...Don!!"+"□"*(own_ichi-1) + player1 +"□"*(30-own_ichi)+"Goal!!")
	print("OYMGSet...Don!!"+"□"*(Robo63_ichi-1) + "Robo63"+"□"*(30-Robo63_ichi)+"Goal!!") #後攻の格差是正
	print("OYMGSet...Don!!"+"□"*(ichiA-1) + playerA1 +"□"*(30-ichiA)+"Goal!!")
	print("OYMGSet...Don!!"+"□"*(ichiB-1) + playerB1 +"□"*(30-ichiB)+"Goal!!")
	print("OYMGSet...Don!!"+"□"*(ichiC-1) + playerC1 +"□"*(30-ichiC)+"Goal!!")
	print("OYMGSet...Don!!"+"□"*(ichiD-1) + playerD1 +"□"*(30-ichiD)+"Goal!!") 
	print("__________")
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
def game(player3):
	while True:
		global ichiA
		global ichiB
		global ichiC
		global ichiD
		input("Enterを押すと"+player3+"さんサイコロを振れますよ")
		playsound("sai1.mp3")
		global own_ichi
		r2 = awase(num)
		detame = awase2(r2,playerSE,player,tsnum1,num2,numA)
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
		banmen(player3,ichiABCD)
		if own_ichi == 30:
			print(player3+"一着ボーナス獲得！")
			bonus(player3,nokori2) #robo63のみになっているから他からもポイントを受け取りたい
			nokoriA = str(30-ichiA)
			nokoriA=int(nokoriA)
			bonus(player3,nokoriA)
			nokoriB = str(30-ichiB)
			nokoriB=int(nokoriB)
			bonus(player3,nokoriB)
			nokoriC = str(30-ichiC)
			nokoriC=int(nokoriC)
			bonus(player3,nokoriC)
			nokoriD = str(30-ichiD)
			nokoriD=int(nokoriD)
			bonus(player3,nokoriD)
			playsound("owariniitashimasu.mp3")
			print("Owari Ni Itashi Masu")
			playsound("race2.wav")
			playsound("shuuryoushimasu.mp3")
			print("終了します。どうもありがとうございました。もっと、どんどん資の産みを増やそう")
			break
		input("Enterを押すとRobo63さんとその他の走者のすごろくが振られます")
		playsound("sai2.mp3")
		global Robo63_ichi
		r63 = awase(num3)
		detame2 = awase2(r63,robo63SE,robo63,tsnum2,num4,numB)
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
		banmen(player3,ichiABCD)
		if Robo63_ichi ==30:
			print("コンピュータ,一着ボーナス獲得")
			hunobonus(player3,nokori,filerobo63)
			playsound("owariniitashimasu.mp3")
			print("Owari Ni Itashi Masu")
			playsound("race2.wav")
			playsound("shuuryoushimasu.mp3")
			print("終了します。毎度どうもありがとうございました。どんどん増やそうEmotionalPoint‼")
			break
		ichiA=player3456(player3,nokori,hoyuuA,hoyuupA,filePlayerA,Aenergy,playerA,num5,ichiA,ichiA0,tsnum3,numPLA,numPLA1)
		ichiB=player3456(player3,nokori,hoyuuB,hoyuupB,filePlayerB,Benergy,playerB,num7,ichiB,ichiB0,tsnum4,numPLB,numPLB1)
		ichiC=player3456(player3,nokori,hoyuuC,hoyuupC,filePlayerC,Cenergy,playerC,num9,ichiC,ichiC0,tsnum5,numPLC,numPLC1)
		ichiD=player3456(player3,nokori,hoyuuD,hoyuupD,filePlayerD,Denergy,playerD,num11,ichiD,ichiD0,tsnum6,numPLD,numPLD1)
		banmen(player3,ichiABCD)
		if ichiA==0 or ichiB==0 or ichiC==0 or ichiD==0:
			break
def sugoroku(a3,player4):
	if a3 == "Y" or a3 == "y":
		print(player4+"さんで決まりました")
		banmen(player4,ichiABCD)
		print("すごろく、OYMGSet...Don!!")
		game(player4)
	else:
		playsound("owariniitashimasuka.mp3")
		print("Owari Ni Itashi Masuka？")
		ans = input("Y/N:")
		if ans == "Y" or ans == "y":
			playsound("race2.wav")
			playsound("shuuryoushimasu.mp3")
			print("終了します。どうもありがとうございました。")
			sys.exit()
		else:
			return "n"

playsound("race1.wav")	
answer = input("ゲームを始めますか？ please input(y=yes,n=no) :y or n:")
y = "y"
n = "n"
player = name()
if answer in y:
	a2 = kimari(player)
	j = sugoroku(a2,player)
	while "n" == j:
		a2 = kimari(player)
		j == sugoroku(a2,player)
else:	
	playsound("owariniitashimasu.mp3")
	print("Owari Ni Itashi Masu")
	playsound("remain.wav")
	playsound("race2.wav")
	playsound("shuuryoushimasu.mp3")
print("終了します。どうもありがとうございました。")
robokashitsuke(player)
playsound("2023natsuba.mp3")
