package oone3;

public class Point {
	//��
	private double x;
	private double y;
	public double getX() {
		return x;
	}
	public void setX(double x) {
		this.x = x;
	}
	public double getY() {
		return y;
	}
	public void setY(double y) {
		this.y = y;
	}
	public Point(double x, double y) {
		this.x = x;
		this.y = y;
	}
	public void show() {
		System.out.println("���������:"+"("+x+","+y+")");
	}
	public Point() {
	}
	
	
}
