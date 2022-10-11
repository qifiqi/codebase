package 专业基本技能模块.程序设计;

import java.util.Scanner;
import java.util.regex.Pattern;

/**
 * 手机号码查询系统》关键算法
 */
public class J1_5 {
    /**
     * 实现连号判断功能关键算法并绘制流程图（30 分）。
     * 从键盘接收一个十一位的数字，判断其是否为尾号 5 连的手机号。规则：第 1 位是 1，第二位可以是数字 358 其中之一，后面 4 位任意数字，最后 5 位为任意相同的数字。例如：18601088888、13912366666 则满足
     */
    public static boolean Dome1() {
        Scanner scanner = new Scanner(System.in);
        String phone = scanner.next();
        String zz = "^1{1}[358]{1}[0-9]{4}(\\d)\\1{4}";
        return Pattern.matches(zz, phone);
    }
    
    /**
     * 实现统计非数字功能关键算法
     */
    public static void Dome2() {

    }
    

    public static void main(String[] args) {
        Dome1();
    }
}
