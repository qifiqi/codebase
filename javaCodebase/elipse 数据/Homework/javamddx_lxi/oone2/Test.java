package oone2;

import java.util.Scanner;

public class Test {

	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner scanner=new Scanner(System.in);
		CaculatorNum  caculatorNum =new CaculatorNum();
		System.out.println("�������һ����");
		int a =scanner.nextInt(); 
		System.out.println("������ڶ�����");
		int b=scanner.nextInt();
		System.out.println("��������ַ�");
		char c=scanner.next().charAt(0);
		caculatorNum.setNum1(a);
		caculatorNum.setNum2(b);
		caculatorNum.setOperator(c);
		caculatorNum.caculate(caculatorNum.getOperator());
		
	}

}
