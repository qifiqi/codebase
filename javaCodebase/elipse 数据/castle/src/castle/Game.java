package castle;

import java.util.Scanner;

public class Game {
    private Room currentRoom;
        
    public Game() 
    {
        createRooms();
    }

    private void createRooms()
    {
        Room outside, lobby, pub, study, bedroom;
      
        //	���췿��
        outside = new Room("�Ǳ���");
        lobby = new Room("����");
        pub = new Room("С�ư�");
        study = new Room("�鷿");
        bedroom = new Room("����");
        
        //	��ʼ������ĳ���
        outside.setExits(null, lobby, study, pub);
        lobby.setExits(null, null, null, outside);
        pub.setExits(null, outside, null, null);
        study.setExits(outside, bedroom, null, null);
        bedroom.setExits(null, null, null, study);

        currentRoom = outside;  //	�ӳǱ����⿪ʼ
    }

    private void printWelcome() {
        System.out.println();
        System.out.println("��ӭ�����Ǳ���");
        System.out.println("����һ���������ĵ���Ϸ��");
        System.out.println("�����Ҫ������������ 'help' ��");
        System.out.println();
        System.out.println("��������" + currentRoom);
        System.out.print("�����У�");
        if(currentRoom.northExit != null)
            System.out.print("north ");
        if(currentRoom.eastExit != null)
            System.out.print("east ");
        if(currentRoom.southExit != null)
            System.out.print("south ");
        if(currentRoom.westExit != null)
            System.out.print("west ");
        System.out.println();
    }

    // ����Ϊ�û�����

    private void printHelp() 
    {
        System.out.print("��·������������������У�go bye help");
        System.out.println("�磺\tgo east");
    }

    private void goRoom(String direction) 
    {
        Room nextRoom = null;
        if(direction.equals("north")) {
            nextRoom = currentRoom.northExit;
        }
        if(direction.equals("east")) {
            nextRoom = currentRoom.eastExit;
        }
        if(direction.equals("south")) {
            nextRoom = currentRoom.southExit;
        }
        if(direction.equals("west")) {
            nextRoom = currentRoom.westExit;
        }

        if (nextRoom == null) {
            System.out.println("����û���ţ�");
        }
        else {
            currentRoom = nextRoom;
            System.out.println("����" + currentRoom);
            System.out.print("������: ");
            if(currentRoom.northExit != null)
                System.out.print("north ");
            if(currentRoom.eastExit != null)
                System.out.print("east ");
            if(currentRoom.southExit != null)
                System.out.print("south ");
            if(currentRoom.westExit != null)
                System.out.print("west ");
            System.out.println();
        }
    }
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		Game game = new Game();
		game.printWelcome();

        while ( true ) {
        		String line = in.nextLine();
        		String[] words = line.split(" ");
        		if ( words[0].equals("help") ) {
        			game.printHelp();
        		} else if (words[0].equals("go") ) {
        			game.goRoom(words[1]);
        		} else if ( words[0].equals("bye") ) {
        			break;
        		}
        }
        
        System.out.println("��л���Ĺ��١��ټ���");
        in.close();
	}

}
