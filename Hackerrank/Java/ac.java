import java.util.*;
class myclass
{
public static void main(String args[])
	{
	int i=0,j=0;
	String s[]=new String[1000];
	Scanner sc=new Scanner(System.in);
	int n=sc.nextInt();
	for(i=0;i<n;i++)
		s[i]=sc.next();
		
	 for(i=0;i<n;i++)
		{
		int count=0;
		for(j=0;j<s[i].length()-1;j++)
		    {
		if(s[i].charAt(j)==s[i].charAt(j+1))
		{
				
					s[i].replace(s[i].charAt(j+1),'*');
					//System.out.println(s[i]);
					count++;	
		}	
            }		
			System.out.println(count);
		}
	}
}