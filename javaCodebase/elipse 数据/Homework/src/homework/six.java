package homework;
import java.util.Scanner;

/**
 * ��������ʵ����һ����Ϸ�ؼ��㷨����������ͼ��30 �֣�
�ֱ����������ַ��� s1 �� s2 ������ s1 �а������ٸ� s2�����û������� 0��
Ҫ��ʹ��ѭ����
 * @author key
 *
 */
public class six {
	/**
	 * �ֱ����������ַ��� s1 �� s2 ������ s1 �а������ٸ� s2�����û������� 0��
	 * @param s1 �ַ���
	 * @param S2 �ַ�����������
	 * @return �����ĸ���
	 */
	public static int RepeNum(String s1,String s2){
		int index =0;//������λ�ÿ�ʼ����
		int length = s2.length();//�ַ����ĳ���
		int count =0;//�����ĸ���
		//�������Ȳ������ַ����ĳ���
		while(index < s1.length()){
			//�ж� �����ַ�����index�±�λ�ÿ�ʼ��s2�ַ� 
			if(s1.indexOf(s2,index) != -1){
				//�����±���� ������s2�ַ���λ�ü���s2�ַ��ĳ���
				index = s1.indexOf(s2,index)+length;
				//�����ĸ�����1
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
		System.out.println("�����һ���ַ���:");
		String s1 = in.next();
		System.out.println("����ڶ����ַ���:");
		String s2 = in.next();
		System.out.println(RepeNum(s1,s2));
	}

}

