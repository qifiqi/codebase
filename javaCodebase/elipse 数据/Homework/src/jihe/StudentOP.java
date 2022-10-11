package jihe;

import java.util.ArrayList;
import java.util.Iterator;

public class StudentOP {
     	static ArrayList arrayList= new ArrayList();
     	public static void showinfo() {
     		for(int i=0;i<arrayList.size();i++) {
     			System.out.println("第"+(i+1)+"个同学是"+arrayList.get(i));
     		}
		Iterator<String> iterator=arrayList.iterator();
		while (iterator.hasNext()) {
			System.out.println("---"+iterator.next());
		}
	}
}
