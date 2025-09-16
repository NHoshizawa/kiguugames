import pickle
def swichi():
	print("sugoroku.pyにて始める前に必ずこのソフトウェアファイルにて一回だけ手続きを行ってください。行わないとsugoroku.pyはできませんので注意です。")
	answer = input("(イメージ)robo63に電源を入れる手続きを願います...。(イメージ)電源を入れてよろしいですか？y/n(y以外のキー):")
	y = "y"
	n = "n"
	if answer in y:
		fileasobikaisuuzenbu = str("count")
		fileplayer3win = str("player3win")
		filerobo63win = str("robo63win")
		fileplayerA = str("playerA")
		fileplayerB = str("playerB")
		fileplayerC = str("playerC")
		fileplayerD = str("playerD")
		count = 1
		kachiten = 1
		kachitenrobo63 = 1
		kachitenA = 1
		kachitenB = 1
		kachitenC = 1
		kachitenD = 1
		with open(str(fileasobikaisuuzenbu)+'.pickle', mode='wb') as f:
			pickle.dump(count, f)
		with open(str(fileplayer3win)+'.pickle', mode='wb') as f:
			pickle.dump(kachiten, f)
		with open(str(filerobo63win)+'.pickle', mode='wb') as f:
			pickle.dump(kachitenrobo63, f)
		with open(str(fileplayerA)+'win'+'.pickle', mode='wb') as f:
			pickle.dump(kachitenA, f)
		with open(str(fileplayerB)+'win'+'.pickle', mode='wb') as f:
			pickle.dump(kachitenB, f)
		with open(str(fileplayerC)+'win'+'.pickle', mode='wb') as f:
			pickle.dump(kachitenC, f)
		with open(str(fileplayerD)+'win'+'.pickle', mode='wb') as f:
			pickle.dump(kachitenD, f)
		end = input("終了いたしました。続きをsugoroku.pyにてお楽しみください。何かキーを押してエンターキーを押してください:")
		end = str(end)
		if end == end:
			return 0
	else:
		print("終了します。")
		end = input("終了は何かキーを押してエンターキーを押してください:")
		end = str(end)
		if end == end:
			return 0
swichi()

