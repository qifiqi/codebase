package oone2;

import java.util.Scanner;

public class Test {

	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner scanner=new Scanner(System.in);
		CaculatorNum  caculatorNum =new CaculatorNum();
		System.out.println("请输入第一个数");
		int a =scanner.nextInt(); 
		System.out.println("请输入第二个数");
		int b=scanner.nextInt();
		System.out.println("输入操作字符");
		char c=scanner.next().charAt(0);
		caculatorNum.setNum1(a);
		caculatorNum.setNum2(b);
		caculatorNum.setOperator(c);
		caculatorNum.caculate(caculatorNum.getOperator());
		
	}

}
