package csgl_layout;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Font;

import csgl_jdbcdatabase.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class GoodsManager extends JFrame {

	private JPanel contentPane;
	private JTable table;
	private JTextField textField;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					GoodsManager frame = new GoodsManager();
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
	public GoodsManager() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 828, 611);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBounds(10, 72, 794, 492);
		contentPane.add(panel);
		panel.setLayout(new BorderLayout(0, 0));
		
		JScrollPane scrollPane = new JScrollPane();
		panel.add(scrollPane, BorderLayout.CENTER);
		
		table = new JTable();
		table.setFont(new Font("宋体", Font.BOLD | Font.ITALIC, 20));
		table.setModel(new DefaultTableModel(DBManager.selectSql("SELECT * FROM tb_goods"),
			new String[] {
				"\u5546\u54C1\u7F16\u53F7", "\u5546\u54C1\u540D\u79F0", "\u6570\u91CF", "\u5355\u4EF7"
			}
		));
		scrollPane.setViewportView(table);
		
		JLabel lblNewLabel = new JLabel("\u8F93\u5165\u5546\u54C1\u540D\u79F0\uFF1A");
		lblNewLabel.setFont(new Font("宋体", Font.BOLD, 21));
		lblNewLabel.setBounds(37, 20, 159, 42);
		contentPane.add(lblNewLabel);
		
		textField = new JTextField();
		textField.setBounds(188, 33, 343, 21);
		contentPane.add(textField);
		textField.setColumns(10);
		
		JButton btnNewButton = new JButton("\u6DFB\u52A0");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
//				添加
				//创建新的窗口
				GoodsManager frame =new tj();
				frame.setVisible(true);
				Updatetable(table);				
			}
		});
		btnNewButton.setFont(new Font("宋体", Font.BOLD | Font.ITALIC, 20));
		btnNewButton.setBounds(689, 10, 93, 51);
		contentPane.add(btnNewButton);
		
		JButton btnNewButton_1 = new JButton("\u67E5\u8BE2");
		btnNewButton_1.addActionListener(new ActionListener() {
//			查询
			public void actionPerformed(ActionEvent e) {
			if(textField.getText().length()!=0) {
	 			String name =textField.getText();
	 			String nameresult="SELECT COUNT(*) FROM tb_goods WHERE goodname="+name;
	 			boolean jg=DBManager.pd(nameresult);
	 			if(jg) {
	 				String sql ="SELECT * FROM tb_goods WHERE goodname="+name;
	 	 		    // 插入成功之后，左边的表格需要重新刷新数据
	 				// 刷新数据之前，必须要有数据
	 	 			DefaultTableModel defaultTableModel=(new DefaultTableModel(DBManager.selectSql(sql),
	 	 					new String[] {
	 	 						"\u5546\u54C1\u7F16\u53F7", "\u5546\u54C1\u540D\u79F0", "\u6570\u91CF", "\u5355\u4EF7"
	 	 					}
	 	 				));
	 					table.setModel(defaultTableModel);	// 表格的数据存储在model中
	 					defaultTableModel.fireTableDataChanged();// 刷新数据
	 			}else {
					JOptionPane.showMessageDialog(contentPane, "没找到该商品！");
					textField.setText(" ");
				}
	 		
			}else {
				JOptionPane.showMessageDialog(contentPane, "商品名称为空");
				Updatetable(table);
			}
				
			}
		});
		btnNewButton_1.setFont(new Font("宋体", Font.BOLD | Font.ITALIC, 20));
		btnNewButton_1.setBounds(548, 23, 131, 36);
		contentPane.add(btnNewButton_1);
	}
	public static void Updatetable(JTable table) {
		// 插入成功之后，左边的表格需要重新刷新数据
			// 刷新数据之前，必须要有数据
			DefaultTableModel defaultTableModel=(new DefaultTableModel(
					DBManager.selectSql("SELECT * FROM tb_goods"),
					new String[] {
						"\u5546\u54C1\u7F16\u53F7", "\u5546\u54C1\u540D\u79F0", "\u6570\u91CF", "\u5355\u4EF7"
					}
				));
				table.setModel(defaultTableModel);	// 表格的数据存储在model中
				defaultTableModel.fireTableDataChanged();// 刷新数据
	}
}
