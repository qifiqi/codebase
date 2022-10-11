package oone3;

public class Cylinder extends Circle {
	//圆柱体
	double height;//高度
	public Cylinder(double x, double y) {
		super(x, y);
	}
	public Cylinder(double x, double y, double radius,double height) {
		super(x, y, radius);
		this.height=height;
	}
	public double getHeight() {
		return height;
	}

	public void setHeight(double height) {
		this.height = height;
	}

	public double area() {
		double aa=3.1415926;
    	double a=2*(radius*radius*aa)+(aa*2*radius*height);
		return a;
	}
	public double volume() {
		double aa=3.1415926;
    	double a=(radius*radius*aa)*height;
		return a;
	}
	 public void show() {
			System.out.println("圆柱体的属性是:"+"("+getX()+","+getY()+","+radius+","+height+")");
	    	System.out.println("圆柱体的面积是："+area());
	    	System.out.println("圆柱体的面积是："+volume());

	    }
}
