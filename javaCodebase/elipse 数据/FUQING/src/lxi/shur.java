/*
 * 猜数字游戏
请写一个程序实现下述效果
游戏操作如下：
1.后台预先生成一个1-100之间的随机数，用户键盘录入猜数字
2.如果猜对了，打印“恭喜您，答对了”
3.如果猜错了
    猜大了：打印“sorry，您猜大了!”
    猜小了：打印“sorry，您猜小了!”
4.直到数字猜到为止
分析：
不断的可以输入数字，进行比对，猜测正确才能结束（循环）
超过了100,会提示要输入正确的数字（if）
正确的数字有系统随机生成，代码参考如下：
import java.util.*;
/    /创建Random随机数类变量
		Random ran = new Random();
		int ranNumber = ran.nextInt(100)+1;代表随机生成1~100之间的整数
如果猜测数字比正确数字大，进行提示，并且修改提示语句（if）
如果猜测数字正确，输出相关信息，游戏结束，程序结束

 */
package lxi;
import java.util.Random;
import java.util.Scanner;

public class shur {

	public static void main(String[] args) {
		int min, max;
		min = 1;
		max = 100;
		Random ran = new Random();
		int ranNumber = ran.nextInt(100) + 1;
		Scanner scanner = new Scanner(System.in);
		System.out.println("猜数字游戏");
		System.out.println("欢迎你");

		for (int i = 1; i <= 10; i++) {
			System.out.printf("请输入您%d~%d的的数值\n", min, max);
			int shu = scanner.nextInt();
			if(i==7) {
				System.out.println("您，还有3次机会");
				if(shu<100&&shu>0) {
					if (ranNumber == shu) {
						System.out.println("恭喜您，答对了");
						return;
					} else {
						if (ranNumber < shu) {
							System.out.println("sorry，您猜大了!");
							max = shu;
						} else {
							System.out.println("sorry，您猜小了!");
							min = shu;
						}
					}
					}else {
						System.out.println("sorry,请输入正确的数");
					}
				
			}else {
				if(shu<100&&shu>0) {
					if (ranNumber == shu) {
						System.out.println("恭喜您，答对了");
						return;
					} else {
						if (ranNumber < shu) {
							System.out.println("sorry，您猜大了!");
							max = shu;
						} else {
							System.out.println("sorry，您猜小了!");
							min = shu;
						}
					}
					}else {
						System.out.println("sorry,请输入正确的数");
					}
				
			}
		}
		}
}
