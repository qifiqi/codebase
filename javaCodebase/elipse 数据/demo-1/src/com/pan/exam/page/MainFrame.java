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

import com.pan.exam.model.Personnel;


import javax.swing.JLabel;
import javax.swing.JOptionPane;

import java.awt.Font;
import javax.swing.SwingConstants;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MainFrame extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JTable table;
	private JTextField name_field;
	private JTextField phone_field;
	private JTextField age_field;
	private JTextField salary_field;
	private JComboBox<String> sex_box;
	private JComboBox<String> department_box;
	
	/**
	 * Create the frame.
	 */
	public MainFrame() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 864, 458);
		setMinimumSize(new Dimension(864,458));
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		textField = new JTextField();
		textField.setBounds(62, 10, 244, 21);
		contentPane.add(textField);
		textField.setColumns(10);
		
		JButton search_field = new JButton("\u641C\u7D22");
		search_field.setBounds(330, 9, 93, 23);
		contentPane.add(search_field);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(23, 54, 510, 312);
		contentPane.add(scrollPane);
		
		table = new JTable();
		table.setModel(new DefaultTableModel(
			new Object[][] {
				{null, null, null, null, null, null, null},
				{null, null, null, null, null, null, null},
				{null, null, null, null, null, null, null},
				{null, null, null, null, null, null, null},
				{null, null, null, null, null, null, null},
				{null, null, null, null, null, null, null},
				{null, null, null, null, null, null, null},
			},
			new String[] {
				" \u5458\u5DE5ID", "\u5458\u5DE5\u59D3\u540D", "\u624B\u673A\u53F7\u7801", "\u6027\u522B", "\u5E74\u9F84", "\u57FA\u672C\u5DE5\u8D44", "\u6240\u5728\u90E8\u95E8"
			}
		));
		scrollPane.setViewportView(table);
		
		JLabel lblNewLabel = new JLabel("\u5458\u5DE5\u4FE1\u606F");
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setFont(new Font("宋体", Font.BOLD, 20));
		lblNewLabel.setBounds(634, 38, 86, 23);
		contentPane.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("\u5458\u5DE5\u59D3\u540D\uFF1A");
		lblNewLabel_1.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1.setBounds(566, 75, 75, 21);
		contentPane.add(lblNewLabel_1);
		
		name_field = new JTextField();
		name_field.setBounds(660, 75, 131, 21);
		contentPane.add(name_field);
		name_field.setColumns(10);
		
		JLabel lblNewLabel_1_1 = new JLabel("\u5458\u5DE5\u53F7\u7801\uFF1A");
		lblNewLabel_1_1.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1_1.setBounds(566, 116, 75, 21);
		contentPane.add(lblNewLabel_1_1);
		
		JLabel lblNewLabel_1_2 = new JLabel("\u6027   \u522B\uFF1A");
		lblNewLabel_1_2.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1_2.setBounds(566, 155, 75, 21);
		contentPane.add(lblNewLabel_1_2);
		
		JLabel lblNewLabel_1_3 = new JLabel("\u5E74   \u9F84\uFF1A");
		lblNewLabel_1_3.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1_3.setBounds(566, 196, 75, 21);
		contentPane.add(lblNewLabel_1_3);
		
		JLabel lblNewLabel_1_4 = new JLabel("\u57FA\u672C\u5DE5\u8D44\uFF1A");
		lblNewLabel_1_4.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1_4.setBounds(566, 238, 75, 21);
		contentPane.add(lblNewLabel_1_4);
		
		JLabel lblNewLabel_1_4_1 = new JLabel("\u5458\u5DE5\u90E8\u95E8\uFF1A");
		lblNewLabel_1_4_1.setFont(new Font("宋体", Font.PLAIN, 15));
		lblNewLabel_1_4_1.setBounds(566, 286, 75, 21);
		contentPane.add(lblNewLabel_1_4_1);
		
		phone_field = new JTextField();
		phone_field.setColumns(10);
		phone_field.setBounds(660, 116, 131, 21);
		contentPane.add(phone_field);
		
		age_field = new JTextField();
		age_field.setColumns(10);
		age_field.setBounds(660, 196, 131, 21);
		contentPane.add(age_field);
		
		salary_field = new JTextField();
		salary_field.setColumns(10);
		salary_field.setBounds(660, 238, 131, 21);
		contentPane.add(salary_field);
		
		sex_box = new JComboBox();
		sex_box.setModel(new DefaultComboBoxModel(new String[] {"\u7537", "\u5973"}));
		sex_box.setBounds(660, 154, 131, 23);
		contentPane.add(sex_box);
		
		department_box = new JComboBox();
		department_box.setModel(new DefaultComboBoxModel(new String[] {"\u7814\u53D1\u90E8"}));
		department_box.setBounds(660, 285, 131, 23);
		contentPane.add(department_box);
		
		JButton submit_btn = new JButton("\u63D0\u4EA4");
		submit_btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				actionSubmit(e);
			}
		});
		submit_btn.setBounds(616, 330, 93, 23);
		contentPane.add(submit_btn);
		
		JButton delete_btn = new JButton("\u5220\u9664");
		delete_btn.setBounds(129, 386, 93, 23);
		contentPane.add(delete_btn);
	}

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
		
		Double salary = 0.0;
		try {
			 salary = Double.parseDouble(this.salary_field.getText().trim());

		} catch (NumberFormatException e2) {
			System.err.println("工资未输入");
		
		}
		Personnel personnel = new Personnel(name, phone, sex, department, age, salary);
	    System.out.println(personnel);
	}
}
