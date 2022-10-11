package com.lz.java;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.filter.PageFilter;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.*;
import java.util.Scanner;

public class studentMange {
    boolean quit = true;
    private final String[] col = {"col1","col2"};
    private static final String zkslave = "master,slave01,slave02";
    static Connection conn=null;
    static TableName tableName = null;
    static Scanner scanner = null;
    static Table table = null;

    //创建连接
    static {
        Configuration conf = HBaseConfiguration.create();
        conf.set("hbase.zookeeper.quorum",zkslave);
        //创建连接
        try {
            conn = ConnectionFactory.createConnection(conf);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * 添加到hbase-put单条添加1
     * @param student 学生的实体类
     */
    private void AddStudent(Student student){
        //读取rowkey
        File file = new File("src/main/java/com/lz/java/resource/rowkey.txt");
        Scanner sc = null;
        try {
            sc = new Scanner(file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        assert sc != null;
        sc.useDelimiter("\\Z");
        int sid = sc.nextInt();

        Put put = new Put(Bytes.toBytes(sid));
        put.addColumn(Bytes.toBytes(col[0]),Bytes.toBytes("id"),Bytes.toBytes(String.valueOf(sid)));
        put.addColumn(Bytes.toBytes(col[0]),Bytes.toBytes("name"),Bytes.toBytes(student.getStu_name()));
        put.addColumn(Bytes.toBytes(col[0]),Bytes.toBytes("sex"),Bytes.toBytes(student.getSex()));
        put.addColumn(Bytes.toBytes(col[1]),Bytes.toBytes("source"),Bytes.toBytes(student.getScource()));
        put.addColumn(Bytes.toBytes(col[1]),Bytes.toBytes("class_name"),Bytes.toBytes(student.getClass_name()));
        try {
            table.put(put);
        } catch (IOException e) {
            e.printStackTrace();
        }
        sid++;
        //写入rowkey
        try {
            file.createNewFile(); // 创建新文件,有同名的文件的话直接覆盖        }
            FileOutputStream fos = new FileOutputStream(file, false);
            OutputStreamWriter osw = new OutputStreamWriter(fos);
            BufferedWriter bw = new BufferedWriter(osw);
            bw.write(String.valueOf(sid));
            bw.newLine();
            bw.flush();
            bw.close();
            osw.close();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }


    }

    /**
     * 创建一个学生
     * @return 返回学生对象
     */
    private Student CreateStudent(){
        System.out.println("请输入姓名");
        String name = scanner.next();
        System.out.println("请输入性别");
        String sex = scanner.next();
        System.out.println("请输入成绩");
        String source = scanner.next();
        System.out.println("请输入班级");
        String class_name = scanner.next();
        return new Student(name,sex,source,class_name);
    }

    /**
     * 查询全部数据并分页
     */
    private void InquireAllPage(){
        Scan scan = new Scan();

        //获取总行数
        int total = 0;
        ResultScanner resultScanner = null;
        try {
            resultScanner = table.getScanner(scan);
        } catch (IOException e) {
            e.printStackTrace();
        }
        assert resultScanner != null;
        for (Result ignored : resultScanner) {
            total++;
        }
        //创建分页
        int totalPage;
        if (total%30==0){
            totalPage=total/30;
        }else {
            totalPage=total/30+1;
        }
        System.out.println("总共用"+totalPage+"页");


        int page_num = 30;
        PageFilter filter = new PageFilter(page_num);
        scan.setFilter(filter);
        boolean isFirst = true;
        int startRow = 1;
//        int row = 0;
        int page = 0;
        while (true){
//            row = 0;

            if(!isFirst){
                // 如果不是第一页就设置开始行键
                scan.setStartRow(String.valueOf(startRow).getBytes());
            }
            boolean aa = true;
            do {
                Result result = null;
                try {
                    result = table.get(new Get(Bytes.toBytes(String.valueOf(startRow))));
                } catch (IOException e) {
                    e.printStackTrace();
                }
                assert result != null;
                if (result.isEmpty()){
                    startRow++;
                }else {
                    aa = false;
                }
            }while (aa);
            ResultScanner results = null;
            try {
                results = table.getScanner(scan);
            } catch (IOException e) {
                e.printStackTrace();
            }
            assert results != null;
            for (Result value : results) {
                isFirst = false;
                byte[] idByte = value.getValue(col[0].getBytes(), "id".getBytes());
                byte[] nameByte = value.getValue(col[0].getBytes(), "name".getBytes());
                byte[] ageByte = value.getValue(col[0].getBytes(), "sex".getBytes());
                byte[] address = value.getValue(col[1].getBytes(), "source".getBytes());
                byte[] score = value.getValue(col[1].getBytes(), "class_name".getBytes());

                System.out.println(
                        "id:" + new String(idByte) +
                        "\tname:" + new String(nameByte) +
                        "\tsex:" + new String(ageByte) +
                        "\tsource:" + new String(address) +
                        "\tclass_name:" + new String(score)
                );
                startRow++;
//                row++;
            }
            page++;
            System.out.println("===========================================================");
            if (page>=totalPage){
                results.close();
                break;

            }
        }
    }

    /**
     * 条件查询
     */
    private void Conditional(){
        ConditionalQuery cond = new ConditionalQuery();

        boolean quit = true;
        while (quit){
            Hint(3);
            String num = scanner.next();
            switch (num){
                case "1":
                    cond.NameInquire(table,scanner);
                    break;
                case "2":
                    cond.ClassNameInquire(table,scanner);
                    break;
                case "3":
                    cond.SourceInquire(table,scanner);
                    break;
                case "4":
                    quit = false;
                    break;
                default:
                    System.out.println("你输入的不正确");
                    break;
            }


        }
    }

    /**
     * 按RowKey删除
     */
    private void DeleteStudent(){
        Hint(2);
        String row = scanner.next();
        Delete del = new Delete(row.getBytes());
        try {
            table.delete(del);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * 修改方法,根据RowKey
     */
    private void  UpDataStudent(){
        Hint(2);
        String row = scanner.next();
        Result result = null;
        try {
            result = table.get(new Get(Bytes.toBytes(String.valueOf(row))));
        } catch (IOException e) {
            e.printStackTrace();
        }
        assert result != null;
        if (result.isEmpty()){
            Student student = CreateStudent();
            Put put = new Put(Bytes.toBytes(row));
            put.addColumn(Bytes.toBytes(col[0]),Bytes.toBytes("id"),Bytes.toBytes(row));
            put.addColumn(Bytes.toBytes(col[0]),Bytes.toBytes("name"),Bytes.toBytes(student.getStu_name()));
            put.addColumn(Bytes.toBytes(col[0]),Bytes.toBytes("sex"),Bytes.toBytes(student.getSex()));
            put.addColumn(Bytes.toBytes(col[1]),Bytes.toBytes("source"),Bytes.toBytes(student.getScource()));
            put.addColumn(Bytes.toBytes(col[1]),Bytes.toBytes("class_name"),Bytes.toBytes(student.getClass_name()));
            try {
                table.put(put);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }else {
            System.out.println("你输入的id不存在");
        }


    }

    /**
     * 输出提示
     * @param id 判断是哪里来的
     */
    private static void Hint(int id){
        switch (id){
            case 1:
                //循环提示
                System.out.println("*******************************************");
                System.out.println("-------------1.添加方法----------------------");
                System.out.println("-------------2.查询-------------------------");
                System.out.println("-------------3.条件查询----------------------");
                System.out.println("-------------4.删除-------------------------");
                System.out.println("-------------5.修改-------------------------");
                System.out.println("-------------6.退出-------------------------");
                System.out.println("*******************************************");
                break;
            case 2:
                //修改删除提示
                System.out.println("请输入id:");
                break;
            case 3:
                //条件查询提示
                System.out.println("************条件查询二级菜单*********************");
                System.out.println("-------------1.根据名字查询----------------------");
                System.out.println("-------------2.根据名字和班级查询-------------------------");
                System.out.println("-------------3.及格查询----------------------");
                System.out.println("-------------4.退出到上一级----------------------");

                System.out.println("*******************************************");
                break;
            default:
                throw new IllegalStateException("Unexpected value: " + id);
        }



    }

    public static void main(String[] args) throws IOException {
        studentMange studentMange = new studentMange();
//        获取用户组对象
        Admin admin = conn.getAdmin();
//        获取表操作对象
        tableName= TableName.valueOf("my_db:student");
//        获取控制台输入
        scanner = new Scanner(System.in);
//        获取表对象
        table = conn.getTable(tableName);

//        判断表是否存在
        if (admin.tableExists(tableName)){
            while (studentMange.quit){
                //输出提示
                Hint(1);
                //用户输入
                String sw =  scanner.next();
                switch (sw){
                    case "1":
                        //添加
                        studentMange.AddStudent(studentMange.CreateStudent());
                        break;
                    case "2":
                        //查询全部
                        studentMange.InquireAllPage();
                        break;
                    case "3":
                        studentMange.Conditional();
                        //条件查询
                        break;
                    case "4":
                        //删除
                        studentMange.DeleteStudent();
                        break;
                    case "5":
                        //修改
                        studentMange.UpDataStudent();
                        break;
                    case "6":
                        //退出
                        studentMange.quit = false;
                        admin.close();
                        table.close();
                        conn.close();
                        break;
                    default:
                        System.out.println("你输入的不正确");
                        break;
                }
            }
        }else {
            System.out.println("表不存在");
        }

    }
}
