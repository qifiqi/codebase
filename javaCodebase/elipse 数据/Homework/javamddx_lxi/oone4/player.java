package oone4;

public abstract class player extends person {
	//�˶�Ա����̳�person
	public player() {
	}
	public player(String name, int age) {
		super(name,age);
	}
	public abstract void student();
}
