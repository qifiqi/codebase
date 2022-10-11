package com.pan.exam.dao;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;



import com.pan.exam.model.*;

public class PersonnelDao extends BaseDao {
	/**
	 * 添加方法
	 * @param personnel 用户对象
	 * @return
	 */
	public boolean add(Personnel personnel) {
		String sql = "insert into employee(user_name,phone,age,gender,salary,department) value(?,?,?,?,?,?)";
		int result = update(sql,
				personnel.getPersonnel_name(),
				personnel.getPhone(),
				personnel.getAge(),
				personnel.getSex(),
				personnel.getSalary(),
				personnel.getDepartment()
				);
		return result == 1;
	}
	
    public ArrayList<Personnel> getAll(){
    	return this.search(null);
    }

	public ArrayList<Personnel> search(String content){
		ArrayList<Personnel> list = new ArrayList<>();
		ResultSet resultSet = null;
		String sql;
		//根据是否有查询参数使用不同的sql语句，一个是拿所有， 一个是用户名的模糊搜索
		if (null == content) {
			sql = "select * from Employee ";
			
		}else {
			sql = "select * from Employee where user_name like concat('%','"+content+"','%')"; //%xxx%
	
		}
		//调用查询方法获取数据
		resultSet = select(sql);
		try {
			while (resultSet.next()) {
				//将结果循环遍历组装为用户对象
				Personnel personnel = new Personnel(
						resultSet.getInt("em_id"),
						resultSet.getString("user_name"),
						resultSet.getString("phone"),
						resultSet.getString("gender"),
						resultSet.getString("department"),
						resultSet.getInt("age"),
						resultSet.getDouble("salary")
						);
				list.add(personnel);

				
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return list;
	}
	
	/**
	 * 删除方法
	 * @param id  需要删除的用户id
	 * @return
	 */
	public  void delete(int id) {
		String sql = "delete from Employee where em_id = ?";
		update(sql,id);
		
	}


}
