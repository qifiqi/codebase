package com.tang.exam.model;

import java.util.ArrayList;
import java.util.EventListener;


import javax.swing.table.AbstractTableModel;

public  class PersonnelTableModel  extends AbstractTableModel{
	private ArrayList<Object[]> data;
	private final String[] columnNames= {"用户ID","用户姓名","手机号码","性别","年龄","基本工资","所属部门"};
	public PersonnelTableModel(ArrayList<Personnel> lists) {
		super();
		data = new ArrayList<>();
		for (Personnel personnel : lists) {
			data.add(new Object[] {
				personnel.getPersonnel_id(),
				personnel.getPersonnel_name(),
				personnel.getPhone(),
				personnel.getSex(),
				personnel.getAge(),
				personnel.getSalary(),
				personnel.getDepartment()
			});
			
		}
	}
	/**
	 * 列数
	 */
	@Override
	public int getRowCount() {
		// TODO Auto-generated method stub
		return this.data.size();
	}
	
	/**
	 * 列数
	 */
	@Override
	public int getColumnCount() {
		// TODO Auto-generated method stub
		return columnNames.length;
	}
	
	/**
	 * 某行某列的数据
	 */
	@Override
	public Object getValueAt(int rowIndex, int columnIndex) {
		// TODO Auto-generated method stub
		return this.data.get(rowIndex)[columnIndex];
	}
	@Override
	public String getColumnName(int column) {
		// TODO Auto-generated method stub
		return columnNames[column];
	}
	
	
	
}