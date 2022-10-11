package com.pan.exam;


import java.sql.SQLException;

import com.pan.exam.dao.BaseDao;
import com.pan.exam.page.*;

public class BootStart {

	public static void main(String[] args) {
        MainFrame main = new MainFrame();
        BaseDao baseDao = new BaseDao();
        main.pack();
        main.setVisible(true);
        baseDao.getConnection(); 
        System.out.println("数据库加载驱动成功！");

	}
}
