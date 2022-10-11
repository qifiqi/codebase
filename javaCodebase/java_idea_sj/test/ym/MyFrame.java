package com.lz.ui;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JScrollPane;
import javax.swing.JTabbedPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

import com.lz.dao.StudentDAO;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MyFrame extends JFrame {

	private JPanel contentPane;
	private JTable table;
	private JTextField txtName;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame frame = new MyFrame();
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
	public MyFrame() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 545, 450);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBounds(70, 67, 404, 289);
		contentPane.add(panel);
		panel.setLayout(new BorderLayout(0, 0));
		
		JScrollPane scrollPane = new JScrollPane();
		panel.add(scrollPane, BorderLayout.CENTER);
		
		table = new JTable();
		//����ѧ��dao
		StudentDAO dao=new StudentDAO();
		//��ѯȫ��ѧ����Ϣ
		Object[][] objs=dao.FindAll();
		//�����������
		table.setModel(new DefaultTableModel(
			objs,
			new String[] {"id", "����", "����", "�Ա�", "��ַ"}
		));
		scrollPane.setViewportView(table);
		
		txtName = new JTextField();
		txtName.setBounds(160, 23, 211, 21);
		contentPane.add(txtName);
		txtName.setColumns(10);
		
		JButton btnFind = new JButton("\u67E5\u8BE2");
		btnFind.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				//��ȡ�û����������
				String name=txtName.getText();
				//��дģ����ѯ��sql���
				String sql="select * from student where name like '%"+name+"%'";
				StudentDAO dao=new StudentDAO();
				//ͨ��dao�����ѯ���½��
				Object[][] objs=dao.Find(sql);
				//�������ݸ��±��
				table.setModel(new DefaultTableModel(
					objs,
					new String[] {"id", "����", "����", "�Ա�", "��ַ"}
				));
			}
		});
		btnFind.setBounds(381, 22, 93, 23);
		contentPane.add(btnFind);
		
		JLabel lblNewLabel = new JLabel("\u8BF7\u8F93\u5165\u59D3\u540D");
		lblNewLabel.setBounds(71, 26, 79, 15);
		contentPane.add(lblNewLabel);
		
		JButton btnNewButton = new JButton("\u6DFB\u52A0");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				AddFrame af=new AddFrame();
				af.setSize(600, 400);
				af.setTitle("���ѧ��");
				af.setVisible(true);
				
			}
		});
		btnNewButton.setBounds(80, 366, 93, 23);
		contentPane.add(btnNewButton);
		
		JButton btnNewButton_1 = new JButton("\u5237\u65B0");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				//ˢ�¸��±��
				Object[][] objs=dao.FindAll();
				//�����������
				table.setModel(new DefaultTableModel(
					objs,
					new String[] {"id", "����", "����", "�Ա�", "��ַ"}
				));
			}
		});
		btnNewButton_1.setBounds(188, 366, 93, 23);
		contentPane.add(btnNewButton_1);
	}
}
