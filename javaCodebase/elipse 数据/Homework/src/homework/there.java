package homework;
import java.util.Scanner;

public class there {
	public boolean num1(int a) {
		if (a <= 999 && a > 99) {
			int one = a % 10;// ��λ
			int two = a / 10 % 10;// ʮλ
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
		System.out.println("������һ����λ����");
		int a = one .nextInt();
		boolean cc = two.num1(a);
		if(cc) {
			System.out.println("����������λ����ˮ�ɻ���");	
		}else {
			System.out.println("����������λ������ˮ�ɻ���");
		}

	}

}
