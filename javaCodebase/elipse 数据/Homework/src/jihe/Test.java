package jihe;
public class Test {

	public static void main(String[] args) {
	Student student =new Student("张三", 56464654, 77);
	Student student2 = new Student("李四", 2341234, 84);
	Student student3 = new Student("王五", 23546234, 89);
	Student student4 =new Student("赵六", 12341234, 98);
	StudentOP.arrayList.add(student.getName());
	StudentOP.arrayList.add(student2.getName());
	StudentOP.arrayList.add(student3.getName());
	StudentOP.showinfo();
	int cdu = StudentOP.arrayList.size();
	System.out.println("arrayList的长度有："+cdu);
	StudentOP.showinfo();
	StudentOP.arrayList.remove(1);
	System.out.println("删除第二个同学");
	StudentOP.showinfo();
	StudentOP.arrayList.add(1, student4.getName());
	System.out.println("添加到删除的同学的地方");
	StudentOP.showinfo();
	}

}
