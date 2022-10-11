package homework;
public class five{
	
	public static void main(String[] args){
		int x[]={1,9,3,7,4,2,5,0,6,8};//创建一个数组
		//外循环,需要循环的次数
		for(int i=0; i<x.length-1;i++){
			//内循环,每次循环都能确定一个最大的数字让他沉最底下
			for(int j=0;j<x.length-1-i;j++){
				if(x[j]>x[j+1]){//判断相邻两个元素的大小
					int t=x[j];//定义一个变量t,把第一个赋给t
					x[j]=x[j+1];//把第二个位置的值赋给第一个
					x[j+1]=t;//把t(也就是第一个的值赋给第二个),这样两个元素就交换了位置
					//这样循环完之后,最大的那个数就沉到了数组的最底下
				}
				
			}
		}
		for(int a=0;a<x.length;a++){
		System.out.print(x[a]+" ");
		}
	}
}
