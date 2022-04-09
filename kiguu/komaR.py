import random
pl_pos = 1
com_pos= 1
com2_pos=1
com3_pos=1
com4_pos=1

def banmen():
	print("・"*(pl_pos-1)+"①"+"・"*(30-pl_pos)+"Goal")
	print("・"*(com_pos-1)+"②"+"・"*(30-com_pos)+"Goal")
	print("・"*(com2_pos-1)+"③"+"・"*(30-com2_pos)+"Goal")
	print("・"*(com3_pos-1)+"④"+"・"*(30-com3_pos)+"Goal")
	print("・"*(com4_pos-1)+"⑤"+"・"*(30-com4_pos)+"Goal")
	print("ー"*33)
print("位置について・・・すたぁと！")


banmen()
while True:
		input("Push Enter")
		pl_pos = pl_pos + random.randint(1,6)
		if pl_pos > 30:
			pl_pos = 30
		if pl_pos == 30:
			banmen()
			print("①の勝ちです！")
			break
		com_pos = com_pos + random.randint(1,6)
		if com_pos > 30:
			com_pos = 30
		if com_pos == 30:
			banmen()
			print("②の勝ちです！")
			break
		com2_pos = com2_pos + random.randint(1,6)
		if com2_pos > 30:
			com2_pos = 30
		if com2_pos == 30:
			banmen()
			print("③の勝ちです！")
			break	
		com3_pos = com3_pos + random.randint(1,6)
		if com3_pos > 30:
			com3_pos = 30
		if com3_pos == 30:
			banmen()
			print("④の勝ちです！")
			break
		com4_pos = com4_pos + random.randint(1,6)
		if com4_pos > 30:
			com4_pos = 30
		banmen()
		if com4_pos == 30:
			
			print("⑤の勝ちです！")
			break	