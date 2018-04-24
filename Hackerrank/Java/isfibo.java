import java.util.*;
class Solution
{
static long Fibo(long n) 
{
        long x = 0, y = 1, z = 1;
        for (long i = 0; i < n; i++) {
            x = y;
            y = z;
            z = x + y;
        }
        return x;
}
	public static void main(String gh[])
		{
		long i=0,j=0;
		long count[]=new long[1000];
		Scanner sc=new Scanner(System.in);
		long n=sc.nextInt();
		for(i=0;i<n;i++)
			{
			long x=sc.nextLong();
			for(j=0;j<1000;j++)
				{
				if(x==Fibo(j))
				count[(int)i]++;
				}
			}
		for(i=0;i<n;i++)
			{
			if(count[(int)i]>=1)
			System.out.println("IsFibo");
			else
			System.out.println("IsNotFibo");
			}
		}
}