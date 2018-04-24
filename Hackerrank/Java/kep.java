import java.util.*;
class kep
{
static void kepno(Long x)
{
long y=x*x;
String s=Long.toString(y);
if(s.length()>=2)
{
String s1=s.substring(0,(s.length()/2));
String s2=s.substring(s.length()/2,s.length());
if(x==(Long.parseLong(s1)+Long.parseLong(s2)))
System.out.print(x+" ");
}
else if(s.length()==1 && x==1)
System.out.print(1+" ");
}

static boolean iskepno(Long x)
{
long y=x*x;
String s=Long.toString(y);
if(s.length()>=2)
{
String s1=s.substring(0,(s.length()/2));
String s2=s.substring(s.length()/2,s.length());
if(x==(Long.parseLong(s1)+Long.parseLong(s2)))
return true;
else 
return false;
}
else if(s.length()==1 && x==1)
return true;
else
return false;
}
 
public static void main(String gh[])
	{
	int count=0;
	Scanner sc=new Scanner(System.in);
    int p=sc.nextInt();
    int q=sc.nextInt();
	for(int i=p;i<=q;i++)
	  {
	   if(iskepno((long)i)==true)
	      {
		  count++;
	        kepno((long)i);
		  }	
	  }
      if(count==0)
	  System.out.print("INVALID NO");
	}
}