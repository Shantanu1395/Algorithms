import java.util.*;
import java.io.*;
class gem
{
static int count=0;	
public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		int n=sc.nextInt();
		//int flag[]=new int[100];
		int i=0,j=0,z=0;
		String temp="";
		int arr[]=new int[1000];
		String s[]=new String[1000];
		
		for (i=0;i<n ;i++ ) 
			s[i]=sc.next();

		String str=null;

		/*i=0;
		while(i<s[0].length()-1)
		{
			if(s[0].charAt(i)!=s[0].charAt(i+1))
			{
				arr+=s[0].charAt(i);
				i++;
				j++;
			}
			else
				i++;
		}*/
		//arr+=s[0].charAt(s[0].length()-1);
		//for(int a=0;a<j;a++) 
		//System.out.print(arr.charAt(a));
		//System.out.println(arr);
		//System.out.println();	
		int c=0;
		for (i=0;i<s[0].length() ;i++ ) {
			
			arr[(int)s[0].charAt(i)]++;
		//	System.out.print(arr[(int)s[0].charAt(i)]+":"+s[0].charAt(i)+":"+(int)s[0].charAt(i)+" ");
			}
		//System.out.println();	
		//j=0;	
		for (i=97;i<=122 ;i++ ) {
			if(arr[i]>0)
			{
				temp+=(char)i;
				//j++;
		//		System.out.print((char)i+" ");
			}

		}
		//System.out.println();
		//System.out.println(temp+" "+temp.length());

		for (i=0;i<temp.length() ;i++ ) {
			count=0;
			for (j=1;j<n ;j++ ){ 
				loop:{
			
				if(s[j].indexOf(temp.charAt(i))!=-1)
				{
					count++;
					break loop;
				}
					}
			}
			if(count==n-1)
			  z++;  

		}

	System.out.println(z);	
	}	
}
