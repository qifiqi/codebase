package one;
import java.util.Scanner;

public class whileANDInterest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner fu = new Scanner(System.in);
		System.out.println("请输入你的本金：");
		double num1 = fu.nextDouble();
		System.out.println("请输入你的利率:");
		double num2 = fu.nextDouble();
		int num3 = 0;
		System.out.println("请输入你想要的金额:");
		double num4 = fu.nextDouble();
		while (num1 <= num4) {
			num1 += num1 * num2;
			num3++;
			System.out.printf("%d年月日之后，本金：%.2f\n", num3, num1);
		}
		System.out.println("存款" + num3 + "后，本金超过了你想要的金额");

	}

}
