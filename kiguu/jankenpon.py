import random
import os
import sys
def jankenpon(x):
	guu=["",
		 " ＾＾＾＾ ",
		 " |||||||| ",
		 " >\\\\\\\\\\\\\\ ",
		 " <\\\\\\\\\\\\\\ ",
		 "  \\\\\\\\\\\\ ",
		 "   \\\\\\\\\\ ",
		""
		]
	choki=["",
		"\\     \\ ",
		" \\   \\ ",
		"  \\ \\ ",
		"  \\\\^^ ",
		" ---//\\ ",
		"\\\\\\\\\\\\\\\\ ",
		" \\\\\\\\\\\\\\ ",
		"  \\\\\\\\\\ ",
		"  \\\\\\"
	     ]
	paa=["",
		"     \\",
		"   \\ \\ \\ ",
		" \\ \\ \\ \\ ",
		" \\ \\ \\ \\  \\",
		" \\\\\\\\\\\\\\\\ \\  ",
	  	"\\\\\\\\\\\\\\\\\\\\ ",
		" \\\\\\\\\\\\\\ ",
		"  \\\\\\\\\\ ",
		""
	    ]
	if x==0:
		for o in guu[0:]:
			print(o)
	elif x==1:
		for o in choki[0:]:
			print(o)
	elif x==2:
		for o in paa[0:]:
			print(o)
def janken():
	numJ=[0,1,2]
	janken=["guu","choki","par"]
	own = input("janken :0=guu,1=choki,2=par: input: 0or1or2:")
	own = str(own)
	if own == '0' or own == '1' or own == '2':
		print('jannkennponn!?')
		player=random.choice(numJ)
		player=int(player)
		own=int(own)
		jankenpon(own)
		print('own:'+janken[own])
		jankenpon(player)
		print('robo63:'+janken[player])
		kachime=player-own
		kachime=int(kachime)
		if kachime==0:
			print('aiko:even')
			return 'n'
		elif kachime==1 :
			print('win')
			return 'p'
		elif kachime==2 :
			print('lose')
			return 'e'
		elif kachime==-1:
			print('lose')
			return 'e'
		elif kachime==-2:
			print('win')
			return 'p'
	else:
		print('コースを外しましたのでおわり。  失笑...。残念またの機会に')
		sys.exit()	
janken()