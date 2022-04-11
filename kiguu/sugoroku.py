import os
import random
import sys
import pickle
own_ichi = 1
Robo63_ichi = 1
from playsound import playsound
def starts(file1):
	if os.path.exists("./"+str(file1)+".pickle"):
	    print("ようこそすごろくへ、一着でGoal!!なされると ポイントが加算されます。")
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
	hoyuup = hoyuup2/r
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
	hoyuup = hoyuup2/r
	hoyuup = int(hoyuup)
	points = hoyuup2 - hoyuup
	with open(str(file2) +'.pickle', mode='wb') as f:
		pickle.dump(points, f)
	print(file2+"さんには、マイナス"+str(hoyuup)+"ポイントがkiguuのポイントの"+str(hoyuup2)+"ポイントに付加されます。")
def banmen(player1):
	print("OYMGSet...Don!!"+"□"*(own_ichi-1) + player1 +"□"*(30-own_ichi)+"Goal!!")
	print("OYMGSet...Don!!"+"□"*(Robo63_ichi-1) + "Robo63"+"□"*(30-Robo63_ichi)+"Goal!!")
def name():
	file = input("kiguuシリーズで作成済みの名前を入れてください")
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
		detame = random.randint(1,6)
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
			playsound("ending.wav")
			playsound("shuuryoushimasu.mp3")
			print("終了します。どうもありがとうございました。もっと、どんどん資の産みを増やそう")
			break
		input("Enterを押すとRobo63さんのすごろくが振られます")
		playsound("sai2.mp3")
		global Robo63_ichi
		detame2 = random.randint(1,6)
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
			hunobonus(player3,nokori2)
			playsound("owariniitashimasu.mp3")
			print("Owari Ni Itashi Masu")
			playsound("ending.wav")
			playsound("shuuryoushimasu.mp3")
			print("終了します。どうもありがとうございました。どんどん増やそう")
			break
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
			playsound("ending.wav")
			playsound("shuuryoushimasu.mp3")
			print("終了します。どうもありがとうございました。")
			return 0
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
		sugoroku(a2,player)
else:
	playsound("owariniitashimasu.mp3")
	print("Owari Ni Itashi Masu")
	playsound("ending.wav")
	playsound("shuuryoushimasu.mp3")
	print("終了します。どうもありがとうございました。")
sys.exit()
