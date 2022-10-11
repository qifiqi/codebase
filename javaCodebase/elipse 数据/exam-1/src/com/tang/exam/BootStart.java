package com.tang.exam;

import java.sql.ResultSet;
import java.sql.SQLException;

import com.tang.exam.dao.BaseDao;
import com.tang.exam.page.*;

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
