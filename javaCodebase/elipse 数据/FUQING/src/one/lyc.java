package one;
import java.util.Scanner;

public class lyc {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int num;
		int sum = 0;
		System.out.println("������һ����Ȼ����");
		num = sc.nextInt();
		for (int i = 1; i < num; i++) {
			if (num % i == 0)
				sum += i;

		}
		if (sum == num) {
			System.out.printf("%d����ȫ��\n", num);
		} else {
			System.out.printf("%d������ȫ��\n", num);
		}

	}

}
