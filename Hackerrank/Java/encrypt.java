import java.util.*;
class encrypt
{
public static void main(String gh[])
	{
	int k=0,a=0,b=0;
	Scanner sc=new Scanner(System.in);
	String s1=sc.nextLine();
	String s2=s1.replaceAll(" ","");
	String arr[][]=new String[100][100];
	String arr1[][]=new String[100][100];
	int len=s2.length();
	double a1=Math.sqrt(len);
	if(len<=8)
	{
	 a=(int)a1+1;
	 b=(int)a1+1;
	}
	else
	{
	 a=((int)a1);
	b=((int)a1+1);
	}
	
	for(int i=0;i<a;i++)
		{
		for(int j=0;j<b;j++)
			{
			arr[i][j]=""+s2.charAt(k);
			k++;
			if(k>=len)
			break;
			}
		}
	k=0;
		for(int i=0;i<b;i++)
			{
			for(int j=0;j<a;j++)
				{
				if(arr[j][i]==null)
				continue;
				System.out.print(arr[j][i]);
				/*if(k>=len)
				break;
				k++;*/
				}
			System.out.print(" ");	
			}
			
	}
}