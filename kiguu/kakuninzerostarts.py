import pickle
print("kiguuのpoint値を確認したい")
print("ファイル名を入力してください")
file = input("input:")
def kanri(file1):
	print("point保存確認へ・・・")
	with open(str(file1) + '.pickle', 'rb') as f:
		hozon1 = pickle.load(f)
		hozon1 = int(hozon1)
	print("Watashiha,robo63toAnatanoMainasuPointWoZeroniShimasu.\MainasuPointHa,Nakushitahouugarakudesuyo!!\Douitashimasuka?")
	answer = input("input→y/n?:")
	answer = str(answer)
	if answer == "y":
		print("大変申し訳ございませんでした。pointを０pointに変換します。\手続き文言：くんくんくん...、わんっ！？")
		hozon1 = int(0)
		with open(str(file1) +'.pickle', mode='wb') as f:
			pickle.dump(hozon1, f)
		print(str(hozon1) + "ポイント保存されております。")
		end = input("終了は何かキーを押してエンターキーを押してください:")
		end = str(end)
		if end == end:
			return 0
	else:
		print(str(hozon1) + "ポイント保存されております。")
		end = input("終了は何かキーを押してエンターキーを押してください:")
		end = str(end)
		if end == end:
			return 0
kanri(file)