package jihe;
public class Test {

	public static void main(String[] args) {
	Student student =new Student("����", 56464654, 77);
	Student student2 = new Student("����", 2341234, 84);
	Student student3 = new Student("����", 23546234, 89);
	Student student4 =new Student("����", 12341234, 98);
	StudentOP.arrayList.add(student.getName());
	StudentOP.arrayList.add(student2.getName());
	StudentOP.arrayList.add(student3.getName());
	StudentOP.showinfo();
	int cdu = StudentOP.arrayList.size();
	System.out.println("arrayList�ĳ����У�"+cdu);
	StudentOP.showinfo();
	StudentOP.arrayList.remove(1);
	System.out.println("ɾ���ڶ���ͬѧ");
	StudentOP.showinfo();
	StudentOP.arrayList.add(1, student4.getName());
	System.out.println("��ӵ�ɾ����ͬѧ�ĵط�");
	StudentOP.showinfo();
	}

}
