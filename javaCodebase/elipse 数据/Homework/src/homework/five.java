package homework;
public class five{
	
	public static void main(String[] args){
		int x[]={1,9,3,7,4,2,5,0,6,8};//����һ������
		//��ѭ��,��Ҫѭ���Ĵ���
		for(int i=0; i<x.length-1;i++){
			//��ѭ��,ÿ��ѭ������ȷ��һ���������������������
			for(int j=0;j<x.length-1-i;j++){
				if(x[j]>x[j+1]){//�ж���������Ԫ�صĴ�С
					int t=x[j];//����һ������t,�ѵ�һ������t
					x[j]=x[j+1];//�ѵڶ���λ�õ�ֵ������һ��
					x[j+1]=t;//��t(Ҳ���ǵ�һ����ֵ�����ڶ���),��������Ԫ�ؾͽ�����λ��
					//����ѭ����֮��,�����Ǹ����ͳ���������������
				}
				
			}
		}
		for(int a=0;a<x.length;a++){
		System.out.print(x[a]+" ");
		}
	}
}
