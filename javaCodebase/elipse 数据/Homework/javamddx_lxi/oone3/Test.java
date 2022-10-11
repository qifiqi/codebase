package oone3;
public class Test {
	public static void main(String[] args) {
		Point point1= new Point();
		point1.setX(3.0);
		point1.setY(4.0);
		Point point= new Point(point1.getX(),point1.getY());
		point.show();
		System.out.println("-------------------------------------------------------------------");
		Circle circle1=new Circle(point1.getX(),point1.getY());
		circle1.setRadius(7.0);
		Circle circle=new Circle(point1.getX(),point1.getY(),circle1.getRadius());
		circle.show();
		System.out.println("-------------------------------------------------------------------");
		Cylinder cylinder1=new Cylinder(point1.getX(),point1.getY());
		cylinder1.setHeight(9.0);
		cylinder1.setRadius(7.0);
		Cylinder cylinder=new Cylinder(point1.getX(),point1.getY(),cylinder1.getRadius(),cylinder1.getHeight());
		cylinder.show();

	}

}
