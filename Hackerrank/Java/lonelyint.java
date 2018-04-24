import java.util.*;
class Solutiontemp1
{
public static void main(String gh[])
	{
	int i=0,j=0;
	int arr[]=new int[1000];
	int count[]=new int[1000];
	Scanner sc=new Scanner(System.in);
	int t=sc.nextInt();
				for(i=0;i<t;i++)
			    arr[i]=sc.nextInt();	
				for(i=0;i<t;i++)
					{
						for(j=0;j<t;j++)
							{
							if(arr[i]==arr[j])
							count[i]++;
							}
					}
					
					for(i=0;i<t;i++)
					{
					if(count[i]==1)
					System.out.println(arr[i]);
					}
	}				
					
}	
