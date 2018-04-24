import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

class two
{
	public static void main(String[] args) {
	
		int flag[]=new int[100];		
		int i=0,j=0,k=0;
		String s1=new String();
		String s2=new String();

		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		for(k=0;k<n;k++)
		{
		//Scanner sc=new Scanner(System.in);	
		s1=sc.next();
		s2=sc.next();
		for (i=0;i<s1.length();i++) {
			for (j=i;j<s1.length();j++) {
				Pattern pattern=Pattern.compile(s1.substring(i,s1.length()));
				Matcher matcher=pattern.matcher(s2);
				if (matcher.find()) 
					flag[k]=1;
				
				else
					flag[k]=0;
			}
		}

		
		}

		for (i=0;i<n;i++)
		if (flag[i]==1) 
			System.out.println("YES");

		else
			System.out.println("NO");				
	}
}