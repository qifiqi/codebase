package oone4;

public  abstract class coach extends person{
	//½ÌÁ·µÄÀà¼Ì³Ğperson
    public coach() {
	}
	public coach(String name, int age) {
		super(name,age);
	}
	public abstract void teacher();
}
