package com.pan.exam.model;

public class Personnel {
	private int personnel_id ;
	private String  personnel_name ;
	private String phone ;
	private String sex ;
	private String department ;
	private int age ;
	private Double salary ;
	
	
	/**
	 * ����õĹ��캯����û��id
	 * @param personnel_name	�û���
	 * @param phone	�ֻ�����
	 * @param sex	�Ա�
	 * @param department	����
	 * @param age	����
	 * @param salary	����
	 */
	public Personnel(String personnel_name, String phone, String sex, String department, int age, Double salary) {
		super();
		this.personnel_name = personnel_name;
		this.phone = phone;
		this.sex = sex;
		this.department = department;
		this.age = age;
		this.salary = salary;
	}
	
	/**
	 * ��ѯ���ʹ�õĹ��캯��
	 * @param personnel_id	�û�id
	 * @param personnel_name	�û���
	 * @param phone	�ֻ�����
	 * @param sex	�Ա�
	 * @param department	����
	 * @param age	����
	 * @param salary	����
	 */
	
	public Personnel(int personnel_id, String personnel_name, String phone, String sex, String department, int age,
			Double salary) {
		super();
		this.personnel_id = personnel_id;
		this.personnel_name = personnel_name;
		this.phone = phone;
		this.sex = sex;
		this.department = department;
		this.age = age;
		this.salary = salary;
	}
	public int getPersonnel_id() {
		return personnel_id;
	}
	public void setPersonnel_id(int personnel_id) {
		this.personnel_id = personnel_id;
	}
	public String getPersonnel_name() {
		return personnel_name;
	}
	public void setPersonnel_name(String personnel_name) {
		this.personnel_name = personnel_name;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}
	public String getDepartment() {
		return department;
	}
	public void setDepartment(String department) {
		this.department = department;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public Double getSalary() {
		return salary;
	}
	public void setSalary(Double salary) {
		this.salary = salary;
	}

}
