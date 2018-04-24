import java.util.*;
class Sol
{
static int issq(long x)
{
if(Math.sqrt(x)==(int)Math.sqrt(x))
return 1;
else 
return 0;
}

public static void main(String gh[])
{
long i=0;
long s[]=new long[10000];
Scanner sc=new Scanner(System.in);
long n=sc.nextInt();
for(i=0;i<n;i++) 
	{
	int count=0;
	double a=sc.nextDouble();
	double b=sc.nextDouble();
	for(long j=(long)Math.floor(Math.sqrt(a));j<=(long)Math.floor(Math.sqrt(b));j++)
		{
		if(j>(Math.sqrt(a)))
		count++;
		else if(j==(Math.sqrt(a)))
		count++;
		}
	s[(int)i]=count;	
	}
for(i=0;i<n;i++)
System.out.println(s[(int)i]);	
}
}
