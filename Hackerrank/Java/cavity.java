import java.util.*;
class Solutiontemp1
{
public static void main(String gh[])
	{
	int i=0,j=0;
	Scanner sc=new Scanner(System.in);
	int t=sc.nextInt();
	String temp1[]=new String[1000];
	for(i=0;i<t;i++)
		temp1[i]=sc.next();
		
	for(i=0;i<t;i++)
			{
			for(j=0;j<t;j++)
				{
				if(!((i==(t-1) && j==(t-1)) ||(i==0 && j==0) || (i==0 && j!=0) || (j==0 && i!=0) || (i==(t-1) && j!=(t-1)) || (i!=(t-1) && j==(t-1))))
					{
					if((temp1[i].charAt(j)>temp1[i-1].charAt(j)) && (temp1[i].charAt(j)>temp1[i].charAt(j-1)) &&  (temp1[i].charAt(j)>temp1[i+1].charAt(j)) && (temp1[i].charAt(j)>temp1[i].charAt(j+1)) )
					temp1[i]=temp1[i].replace(temp1[i].charAt(j),'X');
				    }
				}	
			}	
			
	for(i=0;i<t;i++)
				System.out.println(temp1[i]);
	}
}	
