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
	 * ��������
	 */
	static {
		try {
			Class.forName(DIRVER_CLASS);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
	/**
	 * �������ݿ�����
	 * @return
	 */
	public static Connection getConnection() {
		try {
			//ʹ�������������������ݿ�
			connection = DriverManager.getConnection(DIRVER_URL, USERRNAME, DIRVER_CLASS);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return connection;
	}
	
	/**
	 * �ر����ݿ�����
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
	 * ��ѯͨ�÷���
	 * @param sql sql���
	 * @param params ��������
	 * @return
	 */
	
	public static ResultSet select(String sql,Object...params) {
		connection = getConnection(); //����
		try {
			//Ԥ����sql��䣬׼����Ӳ���������sql�����?��user_name=?
			statement = connection.prepareStatement(sql);
			if (params != null && params.length >0) {
				//������ר����һ������ȥ��
				setValue(statement,params);	
			}
			//ִ�д���õ�sql���õ����
			resultSet = statement.executeQuery();
		} catch (SQLException e) {
			
		}
		return resultSet;
	}
	
	/**
	 * ��ɾ��ִ�еķ���
	 * @param sql
	 * @param params
	 * @return
	 */
	public static int update(String sql,Object...params) {
		int result = 0;
		connection = getConnection();
		try {
			//Ԥ����
			statement = connection.prepareStatement(sql);
			if (params != null && params.length >0) {
				setValue(statement, params);
			}
			//��ɾ�ķ��ص�Ӱ�������
			result = statement.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			//��Ϊ��ɾ��ֱ�ӷ��ص���int���֣�������Դ���������ͷ�
			close();
		}
		return result;
	}
	
	
	
	
	
	
	/**
	 * ��statement����Ĳ����󶨷���������
	 * @param preparedStatement
	 * @param params
	 */

	private static void setValue(PreparedStatement preparedStatement, Object[] params) {
		for (int i =0; i < params.length;i++) {
			try {
				//ѭ�����ݹ����Ĳ������飬�������ֵһ��һ������Ԥ�����sql������?
				preparedStatement.setObject(i+1,params[i]);
			} catch (SQLException e) {
				
			}
			
		}
		
	}



}
