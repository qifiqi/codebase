package csgl_jdbcdatabase;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import csgl_biao.tb_goods;

public class DBManager {
//加载驱动
	private static final String qvdo="com.mysql.jdbc.Driver";
//	连接数据库的地址
	private static final String rul="jdbc:mysql://localhost:3306/dbgoods";
//	用户名
	private static final String user="root";
//	密码
	private static final String passwrd="123456";
//	static方法加载驱动只要运行就会加载
	static {
		try {
			Class.forName(qvdo);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
//	一个方法来返回connection对象
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
//	查询
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
			// 要知道有几条数据，才可以准确的创建二维数组books =new String[][]
			int hanshu=resultSet.getRow();//获得行数
			cxvnqb=new String[hanshu][4];//行数和列数
			resultSet.beforeFirst();//将光标移动到最前面
			int i=0;
//			用循环来获得所有的值并放到二维数组中
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
	
//	用于定点查询
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
	//	增加删除修改
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
//			同理
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
//	两个不同的关闭方法
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
