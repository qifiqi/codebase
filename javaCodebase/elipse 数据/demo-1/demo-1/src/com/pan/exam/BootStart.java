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
        System.out.println("���ݿ���������ɹ���");

	}
}
