import java.util.*;
class Solutiontemp1
{

public static void main(String gh[])
	{
	Scanner sc=new Scanner(System.in);
	int t=sc.nextInt();
	int i=0,j=0,c=0;
	long rem=0;
	long arr[]=new long[100];
	long temp1[]=new long[100];
	long x[]=new long[1000];
	long count[]=new long[1000];
	long temp[][]=new long[1000][1000];
		for(i=0;i<t;i++)
		{
		arr[i]=sc.nextLong();
		temp1[i]=arr[i];
		}
		
		for(i=0;i<t;i++)
		{
		j=0;
		while(arr[i]!=0)
			{
			rem=arr[i]%10;
			arr[i]=arr[i]/10;
			temp[i][j]=rem;
			j++;
			}
			x[i]=j;
		}
		
		for(i=0;i<t;i++)
		{
			{
				c=0;
					{
					for(int k=0;k<x[i];k++)
						{	
						if(temp[i][k]!=0)
							{
					        if(temp1[i]%temp[i][k]==0)
				            c++;
							}	
						}
					}
			}
			    count[i]=c;	
		}
		for(i=0;i<t;i++)
		System.out.println(count[i]);
		
	}
}	

