package vacation_shujvku;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import vacation_biao.inoculatetable;

public class epidemic_1 {
	private final static String drive = "com.mysql.jdbc.Driver";
	private final static String rul = "jdbc:mysql://localhost:3306/epidemic";
	private final static String user = "root";
	private final static String pasword = "123456";
	static {
		try {
			Class.forName(drive);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static Connection getconnection() {
		Connection connection = null;
		try {
			connection = DriverManager.getConnection(rul, user, pasword);
			return connection;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;

	}

//	��ѯȫ���ķ���
	@SuppressWarnings("static-access")
	public static String[][] inquireall() {
		String[][] aaa = null;
		String sql="SELECT * FROM inoculatetable";
		Connection connection = getconnection();
		PreparedStatement preparedStatement = null;
		ResultSet resultSet;
		try {
			preparedStatement = connection.prepareStatement(sql);
			resultSet = preparedStatement.executeQuery();
			resultSet.last();
			// Ҫ֪���м������ݣ��ſ���׼ȷ�Ĵ�����ά����books =new String[][]
			int hanshu = resultSet.getRow();// �������
			aaa = new String[hanshu][9];// ����������
			resultSet.beforeFirst();// ������ƶ�����ǰ��
			int i = 0;
//			��ѭ����������е�ֵ���ŵ���ά������
			while (resultSet.next()) {
				aaa[i][0]=String.valueOf(resultSet.getInt("inoculateid"));
//��������һ��Ҫ�Ͷ�ά��������һ�£���һ�¾�ת�����������Object
				aaa[i][1]=String.valueOf(resultSet.getString("city"));
				aaa[i][2]=String.valueOf(resultSet.getString("community"));
				aaa[i][3]=String.valueOf(resultSet.getString("name"));
				aaa[i][4]=String.valueOf(resultSet.getString("gender"));
				aaa[i][5]=String.valueOf(resultSet.getString("type"));
				aaa[i][6]=String.valueOf(resultSet.getString("phone"));
				aaa[i][8]=String.valueOf(resultSet.getString("id_number"));
				aaa[i][7]=String.valueOf(resultSet.getString("time"));
				i++;
			}
			close(connection, preparedStatement, resultSet);
			return aaa;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return aaa;

	}

//	�����ѯ�ķ���
	@SuppressWarnings("static-access")
	public static String[][] inquireabf(String city,String community) {
		String[][] aaa = null;
		String sql="select * from inoculatetable where city=? and community=?; ";
		Connection connection = getconnection();
		PreparedStatement preparedStatement = null;
		ResultSet resultSet;
		try {
			preparedStatement = connection.prepareStatement(sql);
			preparedStatement.setString(1, city);
			preparedStatement.setString(2, community);
			resultSet = preparedStatement.executeQuery();
			resultSet.last();
			// Ҫ֪���м������ݣ��ſ���׼ȷ�Ĵ�����ά����books =new String[][]
			int hanshu = resultSet.getRow();// �������
			aaa = new String[hanshu][9];// ����������
			resultSet.beforeFirst();// ������ƶ�����ǰ��
			int i = 0;
//			��ѭ����������е�ֵ���ŵ���ά������
			while (resultSet.next()) {
				aaa[i][0]=String.valueOf(resultSet.getInt("inoculateid"));

				aaa[i][1]=String.valueOf(resultSet.getString("city"));
				aaa[i][2]=String.valueOf(resultSet.getString("community"));
				aaa[i][3]=String.valueOf(resultSet.getString("name"));
				aaa[i][4]=String.valueOf(resultSet.getString("gender"));
				aaa[i][5]=String.valueOf(resultSet.getString("type"));
				aaa[i][6]=String.valueOf(resultSet.getString("phone"));
				aaa[i][8]=String.valueOf(resultSet.getString("id_number"));
				aaa[i][7]=String.valueOf(resultSet.getString("time"));
				i++;
			}
			close(connection, preparedStatement, resultSet);
			return aaa;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return aaa;

	}

//	���
	@SuppressWarnings("static-access")
	public static boolean addmodification(inoculatetable inoculatetable) {
		Connection connection = getconnection();
		PreparedStatement preparedStatement = null;
		String sql = "INSERT INTO inoculatetable VALUES(NULL,?,?,?,?,?,?,?,?);";
		try {
			preparedStatement=connection.prepareStatement(sql);
			
			preparedStatement.setString(1, inoculatetable.getCity());
			preparedStatement.setString(2, inoculatetable.getCommunity());
			preparedStatement.setString(3, inoculatetable.getName());
			preparedStatement.setString(4, inoculatetable.getGender());
			preparedStatement.setString(5, inoculatetable.getType());
			preparedStatement.setString(6, inoculatetable.getPhone());
			preparedStatement.setString(8, inoculatetable.getId_number());
			preparedStatement.setString(7, inoculatetable.getTime());

			int a=preparedStatement.executeUpdate();
//			ͬ��
			close1(connection, preparedStatement);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return false;

	}

//	�޸�
	public static void update1() {
		Connection connection = getconnection();
		PreparedStatement preparedStatement = null;
		String sql = "";
	}

//	ɾ��
	public static void deleteid(int id) {
		Connection connection = getconnection();
		PreparedStatement preparedStatement = null;
		String sql = "DELETE FROM inoculatetable WHERE inoculateid=?;";
		try {
			preparedStatement=connection.prepareStatement(sql);
			preparedStatement.setInt(1, id);
			int a=preparedStatement.executeUpdate();
//			ͬ��
			close1(connection, preparedStatement);
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	
	}

//	������ͬ�Ĺرշ���
	private static void close(Connection connection, PreparedStatement preparedStatement, ResultSet resultSet) {
		try {
			resultSet.close();
			preparedStatement.close();
			connection.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	private static void close1(Connection connection, PreparedStatement preparedStatement) {
		try {
			preparedStatement.close();
			connection.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}


}
