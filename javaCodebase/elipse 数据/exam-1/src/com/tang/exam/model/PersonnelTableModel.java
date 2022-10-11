package com.tang.exam.model;

import java.util.ArrayList;
import java.util.EventListener;


import javax.swing.table.AbstractTableModel;

public  class PersonnelTableModel  extends AbstractTableModel{
	private ArrayList<Object[]> data;
	private final String[] columnNames= {"�û�ID","�û�����","�ֻ�����","�Ա�","����","��������","��������"};
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
	 * ����
	 */
	@Override
	public int getRowCount() {
		// TODO Auto-generated method stub
		return this.data.size();
	}
	
	/**
	 * ����
	 */
	@Override
	public int getColumnCount() {
		// TODO Auto-generated method stub
		return columnNames.length;
	}
	
	/**
	 * ĳ��ĳ�е�����
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