import java.util.*;
import java.math.*;
class fact
{
public static void main(String hg[])
	{
	BigInteger count=BigInteger.ONE;
	Scanner sc=new Scanner(System.in);
	int n=sc.nextInt();
	for(int i=n;i>0;i--)
	count=count.multiply(BigInteger.valueOf(i));
	System.out.println(count);	
	}
}
