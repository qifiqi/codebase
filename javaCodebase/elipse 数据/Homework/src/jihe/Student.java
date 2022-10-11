package jihe;

public class Student {
	private String name;
	private int studenyld;
	private int grade;
	public Student(String name, int studenyld, int grade) {
		this.name = name;
		this.studenyld = studenyld;
		this.grade = grade;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getStudenyld() {
		return studenyld;
	}
	public void setStudenyld(int studenyld) {
		this.studenyld = studenyld;
	}
	public int getGrade() {
		return grade;
	}
	public void setGrade(int grade) {
		this.grade = grade;
	}
	@Override
	public String toString() {
		return "Student [name=" + name + ", studenyld=" + studenyld + ", grade=" + grade + "]";
	}
	
	
}
