package oone3;

public class Circle extends Point {
	//圆
	double radius;//半径
	public double getRadius() {
		return radius;
	}
	public void setRadius(double radius) {
		this.radius = radius;
	}
	public Circle(double x, double y) {
		super(x, y);
	}
	public Circle(double x, double y,double radius){
		super(x, y);
		this.radius=radius;
	}
    public double area() {
    	double aa=3.1415926;
    	double a=(radius*radius)*aa;
		return a;
	}
    public void show() {
		System.out.println("圆的属性是:"+"("+getX()+","+getY()+","+radius+")");
    	System.out.println("圆的面积是："+area());
    }
}
