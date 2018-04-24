import java.util.*;

class serv
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		int number1 = input.nextInt();
		int number2 = input.nextInt();
		ArrayList<Integer> arr=new ArrayList<Integer>();
		int temp[]=new int[1000];
		long i=0;
		for(i=0;i<number1;i++)
		{
			int ax=input.nextInt();
			arr.add(ax);
		}	
			
		for(int i1=0;i1<number2;i1++){
			int a=input.nextInt();				
			int b=input.nextInt();
			int x=arr.get(a);
				
			for(long j=a;j<b;j++){
			x=Math.min(x,arr.get((int)j+1));
			temp[i1]=x;
			}}
			
			for(i=0;i<number2;i++)
			System.out.println(temp[(int)i]);
	}
}
