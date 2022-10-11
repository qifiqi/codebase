package com.lz.java;

public class Student {
    private int sid;
    private String stu_name;
    private String sex;
    private String scource;
    private String class_name;

    public Student(int sid, String stu_name, String sex, String scource, String class_name) {
        this.sid = sid;
        this.stu_name = stu_name;
        this.sex = sex;
        this.scource = scource;
        this.class_name = class_name;
    }

    public Student(String stu_name, String sex, String scource, String class_name) {
        this.stu_name = stu_name;
        this.sex = sex;
        this.scource = scource;
        this.class_name = class_name;
    }

    public Student() {
    }

    public int getSid() {

        return sid;
    }

    public void setSid(int sid) {
        this.sid = sid;
    }

    public String getStu_name() {
        return stu_name;
    }

    public void setStu_name(String stu_name) {
        this.stu_name = stu_name;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getScource() {
        return scource;
    }

    public void setScource(String scource) {
        this.scource = scource;
    }

    public String getClass_name() {
        return class_name;
    }

    public void setClass_name(String class_name) {
        this.class_name = class_name;
    }

    @Override
    public String toString() {
        return "Student{" +
                "sid=" + sid +
                ", stu_name='" + stu_name + '\'' +
                ", sex='" + sex + '\'' +
                ", scource='" + scource + '\'' +
                ", class_name='" + class_name + '\'' +
                '}';
    }
}
