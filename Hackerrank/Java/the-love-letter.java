import java.util.*;
class Solution23
{
static int u=0;
public static void main(String gh[])
	{
	int i=0,j=0;
	long count[]=new long[1000];
	Scanner sc=new Scanner(System.in);
	int t=sc.nextInt();
	String arr[]=new String[1000];
	
		for(i=0;i<t;i++)
		arr[i]=sc.next();
			
	for(i=0;i<t;i++)
		{
		u=0;
		for(j=0;j<arr[i].length()/2;j++)
			{
			if((int)arr[i].charAt(j)>(int)(arr[i].charAt(arr[i].length()-1-j)))
				{
				int x=(int)arr[i].charAt(j);
				int y=(int)arr[i].charAt(arr[i].length()-1-j);
				while(x!=y)
					{
					arr[i]=arr[i].replace(arr[i].charAt(j),(char)((int)arr[i].charAt(j)));
					u++;
					x--;
					}
				}
			if((int)arr[i].charAt(j)<(int)arr[i].charAt(arr[i].length()-1-j))
				{
				int x=(int)arr[i].charAt(j);
				int y=(int)arr[i].charAt(arr[i].length()-1-j);
					while(y!=x)
					{
					arr[i]=arr[i].replace(arr[i].charAt(arr[i].length()-1),(char)((int)(arr[i].charAt(arr[i].length()-1))));
					u++;
					y--;
					}
				}
			}
		count[i]=u;	
		}
		
	for(i=0;i<t;i++)
		System.out.println(count[i]);
		
	}
	
}	