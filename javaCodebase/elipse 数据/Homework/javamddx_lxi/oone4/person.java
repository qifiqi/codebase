package oone4;

public abstract class  person {
	//һ��������
	//����ʾ��������Եķ��� 
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
		System.out.printf("�����ǣ�%s\t������:%d\n",name,age);
	}
}
