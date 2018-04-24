import java.util.*;
class Solutiontemp1
{
public static void main(String gh[])
	{
	int i=0,j=0,d=0,rem=0;
	Scanner sc=new Scanner(System.in);
	int t=sc.nextInt();
	int arr[]=new int[1000];
	int temp1[]=new int[1000];
	int temp2[][]=new int[1000][1000];
	int x[]=new int[1000];
	for(i=0;i<t;i++)
		arr[i]=sc.nextInt();
	
	for(i=0;i<t;i++)
	temp1[i]=arr[i];
	
	for(i=0;i<t;i++)
		{
		j=0;
		while(temp1[i]!=0)
			{
			rem=temp1[i]%10;
			temp1[i]=temp1[i]/10;
			temp2[i][j]=rem;
			j++;
			}
			x[i]=j;
		}
	
	for(i=0;i<t;i++)
			{
			for(j=0;j<x[i]/2;j++)
				{
					d=temp2[i][j];
					temp2[i][j]=temp2[i][x[i]-j-1];
					temp2[i][x[i]-j-1]=d;
				}
			}
		
	for(i=0;i<t;i++)
			{
			for(j=0;j<t;j++)
				{
				if(!((i==(t-1) && j==(t-1)) ||(i==0 && j==0) || (i==0 && j!=0) || (j==0 && i!=0) || (i==(t-1) && j!=(t-1)) || (i!=(t-1) && j==(t-1))))
					{
					if((temp2[i][j]>temp2[i-1][j]) && (temp2[i][j]>temp2[i][j-1]) &&  (temp2[i][j]>temp2[i+1][j]) && (temp2[i][j]>temp2[i][j+1]) )
					temp2[i][j]=(int)'X';
				    }
				}	
			}	
			
	for(i=0;i<t;i++)
			{
			for(j=0;j<t;j++)
				{
				System.out.print(temp2[i][j]);
				}
			System.out.println("");	
			}	
	}
}	
