import java.util.*;
import java.text.DecimalFormat;
class plusminus
{
public static void main(String gh[])
	{
	DecimalFormat df = new DecimalFormat("#.###");
	int count=0,count1=0,count2=0,count3=0;
	Scanner sc=new Scanner(System.in);
	int n=sc.nextInt();
	for(int i=0;i<n;i++)
		{
		int x=sc.nextInt();
		if(x>0)
		count1++;
		else if(x==0)
		count2++;
		else if(x<0)
		count3++;
		count++;
		}
	System.out.print(String.format("%.6f\n%.6f\n%.6f",(float)count1/count,(float)count3/count,(float)count2/count));	
	}
                     }                 