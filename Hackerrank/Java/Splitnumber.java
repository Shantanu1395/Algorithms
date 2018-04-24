import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class split
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String arr[]=new String[100];
		String temp[][]=new String[100][100];
		int n=sc.nextInt();
		int i=0;
		for (i=0;i<n+1;i++ ) {
			arr[i]=sc.nextLine();
			String temp1[]=arr[i].split("-");
			String temp2[]=arr[i].split(" ");
			Pattern p=Pattern.compile("-");
			Matcher m=p.matcher(arr[i]);
			if (m.find()) 
			{
				for (int j=0;j<temp1.length ;j++ ) {
					temp[i][j]=(temp1[j]);
				}
			}
			else
			{
			for (int j=0;j<temp2.length ;j++ ) {
					temp[i][j]=(temp2[j]);
				}	
			}
		}

		for (i=1;i<n+1 ;i++ ) 
				System.out.println("CountryCode="+temp[i][0]+",LocalAreaCode="+temp[i][1]+",Number="+temp[i][2]);
	}
}