
/*
 * 创建Dota游戏中的兵营类（Barracks）
兵营类有一个类成员变量count、一个实例变量name和另一个实例变量selfCount。
count表示的是兵营已经创建士兵的总数；name表示的是每个兵营的名称；selfCount表示每个兵营已经创建的士兵数量。
创建3个兵营，通过控制台为每个兵营定义兵营名称，并指定该兵营需要创建的士兵人数。
在主方法中输出当前兵营中的总人数。
特殊要求：
将兵营类中的name，selfCount属性设置为私有访问权限。
将兵营类中所有属性的赋值方法设置为公有访问权限。
要求兵营名称的长度在4～8位之间。
要求兵营士兵的人数在100～500之间。

 */
package zy;
import java.util.Scanner;

public class Barrack {
	static int  count=0;
	private String name;
	private int selfCount;
	public void name(String name) {
	if (name.length()>=4&&name.length()<=8) {
		System.out.println("军营名字是："+name);
	}else {
		System.out.println("错误不在范围");
	}	
	}
	public void selfCount(int selfCount) {
		if (selfCount<=500&&selfCount>=100) {
			System.out.println("在范围");
		}else {
			System.out.println("不在范围");
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
			System.out.println("输入第"+i+"个兵营的名字:");
			barracks.name=scanner.next();
			barracks.name(barracks.getname());
			System.out.println("请输入这个军营的士兵人数:");
			barracks.selfCount=scanner.nextInt();
			barracks.selfCount(barracks.getselfCount());
			count +=barracks.getselfCount(); 
		}
		System.out.println(count);
	}

}
