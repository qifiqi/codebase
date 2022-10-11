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
		
		setTitle("Ա������ϵͳ");
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
		lblNewLabel.setFont(new Font("����", Font.BOLD, 20));
		lblNewLabel.setBounds(742, 31, 86, 23);
		contentPane.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("\u5458\u5DE5\u59D3\u540D\uFF1A");
		lblNewLabel_1.setFont(new Font("����", Font.PLAIN, 15));
		lblNewLabel_1.setBounds(691, 75, 75, 21);
		contentPane.add(lblNewLabel_1);
		
		name_field = new JTextField();
		name_field.setBounds(801, 75, 131, 21);
		contentPane.add(name_field);
		name_field.setColumns(10);
		
		JLabel lblNewLabel_1_1 = new JLabel("\u5458\u5DE5\u53F7\u7801\uFF1A");
		lblNewLabel_1_1.setFont(new Font("����", Font.PLAIN, 15));
		lblNewLabel_1_1.setBounds(691, 116, 75, 21);
		contentPane.add(lblNewLabel_1_1);
		
		JLabel lblNewLabel_1_2 = new JLabel("\u6027   \u522B\uFF1A");
		lblNewLabel_1_2.setFont(new Font("����", Font.PLAIN, 15));
		lblNewLabel_1_2.setBounds(691, 155, 75, 21);
		contentPane.add(lblNewLabel_1_2);
		
		JLabel lblNewLabel_1_3 = new JLabel("\u5E74   \u9F84\uFF1A");
		lblNewLabel_1_3.setFont(new Font("����", Font.PLAIN, 15));
		lblNewLabel_1_3.setBounds(691, 196, 75, 21);
		contentPane.add(lblNewLabel_1_3);
		
		JLabel lblNewLabel_1_4 = new JLabel("\u57FA\u672C\u5DE5\u8D44\uFF1A");
		lblNewLabel_1_4.setFont(new Font("����", Font.PLAIN, 15));
		lblNewLabel_1_4.setBounds(691, 238, 75, 21);
		contentPane.add(lblNewLabel_1_4);
		
		JLabel lblNewLabel_1_4_1 = new JLabel("\u5458\u5DE5\u90E8\u95E8\uFF1A");
		lblNewLabel_1_4_1.setFont(new Font("����", Font.PLAIN, 15));
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
			JOptionPane.showMessageDialog(this,"��ѡ����Ҫɾ�����û�","����",JOptionPane.WARNING_MESSAGE);
		}else {
			String name = (String)this.table.getModel().getValueAt(selectedRow,1);
			int result = JOptionPane.showConfirmDialog(this,"ȷ��ɾ����"+name+"��","��ʾ",JOptionPane.YES_NO_CANCEL_OPTION);
		    if(result == 0) {//������ǵİ�ť
		    	int id = (int)this.table.getModel().getValueAt(selectedRow,0);
		    	personnelDao.delete(id);
		    	JOptionPane.showMessageDialog(this,"ɾ���ɹ���","��ʾ",JOptionPane.INFORMATION_MESSAGE);
		    	this.updateTable();
		    }
		}
	}
	
	protected void actionSearch(ActionEvent e) {
		this.updateTable();
	}
	
	
	

	
	/**
	 * ��Ӱ�ť���¼�����
	 * @param e
	 */
	

	protected void actionSubmit(ActionEvent e) {
		System.out.println("�ύ��ť�������");
		//��ȡ�û���������ֵ������ȥ��ǰ��Ŀո�
		String name = this.name_field.getText().trim();
		if ("".equals(name)) {
			//�������Ϊ�գ�����������棬���ҽ���������ʲô������
			JOptionPane.showMessageDialog(this,"�û�������Ϊ�գ�","����",JOptionPane.WARNING_MESSAGE);
			return;
		}
	//��ȡ�ֻ��Ų��ж�
		String phone = this.phone_field.getText().trim();
		if ("".equals(phone)) {
			JOptionPane.showConfirmDialog(this,"�ֻ����벻��Ϊ�գ�","����",JOptionPane.WARNING_MESSAGE);
			return;
		}
		//��ȡ���䲢�����쳣
		int age = 0 ;
		try {
			 age = Integer.parseInt(this.age_field.getText().trim());
		} catch (NumberFormatException e2) {
			System.err.println("����δ����");
		}
			
		//��ȡ�Ա�Ͳ���ѡ��
		String sex = this.sex_box.getSelectedItem().toString();
		String department = this.department_box.getSelectedItem().toString();
		//��ȡ�������벢�ж������쳣
		Double salary = 0.0;
		try {
			 salary = Double.parseDouble(this.salary_field.getText().trim());

		} catch (NumberFormatException e2) {
			JOptionPane.showMessageDialog(this,"��������ȷ�Ĺ��ʣ�","����",JOptionPane.WARNING_MESSAGE);
		return;
		}
		//�����е������װΪһ���û�����
		Personnel personnel = new Personnel(name, phone, sex, department, age, salary);
	    if (personnelDao.add(personnel)) {
	    	JOptionPane.showMessageDialog(this,"��ӳɹ�","�ɹ�", JOptionPane.INFORMATION_MESSAGE);
	        this.updateTable();
	    }else {
	    	JOptionPane.showMessageDialog(this,"��ӳɹ�","ʧ��", JOptionPane.ERROR_MESSAGE);

		}
	}
    
	/**
	 * ��������������
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
	 * ���±�������
	 */
	private void updateTable() {
		//�ж��������������û�����ݣ�����������ݣ������ǰ��������״̬��ˢ������Ҳ��ˢ������������
		String text = this.search_field.getText().trim();
		if("".equals(text)) {
			this.table.setModel(new PersonnelTableModel(personnelDao.getAll()));
		
		}else {
			this.table.setModel(new PersonnelTableModel(personnelDao.search(text)));

		}
		
	}
}
