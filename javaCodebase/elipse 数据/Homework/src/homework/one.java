package homework;
import java.util.Scanner;

public class one {
	static int nian;
	static int yfeng;
	static int r;
	static int shu = 0;

	public int num1(int nian, int yfeng, int r) {
		for (int i = 1; i < yfeng; i++) {
			switch (i) {
			case 1:
			case 3:
			case 5:
			case 7:
			case 9:
			case 11:
				shu += 31;
				break;
			case 4:
			case 6:
			case 8:
			case 10:
			case 12:
				shu += 30;
			case 2:
				if ((nian % 4 == 0 && nian % 100 != 0) || (nian % 400 == 0)) {
					shu += 29;
					break;
				} else {
					shu += 28;
					break;
				}
			}
		}
		return shu += r;
	}

	public static void main(String[] args) {
		Scanner dd = new Scanner(System.in);
		System.out.println("请输入年");
		nian = dd.nextInt();
		System.out.println("请输入月份");
		yfeng = dd.nextInt();
		System.out.println("请输入日");
		r = dd.nextInt();
		one ff = new one();
		ff.num1(nian, yfeng, r);
		System.out.printf("%d年%d月%d日是这一年的第%d天", nian, yfeng, r, shu);
	}

}
