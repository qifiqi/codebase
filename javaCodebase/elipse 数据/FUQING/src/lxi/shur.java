/*
 * ��������Ϸ
��дһ������ʵ������Ч��
��Ϸ�������£�
1.��̨Ԥ������һ��1-100֮�����������û�����¼�������
2.����¶��ˣ���ӡ����ϲ��������ˡ�
3.����´���
    �´��ˣ���ӡ��sorry�����´���!��
    ��С�ˣ���ӡ��sorry������С��!��
4.ֱ�����ֲµ�Ϊֹ
������
���ϵĿ����������֣����бȶԣ��²���ȷ���ܽ�����ѭ����
������100,����ʾҪ������ȷ�����֣�if��
��ȷ��������ϵͳ������ɣ�����ο����£�
import java.util.*;
/    /����Random����������
		Random ran = new Random();
		int ranNumber = ran.nextInt(100)+1;�����������1~100֮�������
����²����ֱ���ȷ���ִ󣬽�����ʾ�������޸���ʾ��䣨if��
����²�������ȷ����������Ϣ����Ϸ�������������

 */
package lxi;
import java.util.Random;
import java.util.Scanner;

public class shur {

	public static void main(String[] args) {
		int min, max;
		min = 1;
		max = 100;
		Random ran = new Random();
		int ranNumber = ran.nextInt(100) + 1;
		Scanner scanner = new Scanner(System.in);
		System.out.println("��������Ϸ");
		System.out.println("��ӭ��");

		for (int i = 1; i <= 10; i++) {
			System.out.printf("��������%d~%d�ĵ���ֵ\n", min, max);
			int shu = scanner.nextInt();
			if(i==7) {
				System.out.println("��������3�λ���");
				if(shu<100&&shu>0) {
					if (ranNumber == shu) {
						System.out.println("��ϲ���������");
						return;
					} else {
						if (ranNumber < shu) {
							System.out.println("sorry�����´���!");
							max = shu;
						} else {
							System.out.println("sorry������С��!");
							min = shu;
						}
					}
					}else {
						System.out.println("sorry,��������ȷ����");
					}
				
			}else {
				if(shu<100&&shu>0) {
					if (ranNumber == shu) {
						System.out.println("��ϲ���������");
						return;
					} else {
						if (ranNumber < shu) {
							System.out.println("sorry�����´���!");
							max = shu;
						} else {
							System.out.println("sorry������С��!");
							min = shu;
						}
					}
					}else {
						System.out.println("sorry,��������ȷ����");
					}
				
			}
		}
		}
}
