package oone4;

public abstract class  person {
	//一个抽象类
	//有显示年龄等属性的方法 
	String name;
	int age;
	public person() {
		super();
	}
	public person(String name, int age) {
		super();
		this.name = name;
		this.age = age;
	}
	public abstract void eat();
	public void show() {
		System.out.printf("姓名是：%s\t年龄是:%d\n",name,age);
	}
}
