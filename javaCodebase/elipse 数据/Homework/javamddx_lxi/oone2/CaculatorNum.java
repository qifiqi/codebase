package oone2;

public class CaculatorNum {
	int num1;
	int num2;
	char operator;
	public int getNum1() {
		return num1;
	}
	public void setNum1(int num1) {
		this.num1 = num1;
	}
	public int getNum2() {
		return num2;
	}
	public void setNum2(int num2) {
		this.num2 = num2;
	}
	public char getOperator() {
		return operator;
	}
	public void setOperator(char operator) {
		this.operator = operator;
	}
	public void caculate(char operator) {
		switch (operator) {
		case '+':
			int a=Tools.add(num1, num2);
			System.out.println("输出结果是"+a);
			break;
        case '-':
        	int b=Tools.minus(num1, num2);
			System.out.println("输出结果是"+b);
			break;
		case '/':
			int c=Tools.divide(num1, num2);
			System.out.println("输出结果是"+c);
			break;
		case '*':
			int d=Tools.multiplicate(num1, num2);
			System.out.println("输出结果是"+d);
			break;
		default:
			System.out.println("不在范围");
			break;
		}
	}
}
