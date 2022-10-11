package homework;
import java.util.Scanner;

public class there {
	public boolean num1(int a) {
		if (a <= 999 && a > 99) {
			int one = a % 10;// 个位
			int two = a / 10 % 10;// 十位
			int there = a / 100 % 10;
			int he = (one * one * one + two * two * two + there * there * there);
			if (he == a) {
				return true;
			}
		}
		return false;

	}

	public static void main(String[] args) {
		Scanner one = new Scanner(System.in);
		there two = new there();
		System.out.println("请输入一个三位数：");
		int a = one .nextInt();
		boolean cc = two.num1(a);
		if(cc) {
			System.out.println("输入的这个三位数是水仙花数");	
		}else {
			System.out.println("输入的这个三位数不是水仙花数");
		}

	}

}
