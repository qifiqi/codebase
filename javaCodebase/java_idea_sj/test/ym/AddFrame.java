package com.lz.ui;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import com.lz.dao.StudentDAO;
import com.lz.entity.Student;

import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JRadioButton;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class AddFrame extends JFrame {

	private JPanel contentPane;
	private JTextField txtName;
	private JTextField txtAge;
	private JTextField txtAddress;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					AddFrame frame = new AddFrame();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public AddFrame() {
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("\u59D3\u540D");
		lblNewLabel.setBounds(64, 57, 54, 15);
		contentPane.add(lblNewLabel);
		
		txtName = new JTextField();
		txtName.setBounds(156, 54, 139, 21);
		contentPane.add(txtName);
		txtName.setColumns(10);
		
		JLabel lblNewLabel_1 = new JLabel("\u5E74\u9F84");
		lblNewLabel_1.setBounds(64, 98, 54, 15);
		contentPane.add(lblNewLabel_1);
		
		txtAge = new JTextField();
		txtAge.setColumns(10);
		txtAge.setBounds(156, 95, 139, 21);
		contentPane.add(txtAge);
		
		JLabel lblNewLabel_2 = new JLabel("\u6027\u522B");
		lblNewLabel_2.setBounds(64, 145, 54, 15);
		contentPane.add(lblNewLabel_2);
		
		JLabel lblNewLabel_3 = new JLabel("\u5730\u5740");
		lblNewLabel_3.setBounds(64, 189, 54, 15);
		contentPane.add(lblNewLabel_3);
		
		txtAddress = new JTextField();
		txtAddress.setColumns(10);
		txtAddress.setBounds(156, 186, 139, 21);
		contentPane.add(txtAddress);
		
		JRadioButton rdbtnNewRadioButton = new JRadioButton("\u7537");
		rdbtnNewRadioButton.setBounds(150, 141, 54, 23);
		contentPane.add(rdbtnNewRadioButton);
		
		JRadioButton rdbtnNewRadioButton_1 = new JRadioButton("\u5973");
		rdbtnNewRadioButton_1.setBounds(206, 141, 54, 23);
		contentPane.add(rdbtnNewRadioButton_1);
		
		JButton btnNewButton = new JButton("\u6DFB\u52A0");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				Student stu=new Student();
				stu.setName(txtName.getText());
				stu.setAge(Integer.parseInt(txtAge.getText()));
				stu.setAddress(txtAddress.getText());
				if(rdbtnNewRadioButton.isSelected()) {
					stu.setSex("男");
				}else {
					stu.setSex("女");
				}
				StudentDAO dao=new StudentDAO();
				if(dao.AddStudent(stu)) {
					JOptionPane.showMessageDialog(null, "添加成功","提示信息",JOptionPane.INFORMATION_MESSAGE);
				}else {
					JOptionPane.showMessageDialog(null, "添加失败","提示信息",JOptionPane.INFORMATION_MESSAGE);
				}
			}
		});
		btnNewButton.setBounds(71, 229, 93, 23);
		contentPane.add(btnNewButton);
		
		JButton btnNewButton_1 = new JButton("\u53D6\u6D88");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
			
			}
		});
		btnNewButton_1.setBounds(185, 229, 93, 23);
		contentPane.add(btnNewButton_1);
	}
}
