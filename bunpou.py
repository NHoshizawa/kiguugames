aaa=["S主語","V動詞","C補語","O目的語"]
aab=["名詞的→同格や主語や目的語や補語","形容詞的→名詞を説明、主語や間接目的語=補語になる、","副詞的→動詞を修飾〜するために"]
aac=["語","句","節"]
aad=["SV","SVC","SV O","SVO1(~に)O2(〜を)","SVOC"]
bunkeiburui=0
hinshi=0
kumikei=0
bunkei=0
a1=0
a2=0
a3=0
a4=0
def baa():
	bunkeiburui=int(input('文型文類？0〜4:'))
	hinshi=int(input('語句節の品詞(用法)?0〜2:'))
	kumikei=int(input('語=0 句=1 節=2 いずれか？:'))
	bunkei=int(input('文型1なら0,文型2なら1,文型3なら2,文型4なら3,文型5なら4 のうち0〜4?:'))
	a1=str(aaa[bunkeiburui])
	a2=str(aab[hinshi])
	a3=str(aac[kumikei])
	a4=str(aad[bunkei])
	return a1,a2,a3,a4
def main():
	b1,b2,b3,b4= baa()
	print(b1+b2+b3+b4)
	return 0
main()
	
	
	
