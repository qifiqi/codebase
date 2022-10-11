package 专业基本技能模块.程序设计;


public class J1_2 {
//《智能统计系统》关键算法


    /**
     * 实现统计纸片对折关键算法
     */
    public static void Dome1() {
        double zi = 0.5;
        int num = 0;
        while (zi < 8844430) {
            zi += zi;  //折叠一次就是加他之前的本身
            num++;
        }
        System.out.println("折叠:" + num + "次");
    }

    /**
     * 判断num的平方是不是以num结尾
     */
    public static boolean endW(int num){
        return String.valueOf(num*num).endsWith(num+"");
    }



    /**
     *实现统计同构数关键算法
     */
    public static void Dome2() {
        for (int i = 2; i <= 100; i++) {
            if (endW(i)){
                System.out.println(i);
            }
        }
    }


    public static void main(String[] args) {
        Dome1();
        Dome2();
    }
}
