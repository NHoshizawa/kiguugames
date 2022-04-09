import random
import datetime
ALP = [
"A","B","C","D","E","F","G",
"H","I","J","K","L","M","N",
"O","P","Q","R","S","T","U",
"V","W","X","Y","Z",
]
r = random.choice(ALP)　//モジュールの関数もドット（.）を付けて呼び出します。メソッドと混同しやすいオブジェクトの属性として参照される関数が返した戻り値を変数rに代入
alp = ""
for i in ALP: //リストALPの要素数の中から0番目からからNULL値まで繰り返す
	if i != r:
		alp = alp + i //変数alpにiのリストALP要素数ない表示を代入
print(alp)
st = datetime.datetime.now()//datetimeモジュールのdatetimeクラス内now()モジュールの戻り値を代入
ans = input("抜けてるアルファベットは？")
if ans == r:
	print("正解です")
	et = datetime.datetime.now()
	print(str((et-st).seconds)+"秒かかりました")//クラスstrの引数et,stを渡しそのモジュールの戻り値をprintの引数に渡している。
else:
	print("違います")