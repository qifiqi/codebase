package oone4;

public class basketballcoach extends coach {
	//�������Ա����̳�coach
	public basketballcoach() {
	}
	public basketballcoach(String name, int age) {
		super(name,age);
	}
	@Override
	public void teacher() {
		System.out.println("�������ԱҪ�������˶�Ա��ϰ�����Ͷ������");
	}

	@Override
	public void eat() {
		System.out.println("�������ԱҪ���������˶�Ա�Ըߵ��׵ķ��ˡ�");		
		teacher();
	}

}
