#include <iostream>
using namespace std;

void picture(i1,q1):
	int i1=0;
	int c1=0;
	int a1=0;
	char kigou[]={"クローバー","スペード","ハート","ダイヤ"};
	int poi[]={1,2,3,4,5,6,7,8,9,10,11,12,13};
	char np[13] ={"A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K "};
	a1 = np[i1];
	c1 = kigou[q1];
	str xy[] = {"",
		"----------",
		"|        |",
		     a1     ,
		"|        |",
		     c1     ,
		"|        |",
		     a1     ,
		"|        |",
		"----------",
		""
		};
    for(int i = 0; i < std::end(xy) - std::begin(xy); ++i) 
		{
        std::cout << xy[i] << "\n";
    	};
};