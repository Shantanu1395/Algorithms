import java.util.*;
class temp
{
public static void main(String gh[])
{
long count=0;
Scanner sc=new Scanner(System.in);
long arr[]=new long[1000];
long n=sc.nextLong();
for(long i=0;i<n;i++)
{
arr[(int)i]=sc.nextLong();
count+=arr[(int)i];
}
System.out.println(count);
}
}
