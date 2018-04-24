import java.util.*;
class fs
{
public static void main(String args[])
	{
	int i=0;
	int temp[]=new int[1000];
	Scanner sc=new Scanner(System.in);
	String s=new String();
	s=sc.nextLine();
	
		for(i=0;i<s.length();i++)
		  {
		   for(char x='a';x<='z';x++)
		    {
			    if(Character.toLowerCase(s.charAt(i))==x)
				temp[(int)x]++;
			}
		  }	
	
	   /* for(int i=0;i<s.length();i++)
		  {
		   for(char x='A';x<='Z';x++)
		    {
			System.out.println((int)x);
			    if(s.charAt(i)==x)
				temp[(int)x]++;
			}
		  }
		*/  
		  int d=0;
		for(i=97;i<=122;i++)
				{
					if(temp[i]>=1)
					d++;
				}
		if(d==26)
			System.out.println("pangram");
		else
		    System.out.println("not pangram");
	}
}