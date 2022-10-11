package homework;
import java.util.Scanner;

/**
 * 任务三：实现数一数游戏关键算法并绘制流程图（30 分）
分别输入两个字符串 s1 和 s2 ，请问 s1 中包含多少个 s2，如果没有则输出 0。
要求：使用循环。
 * @author key
 *
 */
public class six {
	/**
	 * 分别输入两个字符串 s1 和 s2 ，请问 s1 中包含多少个 s2，如果没有则输出 0。
	 * @param s1 字符串
	 * @param S2 字符串包含的数
	 * @return 包含的个数
	 */
	public static int RepeNum(String s1,String s2){
		int index =0;//索引的位置开始找起
		int length = s2.length();//字符串的长度
		int count =0;//包含的个数
		//索引长度不超过字符串的长度
		while(index < s1.length()){
			//判断 索引字符串从index下标位置开始有s2字符 
			if(s1.indexOf(s2,index) != -1){
				//索引下标等于 索引到s2字符的位置加上s2字符的长度
				index = s1.indexOf(s2,index)+length;
				//包含的个数加1
				count ++;
			}else{
				break;
			}
		}
		return count;
	}
	@SuppressWarnings("unused")
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.println("输入第一个字符串:");
		String s1 = in.next();
		System.out.println("输入第二个字符串:");
		String s2 = in.next();
		System.out.println(RepeNum(s1,s2));
	}

}

