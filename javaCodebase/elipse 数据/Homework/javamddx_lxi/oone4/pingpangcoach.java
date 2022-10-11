package oone4;

public class pingpangcoach extends coach implements English{
	//乒乓球教练员的类继承coach实现English接口
	public pingpangcoach() {
	}
	public pingpangcoach(String name, int age) {
		super(name,age);
	}
	@Override
	public void speak() {
		System.out.println("乒乓球教练员要学习英语");		
		
	}

	@Override
	public void teacher() {
		System.out.println("乒乓球教练员要教乒乓球队员发球和接球的技巧");
		speak();
	}

	@Override
	public void eat() {
		System.out.println("乒乓球运动员要吃清淡的饭菜");
		teacher();
	}

}
