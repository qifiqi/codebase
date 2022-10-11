package one;

public class MyMath {
	static int num1, num2;

	public int mymath(int a, int b) {
		if (a > b) {
			System.out.println("max" + a);
			return a;
		} else {
			System.out.println("max" + b);
			return b;
		}
	}

	public void mymath1(int n) {
		if (1 < n && n < 100) {
			System.out.println("ok");

		} else {
			System.out.println("not  ok");

		}
	}

	public int mymath2() {
		num1 = 0;
		for (num2 = 1; num2 <= 100; num2++) {
			num1 += num2;
		}
		return num1;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MyMath mymath3 = new MyMath();
		mymath3.num1 = 0;
		mymath3.num2 = 1;
		mymath3.mymath(322, 234);
		mymath3.mymath1(89);
		mymath3.mymath2();
		System.out.println("1到100 的和为：" + num1);

	}

}
