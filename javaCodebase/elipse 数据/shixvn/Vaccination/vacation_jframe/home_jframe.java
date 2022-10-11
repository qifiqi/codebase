package vacation_jframe;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

import csgl_jdbcdatabase.DBManager;
import csgl_layout.GoodsManager;
import csgl_layout.tj;

import java.awt.FlowLayout;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Font;
import javax.swing.SwingConstants;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import vacation_biao.*;
import vacation_shujvku.epidemic_1;
import java.awt.Color;

public class home_jframe extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JTextField textField_1;
	private JTable table_2;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					home_jframe frame = new home_jframe();
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
	public home_jframe() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 1118, 693);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JPanel panel = new JPanel();
		panel.setBounds(10, 92, 1084, 554);
		contentPane.add(panel);
		panel.setLayout(new BorderLayout(0, 0));

		JScrollPane scrollPane = new JScrollPane();
		panel.add(scrollPane);
		
		table_2 = new JTable();
		table_2.setForeground(Color.BLACK);
		table_2.setBackground(Color.WHITE);
		DefaultTableModel defaultTableModel = (new DefaultTableModel(epidemic_1.inquireall(),
			new String[] {
					"\u7F16\u53F7", "\u57CE\u5E02", "\u793E\u533A", "\u59D3\u540D", "\u6027\u522B", "\u75AB\u82D7\u7C7B\u578B", "\u7535\u8BDD\u53F7\u7801", "\u63A5\u79CD\u65F6\u95F4", "\u8EAB\u4EFD\u8BC1\u53F7\u7801"
			}
		
		));
		table_2.setModel(defaultTableModel); // �������ݴ洢��model��
		defaultTableModel.fireTableDataChanged();// ˢ������
		scrollPane.setViewportView(table_2);



		JLabel lblNewLabel = new JLabel("\u57CE\u5E02\uFF1A");
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setFont(new Font("����", Font.BOLD, 20));
		lblNewLabel.setBounds(49, 10, 130, 33);
		contentPane.add(lblNewLabel);

//		����
		textField = new JTextField();
		textField.setBounds(189, 18, 246, 21);
		contentPane.add(textField);
		textField.setColumns(10);

//	    ����
		textField_1 = new JTextField();
		textField_1.setColumns(10);
		textField_1.setBounds(189, 61, 246, 21);
		contentPane.add(textField_1);

		JButton btnNewButton = new JButton("\u641C\u7D22");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
//				����
				
				if ((textField.getText().length() != 0) && (textField_1.getText().length() != 0)) {
					String city=textField_1.getText();
					String community=textField.getText();
					epidemic_1.inquireabf(city, community);
					Updatetable(table_2);
				} else {
					Updatetable(table_2);
				}
			}
		});
		btnNewButton.setFont(new Font("����", Font.BOLD, 25));
		btnNewButton.setBounds(486, 17, 97, 65);
		contentPane.add(btnNewButton);

		JButton btnNewButton_1 = new JButton("\u5220\u9664");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
//				ɾ��
				// showConfirmDialog,����ҳ���а�ť
				// contentPane���õ���λ��������Ļ�ϻ���ǰ��ҳ����
				// JOptionPane.YES_NO_OPTION=���ð�ť������
				int a = JOptionPane.showConfirmDialog(contentPane, "�������Ƿ�Ҫɾ��", "ȷ��", JOptionPane.YES_NO_OPTION);
				// a���ȷ��ʱ��0 ȡ����1
				// ��a=0��ȷ��ɾ��
				if (a == 0) {
					//����ȷ��ѡ�е�����һ�У�ͨ������getSelectedRow�������������һ��
					int bookhang = table_2.getSelectedRow();
					//ͨ�����getvalueAt�������ĳ��ĳ�е�Ԫ���ֵ���±�
					String bookidString=(String) table_2.getValueAt(bookhang, 0);
					//�ɹ����Ҫɾ�����鼮��ţ����÷���
					//ת����int��Integer.valueOf(bookidString);
					int bookid=Integer.valueOf(bookidString);
				    epidemic_1.deleteid(bookid);
					// ɾ���ɹ�֮����ߵı����Ҫ����ˢ������
					// ˢ������֮ǰ������Ҫ������
				    Updatetable(table_2);
				}

			}
		});
		btnNewButton_1.setFont(new Font("����", Font.BOLD, 25));
		btnNewButton_1.setBounds(636, 17, 97, 65);
		contentPane.add(btnNewButton_1);

		JButton btnNewButton_1_1 = new JButton("\u6DFB\u52A0");
		btnNewButton_1_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
//				���
				//�����µĴ���
//				new home_jframe().show();
				home_jframe home_jframe=new home2();
				home_jframe.setVisible(true);
//				new home2();
//				this.dispose();�ͷŴ���
			}
		});
		btnNewButton_1_1.setFont(new Font("����", Font.BOLD, 25));
		btnNewButton_1_1.setBounds(791, 17, 97, 61);
		contentPane.add(btnNewButton_1_1);

		JLabel lblNewLabel_1 = new JLabel("\u793E\u533A\uFF1A");
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1.setFont(new Font("����", Font.BOLD, 20));
		lblNewLabel_1.setBounds(49, 49, 130, 33);
		contentPane.add(lblNewLabel_1);
	}

	public static void Updatetable(JTable table_2) {
		// ����ɹ�֮����ߵı����Ҫ����ˢ������
		// ˢ������֮ǰ������Ҫ������
		DefaultTableModel defaultTableModel = (new DefaultTableModel(epidemic_1.inquireall(),
				new String[] { 				"\u7F16\u53F7", "\u57CE\u5E02", "\u793E\u533A", "\u59D3\u540D", "\u6027\u522B", "\u75AB\u82D7\u7C7B\u578B", "\u7535\u8BDD\u53F7\u7801", "\u63A5\u79CD\u65F6\u95F4", "\u8EAB\u4EFD\u8BC1\u53F7\u7801" }));
		table_2.setModel(defaultTableModel); // �������ݴ洢��model��
		defaultTableModel.fireTableDataChanged();// ˢ������
	}
}
