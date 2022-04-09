import tkinter
import random

def click_btn():
	label["text"]=random.choice(["大吉","中吉","小吉","凶"])
	label.update()
	
root = tkinter.Tk()//root変数をインスタンス化した(tkinterモジュール内TK()クラス)
root.title("おみくじソフト")//Tk()クラス内title()メゾット
root.resizable(False,False) //メソッド（「クラス内で定義された関数」や「オブジェクトの属性として参照される関数」）の場合はドットの前が変数や値になります（つまり、データ型を有するもの）
canvas = tkinter.Canvas(root, width=800,height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="miko.png")//変数gazouにtkinterモジュール内メゾットの戻り値を代入
canvas.create_image(400,300,image=gazou)
label = tkinter.Label(root,text="??",font=("Times New Roman",120),bg="white")
label.place(x=380,y=60)
button = tkinter.Button(root,text="おみくじを引く",font=("Times New Roman",36),command=click_btn,fg="skyblue")//インスタンス(オブジェクト)化
button.place(x=360,y=400)
root.mainloop()//Tk()モジュール内メゾットmainloop()を呼び出し