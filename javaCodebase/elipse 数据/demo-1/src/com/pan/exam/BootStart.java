package com.pan.exam;

import java.sql.ResultSet;
import java.sql.SQLException;

import com.pan.exam.dao.BaseDao;
import com.pan.exam.page.*;

public class BootStart {

	public static void main(String[] args) {
        MainFrame main = new MainFrame();
        main.pack();
        main.setVisible(true);
        
        String sql = "select * from user;";
        
        ResultSet resultSet = BaseDao.select(sql);
        try {
			while (resultSet.next()) {
				System.out.println(resultSet.getString("name"));
				
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}

	}

}
