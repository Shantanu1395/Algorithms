import java.util.*;
class acm{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		int b=sc.nextInt();
		int arr[]=new int[1000];
		String s[]=new String[1000];
		int i=0,j=0;
		int k=0;
		for (i=0;i<a ;i++ ) 
			s[i]=sc.next();
		int c=0;
		for (i=0;i<a-1 ;i++ ) {
			for (j=i+1;j<a ;j++ ){ 
				for( k=0;k<b;k++){
				if (s[i].charAt(k)=='1' && s[j].charAt(k)=='1') 
					arr[c]++;
				else if(s[i].charAt(k)=='1' && s[j].charAt(k)=='0')
					arr[c]++;
				else if(s[i].charAt(k)=='0' && s[j].charAt(k)=='1')
					arr[c]++;
			    }
			    c++;
			}
		}

		int max=arr[0];
		for (i=0;i<c ;i++ ) {
			if (max<arr[i]) 
				max=arr[i];
		}
		int count=0;
		for (i=0;i<c ;i++ ) {
			if(arr[i]==max)
				count++;
		}
		System.out.println(max);
		System.out.println(count);

	}
}