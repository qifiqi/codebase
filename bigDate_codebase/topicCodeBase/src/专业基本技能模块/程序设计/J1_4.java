package 专业基本技能模块.程序设计;

import java.util.Arrays;
import java.util.Scanner;

/**
 * 《英语辅导系统》关键算法
 */
public class J1_4 {

    /**
     * 实现连号判断功能关键算法
     */
    public static void Dome1() {
        String[] A = {"asdf", "fda", "111", "aaaa", "acccc"};
        String[] B = {"aaaa", "bbbb", "vvvv", "ccccc", "ddddd"};
        if (A.length > B.length) {
            String[] C = new String[A.length];
            for (int i = 0; i < A.length; i++) {
                C[i] = String.join("=", A[i], B[i]);
            }
            for (String c : C) {
                System.out.println(c);

            }

        } else {
            String[] C = new String[B.length];
            for (int i = 0; i < B.length; i++) {
                C[i] = String.join("=", A[i], B[i]);
            }
            for (String c : C) {
                System.out.println(c.toString());

            }
        }

    }

    /**
     * 现趣味英语试题 2 关键算法并绘制流程图（30 分）。
     * 判断一个字符串是否是对称字符串，例如：“abc”不是对称字符串，“aba”、“abba”、“aaa”、“mnanm”是对称字符串。是的话输出“Yes”，否则输出“No”。
     */
    public static boolean Dome2(String str) {
        int num = str.length();
        int num_2 = 0;

        for (int i = 0; i < num/2; i++) {
            if (String.valueOf(str.charAt(i)).equals(String.valueOf(str.charAt((num - 1-i))))) {
                num_2++;
            }
        }
        if (num_2>=num/2){
            return true;
        }
        return false;
    }


    public static void main(String[] args) {
//        Dome1();
        System.out.println(Dome2("asdffdsa"));
    }
}
