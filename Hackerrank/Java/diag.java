import java.util.*;
class diag
{
public static void main(String gh[])
	{
	int count1=0,count2=0;
	Scanner sc=new Scanner(System.in);
	int arr[][]=new int[100][100];
	int n=sc.nextInt();
	int i=0,j=0;
	for(i=0;i<n;i++)
		{
		for(j=0;j<n;j++)
			{
			arr[i][j]=sc.nextInt();
			if(i==j)
			count1+=arr[i][j];
			}
			count2+=arr[i][n-i-1];
		}
		System.out.println(Math.abs(count1-count2));
	}
}