package zy;

import java.util.Scanner;

public class Barracks {
	static int count;
	String name;
	int selfCount;

	public Barracks(String name, int selfCount) {
		this.name = name;
		this.selfCount = selfCount;
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("�����һ����Ӫ����:\n��Ӫ���ж��ٸ���");
		String name = scanner.next();
		int selfCount = scanner.nextInt();
		Barracks aaBarracks = new Barracks(name, selfCount);
		System.out.println("����ڶ�����Ӫ����:\n��Ӫ���ж��ٸ���");
		name = scanner.next();
		selfCount = scanner.nextInt();
		Barracks aBarracks = new Barracks(name, selfCount);
		System.out.println("�����������Ӫ����:\n��Ӫ���ж��ٸ���");
		name = scanner.next();
		selfCount = scanner.nextInt();
		Barracks aaaBarracks = new Barracks(name, selfCount);
		count = aaaBarracks.selfCount+aBarracks.selfCount+aaBarracks.selfCount;
		System.out.println(count);
	}

}
