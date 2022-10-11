package com.lz.dao;

import com.lz.entity.Student;

public class StudentDAO extends BaseDAO{

	//查询全部的学生信息
	public Object[][] FindAll(){
		
		String sql="select * from student";
		return this.Find(sql);
	}
	public boolean AddStudent(Student stu) {
		
		String sql="insert into student(name,age,sex,address) values(?,?,?,?)";
		Object[] obj= {stu.getName(),stu.getAge(),stu.getSex(),stu.getAddress()};
		return this.Execute(sql, obj);
	}
	public boolean Remove(int id) {
		String sql="delete from student where id=?";
		return this.Execute(sql, new Object[]{id});
	}
}
