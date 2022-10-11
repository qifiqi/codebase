package csgl_layout;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTable;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Font;
import javax.swing.SwingConstants;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import csgl_jdbcdatabase.*;
import csgl_biao.*;
public class tj extends GoodsManager {

	private JPanel contentPane;
	private JTextField textField;
	private JTextField textField_1;
	private JTextField textField_2;
	private JTextField textField_3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		
	}

	/**
	 * Create the frame.
	 */
	public tj() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 533, 470);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("\u5546\u54C1\u7F16\u53F7:");
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setFont(new Font("宋体", Font.BOLD, 20));
		lblNewLabel.setBounds(41, 39, 163, 33);
		contentPane.add(lblNewLabel);
//		商品编号
		textField = new JTextField();
		textField.setBounds(214, 47, 238, 21);
		contentPane.add(textField);
		textField.setColumns(10);
//		商品名称
		textField_1 = new JTextField();
		textField_1.setColumns(10);
		textField_1.setBounds(214, 108, 238, 21);
		contentPane.add(textField_1);
//		商品数量
		textField_2 = new JTextField();
		textField_2.setColumns(10);
		textField_2.setBounds(214, 181, 238, 21);
		contentPane.add(textField_2);
//		商品价格
		textField_3 = new JTextField();
		textField_3.setColumns(10);
		textField_3.setBounds(214, 254, 238, 21);
		contentPane.add(textField_3);
		
		JButton btnNewButton = new JButton("\u786E\u8BA4");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				if((textField.getText().length()!=0)&&(textField_1.getText().length()!=0)
						&&(textField_2.getText().length()!=0)
						&&(textField_3.getText().length()!=0)) {
						int id =Integer.valueOf(textField.getText());
						String goodidresult="SELECT COUNT(*) FROM tb_goods WHERE goodid="+id;
						boolean jg=DBManager.pd(goodidresult);
						if (jg) {
							JOptionPane.showMessageDialog(contentPane, "商品编号重复");
						}else {

//							添加确认按钮
							int goodid =Integer.valueOf(textField.getText());
							int num =Integer.valueOf(textField_2.getText());
							
							double price =Double.valueOf(textField_3.getText());
							
							String goodname=textField_1.getText();
							
							tb_goods tb_goods=new tb_goods(goodid, num, goodname,  price);
							DBManager.excuteSQL(tb_goods);
							JOptionPane.showMessageDialog(contentPane, "添加成功");
							dispose();
						}
				}else {
					JOptionPane.showMessageDialog(contentPane, "不能为空");
				}
			
			}
		});
		btnNewButton.setFont(new Font("宋体", Font.BOLD, 30));
		btnNewButton.setBounds(76, 342, 141, 54);
		contentPane.add(btnNewButton);
		
		JLabel lblNewLabel_1 = new JLabel("\u5546\u54C1\u540D\u79F0:");
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1.setFont(new Font("宋体", Font.BOLD, 20));
		lblNewLabel_1.setBounds(41, 111, 163, 33);
		contentPane.add(lblNewLabel_1);
		
		JLabel lblNewLabel_2 = new JLabel("\u6570\u91CF");
		lblNewLabel_2.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_2.setFont(new Font("宋体", Font.BOLD, 20));
		lblNewLabel_2.setBounds(41, 184, 163, 33);
		contentPane.add(lblNewLabel_2);
		
		JLabel lblNewLabel_3 = new JLabel("\u4EF7\u683C");
		lblNewLabel_3.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_3.setFont(new Font("宋体", Font.BOLD, 20));
		lblNewLabel_3.setBounds(41, 254, 163, 33);
		contentPane.add(lblNewLabel_3);
		
		JButton btnNewButton_1 = new JButton("\u53D6\u6D88");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
//				取消按钮
				dispose();
			}
		});
		btnNewButton_1.setFont(new Font("宋体", Font.BOLD, 30));
		btnNewButton_1.setBounds(259, 342, 141, 54);
		contentPane.add(btnNewButton_1);
	}
}
