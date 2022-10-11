package homework;
import java.util.Scanner;

public class four {

	public static void main(String[] args) {
		Scanner one = new Scanner(System.in);
		System.out.println("请输入一个数");
		int aa = one.nextInt();
		if (aa % 3 == 0) {
			if (aa % 5 == 0) {
				if (aa % 7 == 0) {
					System.out.println("这个数能被3，5，7整除");
				} else {
					System.out.println("这个数能被3，5整除");
				}
			} else {
				if (aa % 7 == 0) {
					System.out.println("这个数能被3，7整除");
				} else {
					System.out.println("这个数只能被3整除");
				}
			}
		} else {
			if (aa % 5 == 0) {
				if (aa % 7 == 0) {
					System.out.println("这个数能被5，7整除");
				} else {
					System.out.println("这个数只能被5整除");
				}
			} else {
				if (aa % 7 == 0) {
					System.out.println("这个数只能被7整除");
				} else {
					System.out.println("这个数不能被3，5，7整除");
				}
			}
		}

	}

}
