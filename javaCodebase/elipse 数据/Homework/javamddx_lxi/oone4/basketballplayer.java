package oone4;

public class basketballplayer extends player {
	//�����˶�Ա����̳�player
	public basketballplayer() {
	}
	public basketballplayer(String name, int age) {
		super(name,age);
	}
	@Override
	public void student() {
		System.out.println("�����˶�ԱҪ��ϰ�����Ͷ������");
	}

	@Override
	public void eat() {
		System.out.println("�����˶�ԱҪ�Ըߵ��׵ķ��ˣ����ֽ�׳������");		
		student();
	}

}
