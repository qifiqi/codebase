package com.tang.exam.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Iterator;

public class BaseDao {
	private static final String DIRVER_CLASS = "com.mysql.jdbc.driver";
	private static final String DIRVER_URL = "jdbc:mysql://192.168.0.38/exam";
	private static final String USERRNAME = "root";
	private static final String PADDWORD = "123456";
	
	
	protected static Connection connection;
	protected static PreparedStatement statement;
	protected static ResultSet resultSet;
	
	
	/**
	 * 加载驱动
	 */
	static {
		try {
			Class.forName(DIRVER_CLASS);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
	/**
	 * 建立数据库连接
	 * @return
	 */
	public static Connection getConnection() {
		try {
			//使用驱动管理器连接数据库
			connection = DriverManager.getConnection(DIRVER_URL, USERRNAME, DIRVER_CLASS);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return connection;
	}
	
	/**
	 * 关闭数据库连接
	 */
	public static void close() {
		try {
			//
			if (resultSet != null) {
				resultSet.close();	
			}
			if (statement != null) {
				statement.close();
				
			}
			if (connection != null) {
				connection.close();
				
			}
		} catch (SQLException e) {
			e.printStackTrace();
		
		}
	}
	/**
	 * 查询通用方法
	 * @param sql sql语句
	 * @param params 参数数组
	 * @return
	 */
	
	public static ResultSet select(String sql,Object...params) {
		connection = getConnection(); //连接
		try {
			//预处理sql语句，准备添加参数，结束sql里面的?：user_name=?
			statement = connection.prepareStatement(sql);
			if (params != null && params.length >0) {
				//参数绑定专门让一个方法去做
				setValue(statement,params);	
			}
			//执行处理好的sql语句得到结果
			resultSet = statement.executeQuery();
		} catch (SQLException e) {
			
		}
		return resultSet;
	}
	
	/**
	 * 增删改执行的方法
	 * @param sql
	 * @param params
	 * @return
	 */
	public static int update(String sql,Object...params) {
		int result = 0;
		connection = getConnection();
		try {
			//预处理
			statement = connection.prepareStatement(sql);
			if (params != null && params.length >0) {
				setValue(statement, params);
			}
			//增删改返回的影响的行数
			result = statement.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			//因为增删改直接返回的是int数字，所以资源可以立马释放
			close();
		}
		return result;
	}
	
	
	
	
	
	
	/**
	 * 对statement对象的参数绑定方法？？？
	 * @param preparedStatement
	 * @param params
	 */

	private static void setValue(PreparedStatement preparedStatement, Object[] params) {
		for (int i =0; i < params.length;i++) {
			try {
				//循环传递过来的参数数组，将里面的值一个一个放入预处理的sql，代替?
				preparedStatement.setObject(i+1,params[i]);
			} catch (SQLException e) {
				
			}
			
		}
		
	}



}
