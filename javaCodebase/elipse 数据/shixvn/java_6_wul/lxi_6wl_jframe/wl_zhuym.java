package lxi_6wl_jframe;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JScrollPane;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Font;
import javax.swing.SwingConstants;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import javax.swing.ListSelectionModel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import lxi_6wl_jdbc.*;
import lxi_jdbc.lxi_shujkjdbc;
public class wl_zhuym extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JTable table;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					wl_zhuym frame = new wl_zhuym();
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
	public wl_zhuym() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 780, 493);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBounds(10, 101, 744, 311);
		contentPane.add(panel);
		panel.setLayout(new BorderLayout(0, 0));
		
		JScrollPane scrollPane = new JScrollPane();
		panel.add(scrollPane, BorderLayout.CENTER);
		
		table = new JTable();
		table.setCellSelectionEnabled(true);
		table.setSelectionMode(ListSelectionModel.SINGLE_INTERVAL_SELECTION);
		table.setModel(new DefaultTableModel(
			wl_jdbc.getAllcvn(),
			new String[] {
				"\u7F16\u53F7", "\u5546\u54C1\u540D\u79F0", "\u5546\u54C1\u4EF7\u683C", "\u8BA2\u5355\u7F16\u53F7", "\u8BA2\u5355\u63CF\u8FF0"
			}
		) {
			boolean[] columnEditables = new boolean[] {
				false, true, true, true, true
			};
			public boolean isCellEditable(int row, int column) {
				return columnEditables[column];
			}
		});
		scrollPane.setViewportView(table);
		
		JLabel lblNewLabel = new JLabel("\u8BA2\u5355\u7F16\u53F7\uFF1A");
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setFont(new Font("����", Font.BOLD, 16));
		lblNewLabel.setBounds(10, 70, 171, 21);
		contentPane.add(lblNewLabel);
		
		textField = new JTextField();
		textField.setBounds(195, 70, 427, 21);
		contentPane.add(textField);
		textField.setColumns(10);
		
		JButton btnNewButton = new JButton("\u641C\u7D22");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JOptionPane.showMessageDialog(contentPane, "����");
				String orderid=textField.getText();
				lxi_6wl_jdbc.wl_jdbc.getAllcvnid(orderid);
				
				DefaultTableModel defaultTableModel=(new DefaultTableModel(
						wl_jdbc.getAllcvn(),
						new String[] {
							"\u7F16\u53F7", "\u5546\u54C1\u540D\u79F0", "\u5546\u54C1\u4EF7\u683C", "\u8BA2\u5355\u7F16\u53F7", "\u8BA2\u5355\u63CF\u8FF0"
						}
					) {
						boolean[] columnEditables = new boolean[] {
							false, true, true, true, true
						};
						public boolean isCellEditable(int row, int column) {
							return columnEditables[column];
						}
					});
					

				// �������ݴ洢��model��
				table.setModel(defaultTableModel);
				defaultTableModel.fireTableDataChanged();// ˢ������

			}
		});
		btnNewButton.setBounds(632, 69, 126, 23);
		contentPane.add(btnNewButton);
		
		JButton btnNewButton_1 = new JButton("\u5220\u9664");
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				// ɾ��
				// showConfirmDialog,����ҳ���а�ť
				// contentPane���õ���λ��������Ļ�ϻ���ǰ��ҳ����
				// JOptionPane.YES_NO_OPTION=���ð�ť������
				int a = JOptionPane.showConfirmDialog(contentPane, "�������Ƿ�Ҫɾ��", "ȷ��", JOptionPane.YES_NO_OPTION);
				// a���ȷ��ʱ��0 ȡ����1
				// ��a=0��ȷ��ɾ��
				if (a == 0) {
					//����ȷ��ѡ�е�����һ�У�ͨ������getSelectedRow�������������һ��
					int hang = table.getSelectedRow();
					//ͨ�����getvalueAt�������ĳ��ĳ�е�Ԫ���ֵ���±�
					String idString=table.getValueAt(hang, 0).toString();
					//�ɹ����Ҫɾ�����鼮��ţ����÷���
					//ת����int��Integer.valueOf(idString);
					int id=Integer.valueOf(idString);
					lxi_6wl_jdbc.wl_jdbc.deletebookinfo(id);
					// ɾ���ɹ�֮����ߵı����Ҫ����ˢ������
					// ˢ������֮ǰ������Ҫ������
					
					
					DefaultTableModel defaultTableModel=(new DefaultTableModel(
							wl_jdbc.getAllcvn(),
							new String[] {
								"\u7F16\u53F7", "\u5546\u54C1\u540D\u79F0", "\u5546\u54C1\u4EF7\u683C", "\u8BA2\u5355\u7F16\u53F7", "\u8BA2\u5355\u63CF\u8FF0"
							}
						) {
							boolean[] columnEditables = new boolean[] {
								false, true, true, true, true
							};
							public boolean isCellEditable(int row, int column) {
								return columnEditables[column];
							}
						});
						

					// �������ݴ洢��model��
					table.setModel(defaultTableModel);
					defaultTableModel.fireTableDataChanged();// ˢ������

			  }
			
				
				
				
				
			}
		});
		btnNewButton_1.setBounds(661, 422, 93, 23);
		contentPane.add(btnNewButton_1);
		
		JLabel lblNewLabel_1 = new JLabel("\u7269\u6D41\u8DDF\u8E2A\u7BA1\u7406\u7CFB\u7EDF");
		lblNewLabel_1.setFont(new Font("����", Font.BOLD, 44));
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1.setBounds(93, 10, 593, 50);
		contentPane.add(lblNewLabel_1);
	}
}
