package oone4;

public class Test {
	
	public static void main(String[] arge) {
		pingpangcoach pingpangcoach=new pingpangcoach("����",26);
		pingpangplayer pingpangplayer=new pingpangplayer("����",41);
		basketballplayer basketballplayer=new basketballplayer("Ҧ��",28);
		basketballcoach basketballcoach=new basketballcoach("�ܿ�",42);
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
