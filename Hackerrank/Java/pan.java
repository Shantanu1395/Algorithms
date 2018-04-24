import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

class pan
{
	public static void main(String[] args) {
			Scanner sc=new Scanner(System.in);
			int i=0,j=0;
			boolean flag=false;
			String s[]=new String[1000];
			int count[][]=new int[100][100];
			int n=sc.nextInt();
			for (i=0;i<n;i++) {
				s[i]=sc.next();
			}

			for (i=0;i<n ;i++ ) {
				for(j=0;j<10;j++)
				{
				if ((s[i].charAt(j)+"").matches("[A-Z]+")) 
					count[i][j]=1;
				else if((s[i].charAt(j)+"").matches("[0-9]+"))	
					count[i][j]=2;
				else
					count[i][j]=0;
				
			    }
			}

			for (i=0;i<n ;i++ ) {
				loop:
				{

				for (j=0;j<5 ;j++ ) {
					if(count[i][j]==1)
						flag=true;
					else if(count[i][j]==0 || count[i][j]==2)
					{
						flag=false;
						break loop;
					}
				}
				for (j=5;j<9 ;j++ ) {
					if(count[i][j]==2)
						flag=true;
					else if(count[i][j]==0)
					{
						flag=false;	
						break loop;
					}
				}
				if(count[i][9]==1)
					flag=true;
				else if(count[i][j]==0)
				{
					flag=false;
					break loop;
				}

				}

				if(flag==true)
				System.out.println("Yes");

				else
				System.out.println("No");								
				
				}	
		}	
}