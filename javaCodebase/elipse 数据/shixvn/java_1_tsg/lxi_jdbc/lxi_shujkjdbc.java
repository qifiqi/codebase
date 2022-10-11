package lxi_jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import lxi_biao.*;

public class lxi_shujkjdbc {
	private static final String qvdo = "com.mysql.jdbc.Driver";
	private static final String URL = "jdbc:mysql://localhost:3306/testdb";
	private static final String USER = "root";
	private static final String PASSWORD = "123456";

	static {
		try {
			// 加载驱动
			Class.forName(qvdo);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static Connection getConnection() {
		Connection conn = null;
		try {
			// 连接数据库
			conn = DriverManager.getConnection(URL, USER, PASSWORD);
			return conn;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return conn;
	}


	// 插入修改数据到bookinfo
	public static void insertandxgaibookinfo(bookinfo bookinfo) {
		Connection conn = null;
		PreparedStatement preparedStatement = null;
		String sql="INSERT INTO bookinfo VALUES(0,?,?,?,?,?)";
		conn = getConnection();
		try {
			preparedStatement = conn.prepareStatement(sql);
			preparedStatement.setString(1, bookinfo.getBookname());
			preparedStatement.setString(2, bookinfo.getBookauthor());
			preparedStatement.setString(3, bookinfo.getBookpublish());
			preparedStatement.setFloat(4, bookinfo.getBookprice());
			preparedStatement.setString(5, bookinfo.getBooktype());
			int count = preparedStatement.executeUpdate();
			if (count > 0) {
				System.out.println("成功");
			} else {
				System.out.println("失败");
			}
			close1(conn, preparedStatement);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
	// 修改数据到bookinfo
		public static void xgaibookinfo(bookinfo bookinfo) {
			Connection conn = null;
			PreparedStatement preparedStatement = null;
			String sql="INSERT INTO bookinfo VALUES(?,?,?,?,?,?)";
			conn = getConnection();
			try {
				preparedStatement = conn.prepareStatement(sql);
				preparedStatement.setInt(1, bookinfo.getBookid());
				preparedStatement.setString(2, bookinfo.getBookname());
				preparedStatement.setString(3, bookinfo.getBookauthor());
				preparedStatement.setString(3, bookinfo.getBookpublish());
				preparedStatement.setFloat(5, bookinfo.getBookprice());
				preparedStatement.setString(6, bookinfo.getBooktype());
				int count = preparedStatement.executeUpdate();
				if (count > 0) {
					System.out.println("成功");
				} else {
					System.out.println("失败");
				}
				close1(conn, preparedStatement);
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		}
	// 根据id删除
	public static void deletebookinfo(int bookid) {
		Connection conn = null;
		PreparedStatement preparedStatement = null;
		String sql = "DELETE FROM bookinfo WHERE bookid=?";
		conn = getConnection();
		try {
			preparedStatement = conn.prepareStatement(sql);
			preparedStatement.setInt(1, bookid);
			int count = preparedStatement.executeUpdate();
			if (count > 0) {
				System.out.println("删除成功");
			} else {
				System.out.println("删除失败");
			}
			close1(conn, preparedStatement);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	public static String[][] getAllbookinfo() {
		// 定义返回类型的变量
		String[][] books = null;
		Connection conn = null;
		PreparedStatement preparedStatement = null;
		ResultSet resultSet;
		String sql = "SELECT * FROM bookinfo";
		conn = getConnection();
		try {
			preparedStatement = conn.prepareStatement(sql);
			resultSet = preparedStatement.executeQuery();// 这个方法的返回值是一个结果集
			// 要知道有几条数据，才可以准确的创建二维数组books =new String[][]
			resultSet.last();
			int rows = resultSet.getRow();// 获取当前行数
			books = new String[rows][6];// [行数][列数]
			resultSet.beforeFirst();
//			resultSet.last();可以使用的固定结构
//			int rows = resultSet.getRow();//获取当前行数
//			books =new String[rows][6];//[行数][列数]
//			resultSet.beforeFirst();光标移到最前面
		   int i=0;
			while (resultSet.next()) {
				books[i][0]= String.valueOf(resultSet.getInt("bookid"));
				
				//顺序尽量按照页面前端来
				books[i][1]= resultSet.getString("bookname");
				books[i][2] = resultSet.getString("bookauthor");
				books[i][3] = resultSet.getString("bookpublish");
				books[i][5] = resultSet.getString("booktype");

				books[i][4] = String.valueOf(resultSet.getFloat("bookprice"));
				i++;
			}
			close(conn, preparedStatement, resultSet);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return books;

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
