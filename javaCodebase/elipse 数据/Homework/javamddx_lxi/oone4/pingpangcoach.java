package oone4;

public class pingpangcoach extends coach implements English{
	//ƹ�������Ա����̳�coachʵ��English�ӿ�
	public pingpangcoach() {
	}
	public pingpangcoach(String name, int age) {
		super(name,age);
	}
	@Override
	public void speak() {
		System.out.println("ƹ�������ԱҪѧϰӢ��");		
		
	}

	@Override
	public void teacher() {
		System.out.println("ƹ�������ԱҪ��ƹ�����Ա����ͽ���ļ���");
		speak();
	}

	@Override
	public void eat() {
		System.out.println("ƹ�����˶�ԱҪ���嵭�ķ���");
		teacher();
	}

}
