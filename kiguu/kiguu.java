import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Arrays;
import java.io.*;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
class kiguu{
	static int Filedump(String file1,String kanrikiguu,int atai){
		Scanner scanner = new Scanner(System.in);
		File c1 = new File();
		String kiguu ="kiguu";
		String kanri ="kanri";
		try{
			BufferdReader br = new printWriter
			(new BufferedReader(new FileReader(String(file1)+String(kanrikiguu)+ ".txt")));
			pw.println(atai);
			pw.close();
		}catch (FileNotFoundException f) {
		}
		
	}	
	static int Fileload(String file2,String kanrikiguu,int atai2){
		try{
			BufferdReader br =
			new BufferedReader(new FileReader(String(file2)+String(kanrikiguu)+ "kanri.txt"));
			int atai2 = br.readLine();
			br.close();
		}catch (FileNotFoundException f) {
		}
		return atai2;
	}
	static int[] num0 = {
	        1,-2,3,-4,5,
	        -6,7,-8,9,-10,
	        11,-12,13
	        };
	static String[] kigou = {"クローバー","スペード","ハート","ダイヤ"};
	String dpz=0;
	String i=0;
	int[] poi = {1,2,3,4,5,6,7,8,9,10,11,12,13};
	int[] poi2 = {1,2,3,4,5,6,7,8,9,10,11,12,13};
	Random pw = new Random();
	int pw = pw.nextInt(poi);
	int pw = poi[pw.nextInt(13)];
	Random pw1 = new Random();
	int pw1 = pw1.nextInt(poi2);
	int pw1 = poi2[pw1.nextInt(13)];
	int n = scanner.next();
	int n = (String)n;
	static int kanriup(String file1){
		Fileload(file1,kanri,hozon2);
	}
	    
	static int kanri(String file2){
		Fileload(file2,kiguu,hozon1);
	}
	    
	static int kanri2(String file3){
		System.out.println("現在の保有ポイント合計は...");
		int hozon1 = Fileload(file3,"",hozon1);
		int total = (int)hozon1;
		System.out.println("合計で" + String(total) + "ポイントです");
	}

	static int end(String file4){
		String filebanchi = "C:\\"+String(file4)+"kanri.txt";
		File file = new File(filebanchi);
		if (isFileExists(file)){
			int hozon2 = Fileload(file4,kanri,hozon2);
			int hozon1 = Fileload(file4,kiguu,hozon1);
			int hoyuup = hozon2 + hozon1;
			hoyuup = (int)hoyuup;
			String filebanchi = "C:\\"+String(file4)+".txt";
			File file = new File(filebanchi);
			if (isFileExists(file)) {
				int hoyuup2 = Fileload(file4,"",hoyuup2);
				hoyuup2 = hoyuup2 + hoyuup;
				Filedump(file4,"",hoyuup2);
				System.out.println("保有ポイントは"+String(hoyuup2)+"です。");
				try {
					Path path = Paths.get("./"+String(file4)+"kanri.txt");
					Files.deleteIfExists(path);
				} catch (FileNotFoundException f) {
				}
				System.out.println("何か押してエンターキーを押してください:");
				String end = scanner.next();

				if (end == end){
					System.exit(0);
				}
			}else{
				Filedump(file4,"",hoyuup);
				System.out.println("保有ポイントは"+String(hoyuup)+"です。");
				Path path = Paths.get("./"+String(file4)+"kanri.txt");
				Files.deleteIfExists(path);
				System.out.println("何か押してエンターキーを押してください:");
				String end = scanner.next();
				if (end == end){
					System.exit(0);
					}
			}
		}
		else{
			int hozon1 = Fileload(file4,kiguu,hozon1);
			int hoyuup = (int)hozon1;
			String filebanchi = "C:\\"+String(file4)+".txt";
			File file = new File(filebanchi);
			if (isFileExists(file)) {
				System.out.printlnln("File exists!!");
				int houup2 = Fileload(file4,"",hoyuup2);
				int hoyuup2 = hoyuup2 + hoyuup;
				Filedump(file4,"",hoyuup2);
				System.out.println("保有ポイントは"+String(hoyuup2)+"です。");
				System.out.println("何か押してエンターキーを押してください:");
				String end = scanner.next();
				if (end == end){
					System.exit(0);
			 	}
			}else{
				Filedump(file4,"",hoyuup);
				System.out.println("保有ポイントは"+String(hoyuup)+"です。");
				System.out.println("何か押してエンターキーを押してください:");
				String end = scanner.next();
				if (end == end){
					System.exit(0);
				}
			}
		}
	}

	static int picture(int i1,int q1){
		String[] np = {"A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K "};
		int a1=np[i1];
		String c1=kigou[q1];
		String[] xy = {
			"",
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
			String str_xy = String.join(",",xy);

			System.out.println(str_xy);
	}
	static int tensuu(int i){
		int[] num = {
		1,-2,3,-4,5,
		-6,7,-8,9,-10,
		11,-12,13
		};
		Random r = new Random();
		String r = r.nextInt(num);
		r = num[r.nextInt(13)];
		picture(num0.index(r),i);
		System.out.println("奇数は正で偶数は負になります。" + String(r));
		List<String> list = new ArrayList<String>(Arrays.asList(r));
		list.remove(r);
		int num1 = num;
		Random r2 = new Random();
		int r2 = r2.nextInt(num1);
		r2 = num1[r2.nextInt(13)];
		picture(num0.index(r2),i);
		System.out.println("奇数は正で偶数は負になります。"+String(r2));
		List<String> list = new ArrayList<String>(Arrays.asList(r2));
		list.remove(r2);
		int num2 = num1;
		Random r3 = new Random();
		r3 = r3.nextInt(num2);
		r3 = num2[r3.nextInt(13)];
		picture(num0.index(r3),i);
		System.out.println("奇数は正で偶数は負になります。"+String(r3));
		int x = r+r2+r3;
		int y = abs(x);
		if (y <= 13 && y != r && y != r2 && y != r3){
			if (y != r != r2 != r3){
				System.out.println(String(y) + "の値となります。三枚を足した合計や13以下の値の絶対値を参考に存在するトランプの数字のみとなります");
				return y;
			}
			else{
				int y = 0;
				System.out.println("合計値のトランプが既に出ており"+String(y)+"のため無効になります（笑）");
				return y;
			}
		}
		else{
			System.out.println(String(y) + "の値は合計値の絶対値です。");
			System.out.println("合計値が13以上なので,13以下にします。");
			int y = y - 13;
			if (y <= 13){
				if (y !=  r != r2 != r3){
					System.out.println(String(y) + "の値となります。三枚を足した合計や13以下の値の絶対値を参考に存在するトランプの数字のみとなります"); 
					return y;
				}
				else{
					y = 0;
					System.out.println("合計値のトランプが既に出ており"+String(y)+"のため無効になります（笑）");
					return y;
				}
			}
			else{
				y = y - 13;
				if (y != r != r2 != r3){
					System.out.println(String(y) + "の値となります。三枚を足した合計や13以下の値の絶対値を参考に存在するトランプの数字のみとなります"); 
					return y;
				}
				else{
					y = 0;
					System.out.println("合計値のトランプが既に出ており"+String(y)+"のため無効になります（笑）");
					return y;
				}
			}
		}
	}
	static int cal(int i){
		int c2 = 0;
		c2 = (int)tensuu(i);
		string kig=kigou[i];
		int kg = c2 % 2;
		if (kg == 0){
			c2=-c2;
			System.out.println(kig+ "偶数なので値がマイナスになります。"+String(c2));
			return c2;
		}
		else{
			c2=c2;
			System.out.println(kig+"奇数なので値がプラスになります。"+String(c2));
			return c2;
		}
	}
	static int kiguu(String file5){
		int c=(int)cal(0);
		int s=(int)cal(1);
		int h=(int)cal(2);
		int d=(int)cal(3);
		int o=c+s+h+d;
		int q = abs(o);
		q = (int)q;
		if (q == 0){
			System.out.print("kiguuの結果が0pointなのでinputとoutputバランスよく!今日、一日気を休めてね");
			int point = q;
			Filedump(file5,kiguu,point);
			return 'e';
		}
		else{
			System.out.println("トランプの４種類の各々の３枚の合計が");
			System.out.println(String(q)+"pointの結果となり。奇数か?、偶数か?、当たりかどうか、結果へ進みます。");
			int pz = q % 2;
			pz = (int)pz;
			if (pz == 0 && n == '0'||  pz == 0 && n == '1'){
				if (n == '0'){ 
					int p1 = q*2;
					System.out.println("PointGet...");
					System.out.println("偶数であたり、2倍に!!");
					System.out.println(String(p1)+"point outputへ気持ちの器量に!!");
					int point = p1;
					Filedump(file5,kiguu,point);
					return 'p';
				}
				else{
					System.out.println("PointGet...そのままになります");
					System.out.println(String(q)+"pointをoutputへ気持ちの器量に!!");
					int point = q;
					Filedump(file5,kiguu,point);
					return 'p';
				}
			}
			else if (pz == 1 && n == '0' ||  pz== 1 && n == '1'){
				if (n == '1'){
					int p1 = q*2;
					System.out.println("PointGet...");
					System.out.println("奇数であたり、2倍に!!");
					System.out.print(String(p1)+"pointをinputへ気持ちの器量に!!");
					int point = p1;
					Filedump(file5,kiguu,point);
					return 'p';
				}
				else{
					System.out.println("PointGet...そのままになります");
					System.out.print(String(q)+"pointをinputへ気持ちの器量に!!");
					int point = q ;
					Filedump(file5,kiguu,point);
					return 'p';
				}
			}
			else{
				System.out.println("kiguu終了");
				int point = 0;
				int hozon1 = Fileload(file5,kiguu,hozon1);
				int point = point + hozon1;
				Filedump(file5,kiguu,point);
				return 'e';
			}
		}
	}
	static int ru(String file6){
		String filebanchi = "C:\\"+String(file6)+"kanri.txt";
		File file = new File(filebanchi);
		if (isFileExists(file)) {
			int point1 = kanri(file6);
			int point8 = kanriup(file6);
			int point7 = (int)point1+(int)point8;
			System.out.println("つづけて、1～5倍運用挑戦しませんか？");
			System.out.print("please input(y=yes,n=no) :y or n:");
			String answer = scanner.next();
			String y = "y";
			String n = "n";
			if (answer == y){
				Random r2 = new Random();
				int r2 = r2.nextInt(1,3);
				int point1 = abs(point1);
				int r3 = point7 * r2/3;
				System.out.println("現在の" + String(point7) + "ポイントの3分の"+String(r2)+",つまり"+String(r3)+"より持ちpoint数字内から無作為に選んだ値の");
				System.out.println("ランダムに出た、数字の傾向は、");
				for (int i = 1; i <= 6; i++){
					Random points = new Random();
					int points = points.nextInt(0,point7);
					System.out.println(String(points));
				}
				System.out.println("となります。次の数字は");
				Random points = new Random();
				int points = points.nextInt(0,point7);
				System.out.println("high(1) or low(2)か?");
				System.out.println("choice,1 or 2:");
				String number = scanner.next();
				int number = number;
				horl = points - point7 * r2/3;
				if (number == 1 ||  number == 2){
					if (horl > 0){
						int answer = 1;
						if (number == answer){
							Random r = new Random();
							int r = points.nextInt(1,5);
							System.out.println("今回は当たれば"+String(r)+"倍になります");
							point8a = (int)point8 * r;
							System.out.println("値は"+String(points)+"でした。当たり!!"+String(point8)+"bet分が"+String(r)+"倍の"+String(point8a)+"pointになりました");
							System.out.println(String(point8a) +"pointになりました。持ちpointはbet分が差し引かれた保有point+(bet point×2)");
							System.out.println("外れたら運用分は0ポイントになります。");
							Filedump(file6,kiguu,point1);
							Filedump(file6,kanri,point8a);
							return 'p';
						}
						else{
							System.out.println("値は"+String(points)+"でした。当たりにならず!!");
							int point8 = 0;
							Filedump(file6,kiguu,point1);
							Filedump(file6,kanri,point8);
							return 'e';
						}
					}
					else if (horl < 0){
						int answer = 2;
						if (number == answer){
								Random r = new Random();
								int r = points.nextInt(1,5);
								int point8a = (int)point8 * r;
								System.out.println("値は"+String(points)+"でした。当たり!!"+String(point8)+"bet分が"+String(r)+"倍になり、bet point控除後のpointに加算されます");
								System.out.println(String(point8a) +"pointになります。現在持ちpointはbet分が差し引かれた保有point+(bet point×2)" );
								System.out.println("外れたら運用分は0ポイントになります。");
								Filedump(file6,kiguu,point1);
								Filedump(file6,kanri,point8a);
								return 'p';
						}else{
								System.out.println("値は"+String(points)+"でした。当たりにならず!!");
								int point8 = 0;
								Filedump(file6,kiguu,point1);
								Filedump(file6,kanri,point8);
								System.out.println(String(point1)+"pointになります。");
								return 'e';
							}
					}else{
						System.out.println("値は"+String(points)+"でした。even!!");
						int point1 = (int)point1;
						Filedump(file6,"",point1);
						return 'p';
					}
				}else{
				System.out.println("選択しなおしてね");
				Filedump(file6,kiguu,point1);
				return 'p';
				}
			}else if (answer == n){
				Filedump(file6,kanri,point8);
				Filedump(file6,"",point1);
				return 'e';
				}
			else{
				System.out.println("選択は無効となりpointは保存されます。");
				Filedump(file6,"",point1);
				return 'p';
			}
		}
		else{
			int point1 = kanri(file6);
			int point7 = (int)point1;
			System.out.println("1～5倍運用挑戦しませんか？");
			System.out.print("please input(y=yes,n=no) :y or n:");
			String answer = scanner.next();
			String y = "y";
			String n = "n";
			if (answer == y){
				System.out.println("kiguuポイントは" + String(point1) + "ポイントあります");
				System.out.println("持ちpointの中からいくら運用しますか？:");
				int bet = scanner.next();
				String bet = String(bet);
				int ans = Character.isAlphabetic(bet);
				String ans = String(ans);
				if (ans == "true"){
					System.out.println("数字を入力してください");
					Filedump(file6,kiguu,point1);
					return 'p';
				}
				else{
					int bet = (int)bet;
					if (bet <= intpoint1 && bet > 0){
						point2 = point1 - bet;
						Random r2 = new Random();
						int r2 = points.nextInt(1,3);
						int point1 = abs(point1);
						int r3 = point7 * r2/3;
						int r3 = (int)r3;
						System.out.println("現在の" + String(point7) + "ポイントの3分の"+String(r2)+",つまり"+String(r3)+"より持ちpoint数字内から無作為に選んだの値は");
						System.out.println("ランダムに出た、数字の傾向は、");
						for(int i = 1; i <= 6; i++){
							Random points = new Random();
							int points = points.nextInt(0,point7);
							System.out.println(String(points));
						}
						System.out.println("となります。次の数字は");
						Random points = new Random();
						int points = points.nextInt(0,point7);
						System.out.println("high(1) or low(2)か?");
						System.out.println("choice,1 or 2:");
						int number = scanner.next();
						int horl = points - point7 * r2/ 3;
						if (number == 1 ||  number == 2){
							if (horl > 0){
								int answer = 1;
								if (number == answer){
									Random r = new Random();
									int r = points.nextInt(1,5);
									System.out.println("今回は当たれば"+String(r)+"倍になります");
									point8 = (int)bet * r;
									System.out.println("値は"+String(points)+"でした。当たり!!"+ String(bet)+"bet分が"+str(r)+"倍になり持ちポイントは" + str(point8) + "になりました");
									System.out.println("外れたら運用分は0ポイントになります。");
									Filedump(file6,kiguu,point2);
									Filedump(file6,kanri,point8);
									return 'p';
								}
								else{
									System.out.println("値は"+String(points)+"でした。当たりにならず!!"); 
									int point8 = 0;
									Filedump(file6,kiguu,point2);
									Filedump(file6,kanri,point8);
									return 'e';
								}
							}
							else if (horl < 0){
								int answer = 2;
								if (number == answer){
									Random r = new Random();
									int r = points.nextInt(1,5);
									int point8 = (int)bet * r;
									int point8 = (int)point8;
									int point1 = point1 - (int)bet;
									System.out.println("値は"+String(points)+"でした。当たり!!"+ String(bet)+"bet分が"+str(r)+"倍になり持ちポイントは" + str(point8) + "になりました");
									System.out.println("外れたら運用分は0ポイントになります。");
									Filedump(file6,kiguu,point2);
									Filedump(file6,kanri,point8);
									return 'p';
								}
								else{
									System.out.println("値は"+String(points)+"でした。当たりにならず!!");
									int point8 = 0;
									Filedump(file6,kiguu,point2);
									Filedump(file6,kanri,point8);
									System.out.println(String(point2)+"pointになります。");
									return 'e';
								}
							}
							else{
								System.out.println("値は"+String(points)+"でした。even!!");
								int point1 = (int)point1;
								int p2 = point1;
								Filedump(file6,kiguu,point1);
								return 'p';
							}
						}
						else{
							System.out.println("選択しなおしてね");
							Filedump(file6,"",point1);
							return 'p';
						}
					}
				}
			}
			else if (answer == n){
				Filedump(file6,kiguu,point1);
				return 'e';
			}
			else{
				System.out.println("選択は無効となりpointは保存されます。");
				Filedump(file6,kiguu,point1);
				return 'p';
			}
		}
	}

	public static void main(String[] args){
		System.out.println("トランプゲームkiguu copyrighted(produced) by NoritsuguHoshizawa");
		System.out.println("point保存する新規Point名(新規ファイル名)または、既存のPoint名(前回のファイル名)をアルファベットから始まる半角英数字を入力してください");
		System.out.print("input:");
		String file = scanner.next();
		System.out.println("偶数0か奇数1か当たればpointを2倍に Let's choice : 0or1 注0,1以外は終了:");
		System.out.println("行動力気持ちの縺れつり合い人生数理意思決定ディール無の境地!!");
		System.out.println("kiguu87の数字の読み方愉しみ方。!  \n9＝’q’uantum or 苦労、8＝破、7=転じて、\n６＝無になれる資質、５＝後、4＝資、３＝産、２＝受信、10=おわり\n１＝送信、０＝目的や汚(けが)れ、１１＝一方通、\n１２＝双方向、１３＝産みを送信,14=資を送信、\n１５＝以後、１６＝色、000=おっさん01=老いる\nDX=13X");
		char answer = kiguu(file);
		while (answer == 'p'){
			char answer = ru(file);
		}
		System.exit(0);
	}
}
