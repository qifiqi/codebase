package oone4;

public class basketballcoach extends coach {
	//篮球教练员的类继承coach
	public basketballcoach() {
	}
	public basketballcoach(String name, int age) {
		super(name,age);
	}
	@Override
	public void teacher() {
		System.out.println("篮球教练员要教篮球运动员练习运球和投篮技巧");
	}

	@Override
	public void eat() {
		System.out.println("篮球教练员要跟着篮球运动员吃高蛋白的饭菜。");		
		teacher();
	}

}
