package oone4;

public class pingpangplayer extends player implements English{
	//乒乓球运动员的类继承player实现English接口
	public pingpangplayer() {
	}
	public pingpangplayer(String name, int age) {
		super(name,age);
	}
	@Override
	public void speak() {
		System.out.println("乒乓球运动员要学习英语");	
	}

	@Override
	public void student() {
		System.out.println("乒乓球运动员要练习发球和接球的技巧");		
		speak();
	}

	@Override
	public void eat() {
		System.out.println("乒乓球运动员要吃清淡的饭菜");
		student();
	}



}
