import java.util.*;
class and{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		long n=sc.nextLong();
		long i=0;
		long x=0;
		long arr[]=new long[1000];
		for(i=0;i<n;i++)
		{
			long a=sc.nextLong();
			long b=sc.nextLong();
			x=a;
			for(long j=a;j<b;j++){
				x=x & (j+1);
				//System.out.println(j+"&"+(j+1)+"="+x);
			}
		arr[(int)i]=x;	
		}

		for (i=0;i<n ;i++ ) 
			System.out.println(arr[(int)i]);
		
	}
}