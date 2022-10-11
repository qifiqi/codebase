package com.lz.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class BaseDAO {

	//连接对象
	Connection con=null;
	//执行增删改的对象
	PreparedStatement psmt=null;
	//存放查询结果的对象
	ResultSet rs=null;
	//打开连接方法
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
	//通用的增删改方法
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
	//通用的查询方法，可以返回二维数组
	public Object[][] Find(String sql){	
		try {
			conn();
			psmt=con.prepareStatement(sql);
			rs=psmt.executeQuery();
			//获取总列数
			int cols=rs.getMetaData().getColumnCount();
			//移到最后一行
			rs.last();
			//获取总行数
			int rows=rs.getRow();
			//根据行数和列数创建二维数组
			Object[][] objs=new Object[rows][cols];
			//移到第一行
			rs.beforeFirst();
			//从第0行开始读取数据
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
	//关闭连接方法
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
