package oone4;

public class Test {
	
	public static void main(String[] arge) {
		pingpangcoach pingpangcoach=new pingpangcoach("马明",26);
		pingpangplayer pingpangplayer=new pingpangplayer("刘国",41);
		basketballplayer basketballplayer=new basketballplayer("姚梁",28);
		basketballcoach basketballcoach=new basketballcoach("杰克",42);
		pingpangplayer.show();
		pingpangplayer.eat();
		System.out.println("-----------------------------------");
		basketballplayer.show();
		basketballplayer.eat();
		System.out.println("-----------------------------------");
		pingpangcoach.show();
		pingpangcoach.eat();
		System.out.println("-----------------------------------");
		basketballcoach.show();
		basketballcoach.eat();
	}
}
