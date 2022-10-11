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
	 * 添加用的构造函数，没有id
	 * @param personnel_name	用户名
	 * @param phone	手机号码
	 * @param sex	性别
	 * @param department	部门
	 * @param age	年龄
	 * @param salary	工资
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
	 * 查询结果使用的构造函数
	 * @param personnel_id	用户id
	 * @param personnel_name	用户名
	 * @param phone	手机号码
	 * @param sex	性别
	 * @param department	部门
	 * @param age	年龄
	 * @param salary	工资
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
