package com.lz.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class BaseDAO {

	//���Ӷ���
	Connection con=null;
	//ִ����ɾ�ĵĶ���
	PreparedStatement psmt=null;
	//��Ų�ѯ����Ķ���
	ResultSet rs=null;
	//�����ӷ���
	public void conn(){
		
		try {
			Class.forName("com.mysql.jdbc.Driver");
			con=DriverManager.getConnection("jdbc:mysql://localhost:3306/dbgoods", "root", "123456");
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	//ͨ�õ���ɾ�ķ���
	public boolean Execute(String sql,Object[] obj){
		try {
			conn();
			psmt=con.prepareStatement(sql);
			for(int i=0;i<obj.length;i++){
				psmt.setObject(i+1, obj[i]);
			}
			int cnt=psmt.executeUpdate();
			if(cnt>0)
				return true;
			return false;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}
		finally{
			close();
		}
	}
	//ͨ�õĲ�ѯ���������Է��ض�ά����
	public Object[][] Find(String sql){	
		try {
			conn();
			psmt=con.prepareStatement(sql);
			rs=psmt.executeQuery();
			//��ȡ������
			int cols=rs.getMetaData().getColumnCount();
			//�Ƶ����һ��
			rs.last();
			//��ȡ������
			int rows=rs.getRow();
			//��������������������ά����
			Object[][] objs=new Object[rows][cols];
			//�Ƶ���һ��
			rs.beforeFirst();
			//�ӵ�0�п�ʼ��ȡ����
			int i=0;
			while(rs.next()){
				for(int j=1;j<=rs.getMetaData().getColumnCount();j++){
					objs[i][j-1]=rs.getObject(j);
				}
				i++;
			}
			return objs;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		}
		finally{
			close();
		}
	}
	//�ر����ӷ���
	public void close(){
		try {
			if(rs!=null && !rs.isClosed()){
				rs.close();
				rs=null;
			}
			if(psmt!=null && !psmt.isClosed()){
				psmt.close();
				psmt=null;
			}
			if(con!=null && !con.isClosed()){
				con.close();
				con=null;
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
