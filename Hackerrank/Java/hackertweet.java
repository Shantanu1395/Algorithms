import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
 
class hacker
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int count=0;
		String arr[]=new String[1000];
		int i=0;
		for (i=0;i<n+1 ;i++ ) {
			arr[i]=sc.nextLine();
			Pattern p=Pattern.compile("hackerrank");
			Matcher m=p.matcher(arr[i].toLowerCase());
			if (m.find()) 
				count++;
			else
				System.out.println("No");
		}
		System.out.println(count-1);
	}
}