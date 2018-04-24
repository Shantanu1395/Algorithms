import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class grid
{
	public static void main(String[] args) {
		int i=0,j=0,count=0,k=0;
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int a[]=new int[5000];
		int b[]=new int[5000];
		int x[]=new int[5000];
		int y[]=new int[5100];
		int xmen[]=new int[5100];

		String str[][]=new String[5100][5100];
		String str1[][]=new String[5100][5100];

		for (i=0;i<n ;i++ ) {
		a[i]=sc.nextInt();
		b[i]=sc.nextInt();	

		for (j=0;j<a[i] ;j++ ) 
			str[i][j]=sc.next();

		//Scanner sc1=new Scanner(System.in);
			x[i]=sc.nextInt();
			y[i]=sc.nextInt();

		for (j=0;j<x[i] ;j++ ) 
			str1[i][j]=sc.next();

		for(j=0;j<x[i];j++)
			{
				Pattern pattern=Pattern.compile(str1[i][j]);
				for (k=0;k<a[i] ;k++ ) {
					Matcher matcher=pattern.matcher(str[i][k]);
					if (matcher.find()) {
						count++;
					}
				}
			}

			if (count==x[i]) 
				xmen[i]=1;
			else
				xmen[i]=0;

			count=0;

		}

		for (i=0;i<n ;i++ ) {
			if(xmen[i]==1)
			System.out.println("yes");
			else if(xmen[i]==0)
			System.out.println("no");	
		}
		
	}
}