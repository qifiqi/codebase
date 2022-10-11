package one;
import java.util.Scanner;

public class ifANDelse {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner fu = new Scanner(System.in);
		System.out.println("请输入年龄：");
		int num1 = fu.nextInt();
		System.out.println("请输入性别：");
		char num2 = fu.next().charAt(0);
		if (num2 == '男') {
			if (num1 >= 30) {
				System.out.println("单身狗");
				System.out.println("没人要");
			} else {
				System.out.println("小鲜肉");
				System.out.println("但是还是没人要");
			}
		} else {
			if (num1 >= 30) {
				System.out.println("剩女，还是大龄的");
				System.out.println("就是不知道是不是富婆");
			} else {
				System.out.println("不错小年轻，但是就是没有本钱");
				System.out.println("不知道是不是即年轻又还是富婆");
			}
		}

	}

}
