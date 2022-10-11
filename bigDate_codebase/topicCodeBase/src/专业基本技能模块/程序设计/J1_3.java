package 专业基本技能模块.程序设计;

import java.util.Arrays;
import java.util.Scanner;

public class J1_3 {
    
    /**
     *实现抓娃娃游戏功能关键算法
     */
    public static void Dome1(){
        int[] a = new int[10];
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 10; i++) {
            System.out.println("输入第"+(i+1)+"个娃娃的数字");
            a[i] = scanner.nextInt();
        }
        System.out.println("最大的值是:"+Arrays.stream(a).max().getAsInt());
    }
    
    
    /**
     *实现算数游戏功能关键算法
     */
    public static void Dome2(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("输入数字");
        int num = scanner.nextInt();
        int x = 1;
        while (num>0){
            x *= num%10;
            num = num/10;
        }
        System.out.println(x);
    }
    
    
    
    /**
     * 《儿童网络游戏游戏》
     * @param args
     */
    public static void main(String[] args) {
//        Dome1();
        Dome2();
    }
}
