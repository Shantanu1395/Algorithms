import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
class song
{
public static void main(String gh[])
	{
	int k=0;
	Scanner sc=new Scanner(System.in);
	int count[]=new int[1000];
	String s1[]=new String[1000];
	String s4="31415926535897932384626433833";
	int n=sc.nextInt();
	for(k=0;k<n;k++)
	  {
	   sc=new Scanner(System.in);
	   s1[k]=sc.nextLine();
	   String s2[]=s1[k].split(" ");
	   String s3="";
	   for(int i=0;i<s2.length;i++)
	   s3=(s3+(s2[i].length())+"");
	   Pattern pattern = Pattern.compile(s3);
	   Matcher matcher = pattern.matcher(s4);
	   if (matcher.find())
		count[k]=1;
       else 
	   count[k]=0;
	   }
	   for(k=0;k<n;k++)
	      {
		  if (count[k]==1)
          System.out.println("It's a pi song.");
          else if(count[k]==0)  
          System.out.println("It's not a pi song.");
		  }
	}
}
