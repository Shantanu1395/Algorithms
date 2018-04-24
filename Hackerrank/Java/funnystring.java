import java.util.*;
class myclass
{
public static void main(String args[])
	{
	int i=0,j=0;
	StringBuffer temp[]=new StringBuffer[1000];
	StringBuffer s[]=new StringBuffer[1000];
	StringBuffer r[]=new StringBuffer[1000];
	Scanner sc=new Scanner(System.in);
	int n=sc.nextInt();
	for(i=0;i<n;i++)
		{
		s[i] = new StringBuffer();
		s[i].append(sc.next());
		temp[i] = new StringBuffer();
		temp[i].append(s[i]);
		}
	for(i=0;i<n;i++)
	  {
		r[i] = new StringBuffer();
		r[i].append(s[i].reverse());
	  }
	  
	  for(i=0;i<n;i++)
	  {
	  int x=0;
	  for(j=1;j<s[i].length();j++)
		{
		if(Math.abs((int)temp[i].charAt(j)-(int)temp[i].charAt(j-1))==Math.abs((int)r[i].charAt(j)-(int)r[i].charAt(j-1)))
			{
			x++;
			}
		}
		if(x==temp[i].length()-1)
		System.out.println("Funny");
		else
		System.out.println("Not Funny");
	  }
	  
	}
}