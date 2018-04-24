import java.util.*;
class r
{

public static int fact(int n)
{
	int count=1;
	for(int i=n;i>0;i--)
	count*=i;
	return count;
}

	public static void main(String[] y) {
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
		int i=0;
		float b[]=new float[99];
		float c[]=new float[99];
		for(int j=0;j<n;j++)
		{
			b[j]=0;
		float a=s.nextFloat();
		int x=0;
		double k=0;
		for(i=1;i<=9;i+=2)
		{	
			b[j]+=(Math.pow(-1,x))*(Math.pow(a,i))/fact(i);
			x++;
		}

		x=0;
		k=0;
		c[j]=0;
		for(i=0;i<=8;i+=2)
		{	
			c[j]+=(Math.pow(-1,x))*(Math.pow(a,i))/fact(i);
			x++;
		}
}

	for (i=0;i<n ;i++ ) {
	System.out.printf("%.3f\n%.3f\n",b[i],c[i]);
	}

}
}