import pickle
print("kiguuのpoint値を確認したい")
print("ファイル名を入力してください")
file = input("input:")
def kanri(file1):
    print("point保存確認へ・・・")
    with open(str(file1) + '.pickle', 'rb') as f:
        hozon1 = pickle.load(f)
        hozon1 = int(hozon1)
    print(str(hozon1) + "ポイント保存されております。")
    end = input("終了は何かキーを押してエンターキーを押してください:")
    end = str(end)
    if end == end:
        return 0