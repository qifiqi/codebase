package one;
import java.util.Scanner;

public class whileANDInterest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner fu = new Scanner(System.in);
		System.out.println("��������ı���");
		double num1 = fu.nextDouble();
		System.out.println("�������������:");
		double num2 = fu.nextDouble();
		int num3 = 0;
		System.out.println("����������Ҫ�Ľ��:");
		double num4 = fu.nextDouble();
		while (num1 <= num4) {
			num1 += num1 * num2;
			num3++;
			System.out.printf("%d������֮�󣬱���%.2f\n", num3, num1);
		}
		System.out.println("���" + num3 + "�󣬱��𳬹�������Ҫ�Ľ��");

	}

}
