import java.util.Scanner;

public class xitone {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner fu = new Scanner(System.in);
		int a, b;
		int c = 0;
		System.out.println("请输入你要计算的值");
		a = fu.nextInt();
		for (int i = 1, j = 2; i < 2 * a - 1; i += 2, j += 2) {
			c += i - j;

		}
		System.out.println("值是" + c);

	}

}
