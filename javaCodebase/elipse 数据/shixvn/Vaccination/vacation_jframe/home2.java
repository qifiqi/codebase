package vacation_jframe;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import vacation_biao.inoculatetable;
import vacation_shujvku.epidemic_1;

import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.JButton;
import javax.swing.JRadioButton;


public class home2 extends home_jframe implements ActionListener {

	private JPanel contentPane;
	private JTextField textField;
	private JTextField textField_1;
	private JTextField textField_2;
	private JTextField textField_3;
	private JTextField textField_4;
	private JTextField textField_5;
	JButton btnNewButton;
	JButton btnNewButton_1;
	JButton btnNewButton_2;
	JLabel lblNewLabel;
	private JTextField textField_6;
	private JTextField textField_7;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					home2 frame = new home2();
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
	public home2() {
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 651, 417);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);

		JPanel panel = new JPanel();
		contentPane.add(panel, BorderLayout.CENTER);
		panel.setLayout(null);

		JLabel lblNewLabel = new JLabel("\u57CE\u5E02\r\n\uFF1A");
		this.lblNewLabel = lblNewLabel;
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setBounds(10, 10, 93, 32);
		panel.add(lblNewLabel);
//		城市
		textField = new JTextField();
		textField.setBounds(113, 16, 166, 21);
		panel.add(textField);
		textField.setColumns(10);
//		社区
		textField_1 = new JTextField();
		textField_1.setColumns(10);
		textField_1.setBounds(392, 16, 225, 21);
		panel.add(textField_1);

		JLabel lblNewLabel_1 = new JLabel("\u793E\u533A\uFF1A");
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1.setBounds(289, 10, 93, 32);
		panel.add(lblNewLabel_1);

		JLabel lblNewLabel_2 = new JLabel("\u59D3\u540D\uFF1A");
		lblNewLabel_2.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_2.setBounds(10, 73, 93, 32);
		panel.add(lblNewLabel_2);
//		姓名
		textField_2 = new JTextField();
		textField_2.setColumns(10);
		textField_2.setBounds(113, 79, 166, 21);
		panel.add(textField_2);

		JLabel lblNewLabel_1_1 = new JLabel("\u75AB\u82D7\u7C7B\u578B\uFF1A");
		lblNewLabel_1_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1_1.setBounds(289, 73, 93, 32);
		panel.add(lblNewLabel_1_1);
//		疫苗接种类型
		textField_3 = new JTextField();
		textField_3.setColumns(10);
		textField_3.setBounds(392, 79, 225, 21);
		panel.add(textField_3);

		JLabel lblNewLabel_3 = new JLabel("\u7535\u8BDD\u53F7\u7801\uFF1A");
		lblNewLabel_3.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_3.setBounds(10, 148, 93, 32);
		panel.add(lblNewLabel_3);
//		电话号码
		textField_4 = new JTextField();
		textField_4.setColumns(10);
		textField_4.setBounds(113, 154, 166, 21);
		panel.add(textField_4);

		JLabel lblNewLabel_1_2 = new JLabel("\u8EAB\u4EFD\u8BC1\u53F7\u7801\uFF1A");
		lblNewLabel_1_2.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1_2.setBounds(289, 148, 93, 32);
		panel.add(lblNewLabel_1_2);
//		身份证号码
		textField_5 = new JTextField();
		textField_5.setColumns(10);
		textField_5.setBounds(392, 154, 225, 21);
		panel.add(textField_5);
//		添加
		JButton btnNewButton = new JButton("\u6DFB\u52A0");
		this.btnNewButton = btnNewButton;
		btnNewButton.addActionListener(this);
		btnNewButton.setBounds(113, 313, 97, 23);
		panel.add(btnNewButton);
//		重置
		JButton btnNewButton_1 = new JButton("\u91CD\u7F6E");
		this.btnNewButton_1 = btnNewButton_1;
		btnNewButton_1.addActionListener(this);

		btnNewButton_1.setBounds(220, 313, 97, 23);
		panel.add(btnNewButton_1);
//		关闭
		JButton btnNewButton_2 = new JButton("\u5173\u95ED");
		this.btnNewButton_2 = btnNewButton_2;
		btnNewButton_2.addActionListener(this);
		btnNewButton_2.setBounds(327, 313, 97, 23);
		panel.add(btnNewButton_2);

		JLabel lblNewLabel_3_1 = new JLabel("\u6027\u522B");
		lblNewLabel_3_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_3_1.setBounds(10, 210, 93, 32);
		panel.add(lblNewLabel_3_1);

		JLabel lblNewLabel_3_1_1 = new JLabel("\u75AB\u82D7\u63A5\u79CD\u65E5\u671F");
		lblNewLabel_3_1_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_3_1_1.setBounds(289, 210, 93, 32);
		panel.add(lblNewLabel_3_1_1);
//		性别
		textField_6 = new JTextField();
		textField_6.setColumns(10);
		textField_6.setBounds(113, 216, 166, 21);
		panel.add(textField_6);
//		疫苗接种时间
		textField_7 = new JTextField();
		textField_7.setColumns(10);
		textField_7.setBounds(392, 216, 225, 21);
		panel.add(textField_7);
	}

	public void itemStateChanged(ItemEvent e) {
		System.out.println(((JRadioButton) e.getSource()).getText() + "选项发生了改变");
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if (e.getSource() == btnNewButton) {
//			城市
			String city = textField.getText();
//			社区
			String community = textField_1.getText();
//			姓名
			String Name = textField_2.getText();
//			疫苗接种类型
			String type = textField_3.getText();
//			电话号码
			String phone = textField_4.getText();
//			身份证号码
			String Id_number = textField_5.getText();
//			性别
			String gender = textField_6.getText();
//			疫苗接种时间
			String time = textField_7.getText();

			inoculatetable inoculatetable = new inoculatetable(0, city, community, Name, gender, type, phone, Id_number,
					time);
			epidemic_1.addmodification(inoculatetable);
		} else if (e.getSource() == btnNewButton_1) {
			textField.setText(" ");
			textField_1.setText(" ");
			textField_2.setText(" ");
			textField_3.setText(" ");
			textField_4.setText(" ");
			textField_5.setText(" ");
		} else if (e.getSource() == btnNewButton_2) {
			this.dispose();
		}
	}

}
