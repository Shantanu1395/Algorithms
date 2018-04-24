import java.util.*;
class flip{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		long s1[]=new long[1000];
		int n=sc.nextInt();
		for(int i=0;i<n;i++)
			s1[i]=sc.nextLong();

		String s2[]=new String[1000];
		for (int i=0;i<n ;i++ ) {
			s2[i]=Long.toString(s1[i],2);
			while(s2[i].length()!=32)
				s2[i]="0"+s2[i];
		}

		for (int i=0;i<n ;i++ ) {
			{
			String t1=s2[i].replaceAll("1","3");
			t1=t1.replaceAll("0","4");
			t1=t1.replaceAll("3","0");
			t1=t1.replaceAll("4","1");
			s2[i]=t1;
			}
		}

		for (int i=0;i<n ;i++ ) {
			System.out.println(Long.parseLong(s2[i],2));
		}
	}
}