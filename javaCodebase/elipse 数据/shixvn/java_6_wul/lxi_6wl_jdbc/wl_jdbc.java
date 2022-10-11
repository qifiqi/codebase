package lxi_6wl_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class wl_jdbc {
	private static final String QVDO_STRING ="com.mysql.jdbc.Driver";
	private static final String URL_STRING ="jdbc:mysql://localhost:3306/orederdb";
	private static final String USER_STRING ="root";
	private static final String PASSWORD_STRING ="123456";
	
	
	static {
		try {
			Class.forName(QVDO_STRING);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static Connection getConnection() {
		try {
			Connection conn=DriverManager.getConnection(URL_STRING, USER_STRING, PASSWORD_STRING);
			return conn;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
		
	}
	
	
//	��ѯ
	public static String[][] getAllcvn() {
		// ���巵�����͵ı���
		String[][] books = null;
		Connection conn = null;
		PreparedStatement preparedStatement = null;
		ResultSet resultSet;
		String sql = "SELECT * FROM tb_order";
		conn = getConnection();
		try {
			preparedStatement = conn.prepareStatement(sql);
			resultSet = preparedStatement.executeQuery();// ��������ķ���ֵ��һ�������
			// Ҫ֪���м������ݣ��ſ���׼ȷ�Ĵ�����ά����books =new String[][]
			resultSet.last();
			int rows = resultSet.getRow();// ��ȡ��ǰ����
			books = new String[rows][6];// [����][����]
			resultSet.beforeFirst();
//			resultSet.last();����ʹ�õĹ̶��ṹ
//			int rows = resultSet.getRow();//��ȡ��ǰ����
//			books =new String[rows][6];//[����][����]
//			resultSet.beforeFirst();����Ƶ���ǰ��
		   int i=0;
			while (resultSet.next()) {
				books[i][0]= String.valueOf(resultSet.getInt("id"));
				
				//˳��������ҳ��ǰ����
				books[i][1]= resultSet.getString("name");
				books[i][3] = resultSet.getString("orderid");
				books[i][4] = resultSet.getString("descinfo");

				books[i][2] = String.valueOf(resultSet.getDouble("price"));
				i++;
			}
			close(conn, preparedStatement, resultSet);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return books;

	}
	
//	��ѯ
	public static String[][] getAllcvnid(String orderid) {
		// ���巵�����͵ı���
		String[][] books = null;
		Connection conn = null;
		PreparedStatement preparedStatement = null;
		ResultSet resultSet;
		String sql = "SELECT * FROM tb_order where orderid=?";
		conn = getConnection();
		try {
			preparedStatement = conn.prepareStatement(sql);
			preparedStatement.setString(1, orderid);
			resultSet = preparedStatement.executeQuery();// ��������ķ���ֵ��һ�������
			// Ҫ֪���м������ݣ��ſ���׼ȷ�Ĵ�����ά����books =new String[][]
			resultSet.last();
			int rows = resultSet.getRow();// ��ȡ��ǰ����
			books = new String[rows][6];// [����][����]
			resultSet.beforeFirst();
//			resultSet.last();����ʹ�õĹ̶��ṹ
//			int rows = resultSet.getRow();//��ȡ��ǰ����
//			books =new String[rows][6];//[����][����]
//			resultSet.beforeFirst();����Ƶ���ǰ��
		   int i=0;
			while (resultSet.next()) {
				books[i][0]= String.valueOf(resultSet.getInt("id"));
				
				//˳��������ҳ��ǰ����
				books[i][1]= resultSet.getString("name");
				books[i][3] = resultSet.getString("orderid");
				books[i][4] = resultSet.getString("descinfo");

				books[i][2] = String.valueOf(resultSet.getDouble("price"));
				i++;
			}
			close(conn, preparedStatement, resultSet);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return books;

	}
	// ����idɾ��
		public static void deletebookinfo(int id) {
			Connection conn = null;
			PreparedStatement preparedStatement = null;
			String sql = "DELETE FROM tb_order WHERE id=?";
			conn = getConnection();
			try {
				preparedStatement = conn.prepareStatement(sql);
				preparedStatement.setInt(1, id);
				int count = preparedStatement.executeUpdate();
				if (count > 0) {
					System.out.println("ɾ���ɹ�");
				} else {
					System.out.println("ɾ��ʧ��");
				}
				close1(conn, preparedStatement);
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		}
	public static void close(Connection conn, PreparedStatement preparedStatement, ResultSet resultSet) {
		try {
			resultSet.close();
			preparedStatement.close();
			conn.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public static void close1(Connection conn, PreparedStatement preparedStatement) {
		try {
			preparedStatement.close();
			conn.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
