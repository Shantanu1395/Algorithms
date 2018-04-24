 import java.util.*;
class make{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String s1=sc.next();
		String s2=sc.next();
		int arr[]=new int[1000];
		int arr1[]=new int[1000];
		int x=0,i=0;

		for ( i=0;i<s1.length() ;i++ ) 
			arr1[(int)s1.charAt(i)]++;		

		for ( i=0;i<s2.length() ;i++ )
				arr[(int)s2.charAt(i)]++;

		for (i=97;i<=122 ;i++ ) {
		if(arr[i]>0)
			x+=Math.min(arr[i],arr1[i]);
		}		

		System.out.println((s1.length()-x)+(s2.length()-x));
	}
}