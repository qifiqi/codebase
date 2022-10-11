package 专业基本技能模块.程序设计;

import java.util.Random;
import java.util.Scanner;

public class J1_1 {

    /**
     * 任务一：实现平均成绩计算功能
     */
    public static void Dome1() {
        int[][] A = new int[30][5];
        int[] B = new int[30];
//        Scanner scanner = new Scanner(System.in);

//        设置每个地方的值
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[i].length; j++) {
                Random ran = new Random();
//                int num = scanner.nextInt();
                int num = ran.nextInt(100);
                A[i][j] = new Integer(num);
            }
        }

//        求平均值
        for (int i = 0; i < A.length; i++) {
            int sum = 0;
            for (int j = 0; j < A[i].length; j++) {
                sum += A[i][j];
            }
            B[i] = new Integer(sum / 5);
        }

//        输出平均地址
        for (int i = 0; i < B.length; i++) {
            System.out.println("第" + (i+1) + "个人的平均数:" + B[i]);

        }
    }


    /**
     * 任务二：实现前项列和计算功能关键算法
     */
    public static void Dome2() {
//        c1=a1/b1
        float s = 0;
        int a1 = 2,b1 = 1,d;
        for (int i = 1; i <= 20; i++) {
            s += (float) a1 / b1;
            d = a1;
            a1 = a1 + b1;
            b1 = d;

            System.out.println("第" + i + "次和:" + s);
        }

    }


    public static void main(String[] args) {
        System.out.println("********************************");
        Dome1();
        System.out.println("********************************");
        Dome2();
        System.out.println("********************************");
    }
}
