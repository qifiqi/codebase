package homework;
import java.util.Scanner;

public class four {

	public static void main(String[] args) {
		Scanner one = new Scanner(System.in);
		System.out.println("������һ����");
		int aa = one.nextInt();
		if (aa % 3 == 0) {
			if (aa % 5 == 0) {
				if (aa % 7 == 0) {
					System.out.println("������ܱ�3��5��7����");
				} else {
					System.out.println("������ܱ�3��5����");
				}
			} else {
				if (aa % 7 == 0) {
					System.out.println("������ܱ�3��7����");
				} else {
					System.out.println("�����ֻ�ܱ�3����");
				}
			}
		} else {
			if (aa % 5 == 0) {
				if (aa % 7 == 0) {
					System.out.println("������ܱ�5��7����");
				} else {
					System.out.println("�����ֻ�ܱ�5����");
				}
			} else {
				if (aa % 7 == 0) {
					System.out.println("�����ֻ�ܱ�7����");
				} else {
					System.out.println("��������ܱ�3��5��7����");
				}
			}
		}

	}

}
