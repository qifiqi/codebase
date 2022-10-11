package lxi;

import java.util.Scanner;

public class chaogeao {
	public boolean isLongPressedName(String name, String typed) {
		int a = 0, aa = 0;
		while (aa <typed.length()) {
			if ((a < name.length()) && (name.charAt(a) == typed.charAt(aa))) {
				a++;
				aa++;
			} else if (aa > 0 && (typed.charAt(aa) == typed.charAt(aa - 1))) {
				aa++;
			} else {
				return false;
			}
		}
		return a == name.length();
	}

	public static void main(String[] aeg) {
		chaogeao chaogeao = new chaogeao();
		Scanner scanner = new Scanner(System.in);
		String name = scanner.next();
		String typed = scanner.next();
		boolean ss=chaogeao.isLongPressedName(name, typed);
		System.out.println(ss);

	}

}
