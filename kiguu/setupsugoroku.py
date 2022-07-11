import pickle
def swichi():
	print("sugoroku.pyにて始める前に必ずこのソフトウェアにて一回だけ手続きを行ってください。行わないとsugoroku.pyはできませんので注意です。")
	answer = input("robo63に電源を入れる手続きを願います...。電源を入れてよろしいですか？y/n(y以外のキー):")
	y = "y"
	n = "n"
	if answer in y:
		filerobo63 = str("robo63")
		roboenergy = 0
		with open(str(filerobo63) +'.pickle', mode='wb') as f:
			pickle.dump(roboenergy, f)
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

