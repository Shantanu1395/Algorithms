import java.util.*;
import java.math.*; 
class Solution
{
	public static void main(String gh[])
		{
		long i=0,j=0;
		
		Scanner sc=new Scanner(System.in);
		long a=sc.nextLong();
		long b=sc.nextLong();
		int n=sc.nextInt();
		/*for(i=3;i<15;i++)
			{
			System.out.println(i+"th term:"+Fibo(a,b,i));
			}
	*/
        long x1 = a, y1 = b, z1 = b;
        BigInteger x=BigInteger.valueOf(x1);
        BigInteger y=BigInteger.valueOf(y1);
        BigInteger z=BigInteger.valueOf(z1);
        for ( i = 0; i < n-2; i++) {
            //x = a;
            y = z;
            z = x.add(y.multiply(y));
            x=y;
        }
        
       System.out.println(z);
		}
}