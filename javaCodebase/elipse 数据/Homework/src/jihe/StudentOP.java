package jihe;

import java.util.ArrayList;
import java.util.Iterator;

public class StudentOP {
     	static ArrayList arrayList= new ArrayList();
     	public static void showinfo() {
     		for(int i=0;i<arrayList.size();i++) {
     			System.out.println("��"+(i+1)+"��ͬѧ��"+arrayList.get(i));
     		}
		Iterator<String> iterator=arrayList.iterator();
		while (iterator.hasNext()) {
			System.out.println("---"+iterator.next());
		}
	}
}
