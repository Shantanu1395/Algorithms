import java.util.*;
class Solution1
{
public static void main(String gh[])
	{
	int count[]=new int[2000];
	int a1[]=new int[2000];
	int a2[]=new int[2000];
	int a3[]=new int[2000];
	Scanner sc=new Scanner(System.in);
	int t=sc.nextInt();
	int i=0,j=0;
	for( i=0;i<t;i++)
		{
		a1[i]=sc.nextInt();
		a2[i]=sc.nextInt();
			for(j=0;j<a1[i];j++)
				{
				a3[j]=sc.nextInt();
				if(a3[j]<=0)
			    count[i]++;
				}
		}
	
	for( i=0;i<t;i++)
		{
		if(count[i]>=a2[i])
		System.out.println("NO");
		else
		System.out.println("YES");
	    }
	}
}