package one;
import java.util.Scanner;

public class ifANDelse {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner fu = new Scanner(System.in);
		System.out.println("���������䣺");
		int num1 = fu.nextInt();
		System.out.println("�������Ա�");
		char num2 = fu.next().charAt(0);
		if (num2 == '��') {
			if (num1 >= 30) {
				System.out.println("����");
				System.out.println("û��Ҫ");
			} else {
				System.out.println("С����");
				System.out.println("���ǻ���û��Ҫ");
			}
		} else {
			if (num1 >= 30) {
				System.out.println("ʣŮ�����Ǵ����");
				System.out.println("���ǲ�֪���ǲ��Ǹ���");
			} else {
				System.out.println("����С���ᣬ���Ǿ���û�б�Ǯ");
				System.out.println("��֪���ǲ��Ǽ������ֻ��Ǹ���");
			}
		}

	}

}
