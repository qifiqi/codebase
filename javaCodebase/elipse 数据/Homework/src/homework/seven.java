package homework;
import java.util.Scanner;
public class seven {
	public int  num1() {
		Scanner one = new Scanner(System.in);
		System.out.println("���������ѧ���ĳɼ���");
		int chngji =one.nextInt();
		return chngji;
	}
	public void num2(int chngji) {
		if(chngji<=100&&chngji>=90) {
			System.out.println("�ȼ�ΪA");
		}else if(chngji<90&&chngji>=80) {
			System.out.println("�ȼ�ΪB");
		}else if(chngji<80&&chngji>=70) {
			System.out.println("�ȼ�ΪC");
		}else if(chngji<70&&chngji>=60) {
			System.out.println("�ȼ�ΪD");
		}else if(chngji<60&&chngji>=0) {
			System.out.println("�ȼ�ΪE");
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
