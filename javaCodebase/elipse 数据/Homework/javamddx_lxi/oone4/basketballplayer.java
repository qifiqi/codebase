package oone4;

public class basketballplayer extends player {
	//篮球运动员的类继承player
	public basketballplayer() {
	}
	public basketballplayer(String name, int age) {
		super(name,age);
	}
	@Override
	public void student() {
		System.out.println("篮球运动员要练习运球和投篮技巧");
	}

	@Override
	public void eat() {
		System.out.println("篮球运动员要吃高蛋白的饭菜，保持健壮的身体");		
		student();
	}

}
