import java.util.*;
class Solution
{
public static void main(String gh[])
	{
	Scanner sc=new Scanner(System.in);
	int n=sc.nextInt();
	long arr[]=new long[n+1];
	for(int i=0;i<n;i++)
		{
		arr[i]=sc.nextLong();
		}
	for(int i=0;i<n;i++)
			{
			long x=arr[i]/2;
			long y=arr[i]-x;
			System.out.println(x*y);
			}
	}
}