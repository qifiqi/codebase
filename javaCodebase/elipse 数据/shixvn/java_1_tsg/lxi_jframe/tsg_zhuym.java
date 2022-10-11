package lxi_jframe;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.SwingConstants;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.table.DefaultTableModel;
import lxi_biao.bookinfo;
import javax.swing.JScrollPane;
import lxi_jdbc.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JCheckBox;


public class tsg_zhuym extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JTextField textField_1;
	private JTextField textField_2;
	private JTextField textField_3;
	private JTable table;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					tsg_zhuym frame = new tsg_zhuym();
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
	public tsg_zhuym() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 665, 406);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		textField = new JTextField();
		textField.setBounds(132, 26, 162, 21);
		contentPane.add(textField);
		textField.setColumns(10);

		JLabel lblNewLabel = new JLabel("\u56FE\u7247\u540D\u79F0\uFF1A");
		lblNewLabel.setHorizontalAlignment(SwingConstants.LEFT);
		lblNewLabel.setBounds(23, 26, 73, 21);
		contentPane.add(lblNewLabel);

		JLabel lblNewLabel_1 = new JLabel("\u4F5C\u8005\uFF1A");
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.LEFT);
		lblNewLabel_1.setBounds(23, 86, 58, 21);
		contentPane.add(lblNewLabel_1);

		textField_1 = new JTextField();
		textField_1.setColumns(10);
		textField_1.setBounds(132, 86, 162, 21);
		contentPane.add(textField_1);

		JLabel lblNewLabel_1_1 = new JLabel("\u51FA\u7248\u793E\uFF1A");
		lblNewLabel_1_1.setHorizontalAlignment(SwingConstants.LEFT);
		lblNewLabel_1_1.setBounds(23, 145, 58, 21);
		contentPane.add(lblNewLabel_1_1);

		textField_2 = new JTextField();
		textField_2.setColumns(10);
		textField_2.setBounds(132, 145, 162, 21);
		contentPane.add(textField_2);

		JLabel lblNewLabel_1_2 = new JLabel("\u4EF7\u683C\uFF1A");
		lblNewLabel_1_2.setHorizontalAlignment(SwingConstants.LEFT);
		lblNewLabel_1_2.setBounds(23, 205, 58, 21);
		contentPane.add(lblNewLabel_1_2);

		textField_3 = new JTextField();
		textField_3.setColumns(10);
		textField_3.setBounds(132, 205, 162, 21);
		contentPane.add(textField_3);

		JComboBox comboBox = new JComboBox();
		comboBox.setModel(new DefaultComboBoxModel(new String[] { "\u5C0F\u8BF4", "\u6742\u5FD7", "\u6559\u6750" }));
		comboBox.setBounds(132, 253, 162, 23);
		contentPane.add(comboBox);

		JLabel lblNewLabel_1_2_1 = new JLabel("\u56FE\u4E66\u7C7B\u578B\uFF1A");
		lblNewLabel_1_2_1.setHorizontalAlignment(SwingConstants.LEFT);
		lblNewLabel_1_2_1.setBounds(23, 254, 99, 21);
		contentPane.add(lblNewLabel_1_2_1);

		JButton btnNewButton = new JButton("\u6DFB\u52A0");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// 使用JOptionpane类的showmessageDialog（）方法弹出弹窗
				JOptionPane.showMessageDialog(contentPane, "添加");
				/*
				 * textField 图片名称 textField_1 作者 textField_2 出版社 textField_3 价格 comboBox 图书类型
				 */
				String bookname = textField.getText();
				String bookauthor = textField_1.getText();
				String bookpublish = textField_2.getText();
				String price = textField_3.getText();

				float bookprice = Float.valueOf(price);
				// 下拉列表获取选中值得方法为 getSelectedItem
				String booktype = String.valueOf(comboBox.getSelectedItem());
				// String typeString1 = comboBox.getSelectedItem().toString();

				bookinfo bookinfo = new bookinfo(0, bookname, bookauthor, bookpublish, bookprice, booktype);
				// 真正目的，
				lxi_shujkjdbc.insertandxgaibookinfo(bookinfo);

				// 插入成功之后，左边的表格需要重新刷新数据
				// 刷新数据之前，必须要有数据
				DefaultTableModel defaultTableModel = (new DefaultTableModel(lxi_shujkjdbc.getAllbookinfo(),
						new String[] { "\u7F16\u53F7", "\u540D\u79F0", "\u4F5C\u8005", "\u51FA\u7248\u793E",
								"\u4EF7\u683C", "\u7C7B\u578B" }) {
					boolean[] columnEditables = new boolean[] { false, true, true, true, true, true };

					public boolean isCellEditable(int row, int column) {
						return columnEditables[column];
					}
				});

				// 表格的数据存储在model中
				table.setModel(defaultTableModel);
				defaultTableModel.fireTableDataChanged();// 刷新数据

			}
		});
		btnNewButton.setBounds(142, 315, 93, 23);
		contentPane.add(btnNewButton);

		JButton btnNewButton_1 = new JButton("\u6E05\u7A7A");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// 清空
				// 使用JOptionpane类的showmessageDialog（）方法弹出弹窗
				JOptionPane.showMessageDialog(contentPane, "清空");
				textField.setText(" ");
				textField_1.setText(" ");
				textField_2.setText(" ");
				textField_3.setText(" ");
			
			}
		});
		btnNewButton_1.setBounds(245, 315, 93, 23);
		contentPane.add(btnNewButton_1);

		JButton btnNewButton_2 = new JButton("\u5220\u9664");
		btnNewButton_2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// 删除
				// showConfirmDialog,弹窗页面有按钮
				// contentPane设置弹窗位置是在屏幕上还是前端页面中
				// JOptionPane.YES_NO_OPTION=设置按钮的数量
				int a = JOptionPane.showConfirmDialog(contentPane, "请问你是否要删除", "确认", JOptionPane.YES_NO_OPTION);
				// a点击确认时是0 取消是1
				// 当a=0是确定删除
				if (a == 0) {
					//首先确认选中的是哪一行，通过个体getSelectedRow（）方法获得哪一行
					int bookhang = table.getSelectedRow();
					//通过表格getvalueAt方法获得某行某列单元格的值从下标
					String bookidString=table.getValueAt(bookhang, 0).toString();
					//成功获得要删除的书籍编号，调用方法
					//转换成int，Integer.valueOf(bookidString);
					int bookid=Integer.valueOf(bookidString);
					lxi_shujkjdbc.deletebookinfo(bookid);
					// 删除成功之后，左边的表格需要重新刷新数据
					// 刷新数据之前，必须要有数据
					
					
					DefaultTableModel defaultTableModel = (new DefaultTableModel(lxi_shujkjdbc.getAllbookinfo(),
							new String[] { "\u7F16\u53F7", "\u540D\u79F0", "\u4F5C\u8005", "\u51FA\u7248\u793E",
									"\u4EF7\u683C", "\u7C7B\u578B" }) {
						boolean[] columnEditables = new boolean[] { false, true, true, true, true, true };

						public boolean isCellEditable(int row, int column) {
							return columnEditables[column];
						}
					});

					// 表格的数据存储在model中
					table.setModel(defaultTableModel);
					defaultTableModel.fireTableDataChanged();// 刷新数据

			  }
			}
		});
		btnNewButton_2.setBounds(348, 315, 93, 23);
		contentPane.add(btnNewButton_2);

		JPanel panel = new JPanel();
		panel.setBounds(316, 26, 305, 248);
		contentPane.add(panel);
		panel.setLayout(new BorderLayout(0, 0));

		JScrollPane scrollPane = new JScrollPane();
		panel.add(scrollPane, BorderLayout.CENTER);

		table = new JTable();
		table.setModel(new DefaultTableModel(lxi_shujkjdbc.getAllbookinfo(), new String[] { "\u7F16\u53F7",
				"\u540D\u79F0", "\u4F5C\u8005", "\u51FA\u7248\u793E", "\u4EF7\u683C", "\u7C7B\u578B" }) {
			boolean[] columnEditables = new boolean[] { false, true, true, true, true, true };

			public boolean isCellEditable(int row, int column) {
				return columnEditables[column];
			}
		});
		scrollPane.setViewportView(table);
		
		JButton btnNewButton_3 = new JButton("\u4FEE\u6539");
		btnNewButton_3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int a = JOptionPane.showConfirmDialog(contentPane, "请问你是否要修改", "确认", JOptionPane.YES_NO_OPTION);
				if (a==0) {
					//首先确认选中的是哪一行，通过个体getSelectedRow（）方法获得哪一行
					int bookhang = table.getSelectedRow();
					//通过表格getvalueAt方法获得某行某列单元格的值从下标
					String bookidString=table.getValueAt(bookhang, 0).toString();
					//成功获得要删除的书籍编号，调用方法
					//转换成int，Integer.valueOf(bookidString);
					int bookid=Integer.valueOf(bookidString);
					/*
					 * textField 图片名称 textField_1 作者 textField_2 出版社 textField_3 价格 comboBox 图书类型
					 */
					String bookname = textField.getText();
					String bookauthor = textField_1.getText();
					String bookpublish = textField_2.getText();
					String price = textField_3.getText();

					float bookprice = Float.valueOf(price);
					// 下拉列表获取选中值得方法为 getSelectedItem
					String booktype = String.valueOf(comboBox.getSelectedItem());
					// String typeString1 = comboBox.getSelectedItem().toString();
					
					bookinfo bookinfo = new bookinfo(bookid, bookname, bookauthor, bookpublish, bookprice, booktype);
					// 真正目的，
					lxi_shujkjdbc.xgaibookinfo(bookinfo);

					
					// 删除成功之后，左边的表格需要重新刷新数据
					// 刷新数据之前，必须要有数据
					
					DefaultTableModel defaultTableModel = (new DefaultTableModel(lxi_shujkjdbc.getAllbookinfo(),
							new String[] { "\u7F16\u53F7", "\u540D\u79F0", "\u4F5C\u8005", "\u51FA\u7248\u793E",
									"\u4EF7\u683C", "\u7C7B\u578B" }) {
						boolean[] columnEditables = new boolean[] { false, true, true, true, true, true };

						public boolean isCellEditable(int row, int column) {
							return columnEditables[column];
						}
					});

					// 表格的数据存储在model中
					table.setModel(defaultTableModel);
					defaultTableModel.fireTableDataChanged();// 刷新数据
				}
				
				
				
			}
		});
		btnNewButton_3.setBounds(451, 315, 93, 23);
		contentPane.add(btnNewButton_3);
	}
}
