import pickle
print("kiguuのpoint値を確認したい")
print("ファイル名を入力してください")
file = input("input:")
def kanri(file1):
	print("point保存確認へ・・・")
	with open(str(file1) + '.pickle', 'rb') as f:
		hozon1 = pickle.load(f)
		hozon1 = int(hozon1)
	if hozon1 <0:
		print("Watashiha,robo63toAnatanoMainasuPointWoZeroniShimasu.MainasuPointHa,Nakushitahougarakudesuyo!!Douitashimasuka?")
		answer = input("input→y/n?:")
		answer = str(answer)
		if answer == "y":
			print(str(hozon1) + "ポイント保存されております。")
			print("大変申し訳ございませんでした。pointを０pointに変換します。手続き文言：くんくんくん...、わんっ!!ChannToOmiTouShiDaWan！？")
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
	else:
		print(str(hozon1) + "ポイント保存されております。")
		print("Think can I reset zeropoints this points ? sorry and please.")
		answer = input("input→y/n?:")
		answer = str(answer)
		if answer == "y":
			print(str(hozon1) + "ポイント保存されております。")
			print("大変申し訳ございませんでした。pointを０pointに変換します。だるいときは生活習慣が悪くて運動習慣と食事制限早寝早起き足りないからではないかと思ってます。お気をつけください。")
			hozon1 = int(0)
			with open(str(file1) +'.pickle', mode='wb') as f:
				pickle.dump(hozon1, f)
			print(str(hozon1) + "ポイント保存されております。")
			end = input("終了は何かキーを押してエンターキーを押してください:")
			end = str(end)
			if end == end:
				return 0
				print(str(hozon1) + "ポイント保存されております。")
		else:
			print(str(hozon1) + "ポイント保存されております。")
			end = input("終了は何かキーを押してエンターキーを押してください:")
			end = str(end)
			if end == end:
				return 0
kanri(file)