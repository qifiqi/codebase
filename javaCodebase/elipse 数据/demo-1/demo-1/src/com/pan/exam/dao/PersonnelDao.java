package com.pan.exam.dao;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;



import com.pan.exam.model.*;

public class PersonnelDao extends BaseDao {
	/**
	 * ��ӷ���
	 * @param personnel �û�����
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
		//�����Ƿ��в�ѯ����ʹ�ò�ͬ��sql��䣬һ���������У� һ�����û�����ģ������
		if (null == content) {
			sql = "select * from Employee ";
			
		}else {
			sql = "select * from Employee where user_name like concat('%','"+content+"','%')"; //%xxx%
	
		}
		//���ò�ѯ������ȡ����
		resultSet = select(sql);
		try {
			while (resultSet.next()) {
				//�����ѭ��������װΪ�û�����
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
	 * ɾ������
	 * @param id  ��Ҫɾ�����û�id
	 * @return
	 */
	public  void delete(int id) {
		String sql = "delete from Employee where em_id = ?";
		update(sql,id);
		
	}


}
