package homework;
import java.util.Scanner;
public class seven {
	public int  num1() {
		Scanner one = new Scanner(System.in);
		System.out.println("请输入这个学生的成绩：");
		int chngji =one.nextInt();
		return chngji;
	}
	public void num2(int chngji) {
		if(chngji<=100&&chngji>=90) {
			System.out.println("等级为A");
		}else if(chngji<90&&chngji>=80) {
			System.out.println("等级为B");
		}else if(chngji<80&&chngji>=70) {
			System.out.println("等级为C");
		}else if(chngji<70&&chngji>=60) {
			System.out.println("等级为D");
		}else if(chngji<60&&chngji>=0) {
			System.out.println("等级为E");
		}else {
			System.out.println("Score is error!");
		}
	}
	public static void main(String[] args) {
		seven ff =new seven();
		int chngji = ff.num1();
		ff.num2(chngji);
	}

}
