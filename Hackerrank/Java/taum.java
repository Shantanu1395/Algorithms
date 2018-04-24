import java.util.*;
import java.math.*;
class taum{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		long money[]=new long[1000];
		int i=0;
		for (i=0;i<n ;i++ ) {
		long black=sc.nextInt();
		long white=sc.nextInt();	
		long pblack=sc.nextInt();
		long pwhite=sc.nextInt();
		long change=sc.nextInt();

		long temp1=black*pblack;
		long temp2=white*pwhite;

		long x=white*(pblack+change);
		long y=black*(pwhite+change);

		if((temp1+temp2)<=(temp1+x) && ((temp1+temp2)<=(temp2+y)))
			money[i]=(temp1+temp2);
		else{
			if((temp1+x)>(temp2+y))
				money[i]=(temp2+y);
			else 
				money[i]=(temp1+x);
		}
	}
	for(i=0;i<n;i++)
		System.out.println(money[i]);
		
	}
}