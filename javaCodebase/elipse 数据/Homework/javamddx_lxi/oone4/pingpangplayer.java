package oone4;

public class pingpangplayer extends player implements English{
	//ƹ�����˶�Ա����̳�playerʵ��English�ӿ�
	public pingpangplayer() {
	}
	public pingpangplayer(String name, int age) {
		super(name,age);
	}
	@Override
	public void speak() {
		System.out.println("ƹ�����˶�ԱҪѧϰӢ��");	
	}

	@Override
	public void student() {
		System.out.println("ƹ�����˶�ԱҪ��ϰ����ͽ���ļ���");		
		speak();
	}

	@Override
	public void eat() {
		System.out.println("ƹ�����˶�ԱҪ���嵭�ķ���");
		student();
	}



}
