
/*
 * ����Dota��Ϸ�еı�Ӫ�ࣨBarracks��
��Ӫ����һ�����Ա����count��һ��ʵ������name����һ��ʵ������selfCount��
count��ʾ���Ǳ�Ӫ�Ѿ�����ʿ����������name��ʾ����ÿ����Ӫ�����ƣ�selfCount��ʾÿ����Ӫ�Ѿ�������ʿ��������
����3����Ӫ��ͨ������̨Ϊÿ����Ӫ�����Ӫ���ƣ���ָ���ñ�Ӫ��Ҫ������ʿ��������
���������������ǰ��Ӫ�е���������
����Ҫ��
����Ӫ���е�name��selfCount��������Ϊ˽�з���Ȩ�ޡ�
����Ӫ�����������Եĸ�ֵ��������Ϊ���з���Ȩ�ޡ�
Ҫ���Ӫ���Ƶĳ�����4��8λ֮�䡣
Ҫ���Ӫʿ����������100��500֮�䡣

 */
package zy;
import java.util.Scanner;

public class Barrack {
	static int  count=0;
	private String name;
	private int selfCount;
	public void name(String name) {
	if (name.length()>=4&&name.length()<=8) {
		System.out.println("��Ӫ�����ǣ�"+name);
	}else {
		System.out.println("�����ڷ�Χ");
	}	
	}
	public void selfCount(int selfCount) {
		if (selfCount<=500&&selfCount>=100) {
			System.out.println("�ڷ�Χ");
		}else {
			System.out.println("���ڷ�Χ");
		}
	}
	public String getname() {
		return name ;
	}
	public int getselfCount() {
		return selfCount;
	}

	public static void main(String[] args) {
		Barrack barracks=new Barrack();
		Scanner scanner =new Scanner(System.in);
		count=0;
		for (int i =1 ;i<=3;i++) {
			System.out.println("�����"+i+"����Ӫ������:");
			barracks.name=scanner.next();
			barracks.name(barracks.getname());
			System.out.println("�����������Ӫ��ʿ������:");
			barracks.selfCount=scanner.nextInt();
			barracks.selfCount(barracks.getselfCount());
			count +=barracks.getselfCount(); 
		}
		System.out.println(count);
	}

}
