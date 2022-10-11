package com.pan.exam.page;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

import com.pan.exam.dao.PersonnelDao;
import com.pan.exam.model.Personnel;
import com.pan.exam.model.PersonnelTableModel;

import javax.swing.JLabel;
import javax.swing.JOptionPane;

import java.awt.Font;
import javax.swing.SwingConstants;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.awt.event.ActionEvent;

public class MainFrame extends JFrame {

	private JPanel contentPane;
	private JTextField search_field;
	private JTable table;
	private JTextField name_field;
	private JTextField phone_field;
	private JTextField age_field;
	private JTextField salary_field;
	private JComboBox<String> sex_box;
	private JComboBox<String> department_box;
	
	private PersonnelDao personnelDao;
	/**
	 * Create the frame.
	 */
	public MainFrame() {
		personnelDao = new PersonnelDao();
		
		setTitle("员工管理系统");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 1049, 462);
		setMinimumSize(new Dimension(1049,462));
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		search_field = new JTextField();
		search_field.setBounds(62, 10, 244, 21);
		contentPane.add(search_field);
		search_field.setColumns(10);
		
		JButton search_btn= new JButton("\u641C\u7D22");
		search_btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				actionSearch(e);
			}
		});
		search_btn.setBounds(330, 9, 93, 23);
		contentPane.add(search_btn);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(23, 56, 639, 309);
		contentPane.add(scrollPane);
		
		table = new JTable();
		table.setModel(new PersonnelTableModel(personnelDao.search(null)));
		scrollPane.setViewportView(table);
		
		JLabel lblNewLabel = new JLabel("\u5458\u5DE5\u4FE1\u606F");
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setFont(new Font("宋体", Font.BOLD, 20));
		lblNewLabel.setBounds(742, 31, 86, 23);
		contentPane.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("\u5458\u5DE5\u59D3\u540D\uFF1A");
		lblNewLabel_1.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1.setBounds(691, 75, 75, 21);
		contentPane.add(lblNewLabel_1);
		
		name_field = new JTextField();
		name_field.setBounds(801, 75, 131, 21);
		contentPane.add(name_field);
		name_field.setColumns(10);
		
		JLabel lblNewLabel_1_1 = new JLabel("\u5458\u5DE5\u53F7\u7801\uFF1A");
		lblNewLabel_1_1.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1_1.setBounds(691, 116, 75, 21);
		contentPane.add(lblNewLabel_1_1);
		
		JLabel lblNewLabel_1_2 = new JLabel("\u6027   \u522B\uFF1A");
		lblNewLabel_1_2.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1_2.setBounds(691, 155, 75, 21);
		contentPane.add(lblNewLabel_1_2);
		
		JLabel lblNewLabel_1_3 = new JLabel("\u5E74   \u9F84\uFF1A");
		lblNewLabel_1_3.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1_3.setBounds(691, 196, 75, 21);
		contentPane.add(lblNewLabel_1_3);
		
		JLabel lblNewLabel_1_4 = new JLabel("\u57FA\u672C\u5DE5\u8D44\uFF1A");
		lblNewLabel_1_4.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1_4.setBounds(691, 238, 75, 21);
		contentPane.add(lblNewLabel_1_4);
		
		JLabel lblNewLabel_1_4_1 = new JLabel("\u5458\u5DE5\u90E8\u95E8\uFF1A");
		lblNewLabel_1_4_1.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1_4_1.setBounds(691, 286, 75, 21);
		contentPane.add(lblNewLabel_1_4_1);
		
		phone_field = new JTextField();
		phone_field.setColumns(10);
		phone_field.setBounds(801, 116, 131, 21);
		contentPane.add(phone_field);
		
		age_field = new JTextField();
		age_field.setColumns(10);
		age_field.setBounds(801, 196, 131, 21);
		contentPane.add(age_field);
		
		salary_field = new JTextField();
		salary_field.setColumns(10);
		salary_field.setBounds(801, 238, 131, 21);
		contentPane.add(salary_field);
		
		sex_box = new JComboBox();
		sex_box.setModel(new DefaultComboBoxModel(new String[] {"\u7537", "\u5973"}));
		sex_box.setBounds(801, 154, 131, 23);
		contentPane.add(sex_box);
		
		department_box = new JComboBox();
		department_box.setModel(new DefaultComboBoxModel(new String[] {"\u7814\u53D1\u90E8", "\u4EBA\u4E8B\u90E8", "\u8FD0\u8425\u90E8", "\u5F00\u53D1\u90E8"}));
		department_box.setBounds(801, 285, 131, 23);
		contentPane.add(department_box);
		
		JButton submit_btn = new JButton("\u63D0\u4EA4");
		submit_btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				actionSubmit(e);
			}
		});
		submit_btn.setBounds(753, 328, 93, 23);
		contentPane.add(submit_btn);
		
		JButton delete_btn = new JButton("\u5220\u9664");
		delete_btn.setBounds(76, 378, 93, 23);
		delete_btn.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				actionDelete(e);
				
			}
			
		});
		contentPane.add(delete_btn);
	}
	protected void actionDelete(ActionEvent e) {
		int selectedRow  = this.table.getSelectedRow();
		if(selectedRow < 0) {
			JOptionPane.showMessageDialog(this,"请选择需要删除的用户","警告",JOptionPane.WARNING_MESSAGE);
		}else {
			String name = (String)this.table.getModel().getValueAt(selectedRow,1);
			int result = JOptionPane.showConfirmDialog(this,"确定删除："+name+"吗？","提示",JOptionPane.YES_NO_CANCEL_OPTION);
		    if(result == 0) {//点击了是的按钮
		    	int id = (int)this.table.getModel().getValueAt(selectedRow,0);
		    	personnelDao.delete(id);
		    	JOptionPane.showMessageDialog(this,"删除成功！","提示",JOptionPane.INFORMATION_MESSAGE);
		    	this.updateTable();
		    }
		}
	}
	
	protected void actionSearch(ActionEvent e) {
		this.updateTable();
	}
	
	
	

	
	/**
	 * 添加按钮的事件方法
	 * @param e
	 */
	

	protected void actionSubmit(ActionEvent e) {
		System.out.println("提交按钮被点击了");
		//获取用户名输入框的值，并且去除前后的空格
		String name = this.name_field.getText().trim();
		if ("".equals(name)) {
			//如果内容为空，这个弹窗警告，并且结束方法，什么都不做
			JOptionPane.showMessageDialog(this,"用户名不能为空！","警告",JOptionPane.WARNING_MESSAGE);
			return;
		}
	//获取手机号并判断
		String phone = this.phone_field.getText().trim();
		if ("".equals(phone)) {
			JOptionPane.showConfirmDialog(this,"手机号码不能为空！","警告",JOptionPane.WARNING_MESSAGE);
			return;
		}
		//获取年龄并处理异常
		int age = 0 ;
		try {
			 age = Integer.parseInt(this.age_field.getText().trim());
		} catch (NumberFormatException e2) {
			System.err.println("年龄未输入");
		}
			
		//获取性别和部门选择
		String sex = this.sex_box.getSelectedItem().toString();
		String department = this.department_box.getSelectedItem().toString();
		//获取工资输入并判断输入异常
		Double salary = 0.0;
		try {
			 salary = Double.parseDouble(this.salary_field.getText().trim());

		} catch (NumberFormatException e2) {
			JOptionPane.showMessageDialog(this,"请输入正确的工资！","警告",JOptionPane.WARNING_MESSAGE);
		return;
		}
		//将所有的输入封装为一个用户对象
		Personnel personnel = new Personnel(name, phone, sex, department, age, salary);
	    if (personnelDao.add(personnel)) {
	    	JOptionPane.showMessageDialog(this,"添加成功","成功", JOptionPane.INFORMATION_MESSAGE);
	        this.updateTable();
	    }else {
	    	JOptionPane.showMessageDialog(this,"添加成功","失败", JOptionPane.ERROR_MESSAGE);

		}
	}
    
	/**
	 * 清理掉输入框内容
	 */
	
	private void clearInput() {
    	this.name_field.setText("");
    	this.phone_field.setText("");
    	this.department_box.setSelectedIndex(0);
    	this.sex_box.setSelectedIndex(0);
    	this.salary_field.setText("");
    	this.age_field.setText("");
    }
	
	/**
	 * 更新表格的数据
	 */
	private void updateTable() {
		//判断搜索输入框里面没有内容，如果是有内容，则代表当前是搜索的状态，刷新数据也是刷新搜索的数据
		String text = this.search_field.getText().trim();
		if("".equals(text)) {
			this.table.setModel(new PersonnelTableModel(personnelDao.getAll()));
		
		}else {
			this.table.setModel(new PersonnelTableModel(personnelDao.search(text)));

		}
		
	}
}
