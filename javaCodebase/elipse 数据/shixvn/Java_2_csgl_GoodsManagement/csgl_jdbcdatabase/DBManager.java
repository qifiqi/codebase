package csgl_jdbcdatabase;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import csgl_biao.tb_goods;

public class DBManager {
//��������
	private static final String qvdo="com.mysql.jdbc.Driver";
//	�������ݿ�ĵ�ַ
	private static final String rul="jdbc:mysql://localhost:3306/dbgoods";
//	�û���
	private static final String user="root";
//	����
	private static final String passwrd="123456";
//	static������������ֻҪ���оͻ����
	static {
		try {
			Class.forName(qvdo);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
//	һ������������connection����
	public static Connection getConnection() {
		Connection connection=null;
		try {
			connection=DriverManager.getConnection(rul, user, passwrd);
			return connection;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
		
	}
//	��ѯ
	public static String[][] selectSql(String sql) {
		String [][] cxvnqb = null;
		Connection connection=null;
		PreparedStatement preparedStatement;
		ResultSet resultSet;
		connection=getConnection();
		try {
			preparedStatement=connection.prepareStatement(sql);
			resultSet=preparedStatement.executeQuery();
			resultSet.last();
			// Ҫ֪���м������ݣ��ſ���׼ȷ�Ĵ�����ά����books =new String[][]
			int hanshu=resultSet.getRow();//�������
			cxvnqb=new String[hanshu][4];//����������
			resultSet.beforeFirst();//������ƶ�����ǰ��
			int i=0;
//			��ѭ����������е�ֵ���ŵ���ά������
			while(resultSet.next()) {
				cxvnqb[i][0]=String.valueOf(resultSet.getInt("goodid"));
				cxvnqb[i][2]=String.valueOf(resultSet.getInt("num"));
				
				cxvnqb[i][1]=resultSet.getString("goodname");
				
				cxvnqb[i][3]=String.valueOf(resultSet.getDouble("price"));
				i++;
			}
			close(connection,preparedStatement,resultSet);
			return cxvnqb;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
	
//	���ڶ����ѯ
	public  static boolean  pd(String sql) {
			Connection connection=null;
			ResultSet resultSet;
			connection=getConnection();
			int count=0;
			try {
				Statement st=connection.createStatement();
				resultSet=st.executeQuery(sql);
				while (resultSet.next()) {
					count=getInt(1);
				}
				if(count==0) {
					return false;
				}
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			return true;
		
		

		
	}
private static int getInt(int i) {
		// TODO Auto-generated method stub
		return 0;
	}
	//	����ɾ���޸�
	public static boolean excuteSQL(tb_goods tb_goods) {
		Connection connection=null;
		PreparedStatement preparedStatement;
		connection=getConnection();
		String sql="INSERT INTO tb_goods VALUES(?,?,?,?)";
		try {
			preparedStatement=connection.prepareStatement(sql);
			
			preparedStatement.setInt(1, tb_goods.getGoodid());
			preparedStatement.setInt(3, tb_goods.getNum());
			
			preparedStatement.setString(2, tb_goods.getGoodname());
			
			preparedStatement.setDouble(4, tb_goods.getPrice());
			int a=preparedStatement.executeUpdate();
//			ͬ��
			close1(connection, preparedStatement);
			if (a ==0) {
				return true;
			}else {
				return false;
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return false;
	}
//	������ͬ�Ĺرշ���
	private static void close(Connection connection,PreparedStatement preparedStatement,ResultSet resultSet) {
		try {
			resultSet.close();
			preparedStatement.close();
			connection.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	private static void close1(Connection connection,PreparedStatement preparedStatement) {
		try {
			preparedStatement.close();
			connection.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	
	
	
	
	
	
	
	
	
	
	
}
