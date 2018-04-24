 import java.util.*;
 class ins{
 	public static void main(String[] args) {
 		Scanner sc=new Scanner(System.in);
 		int n=sc.nextInt();
 		int arr[]=new int[2000];
 		int i=0;
 		for (i=0;i<n ;i++ ) 
 		arr[i]=sc.nextInt();
 		
 		int temp1=arr[n-1];
 		//System.out.println(n);
 		int a=n;
 		loop: {
 		for (i=0;i<a ;i++ ) {
 	
 		if(temp1>arr[a-2-i])
 		{
		arr[a-1-i]=temp1;
		break loop;
		}
		else{
		int temp2=arr[a-2-i];
 		arr[a-1-i]=temp2;
 		//System.out.print("Pass "+i+":");
		for(int x=0;x<a;x++)
		System.out.print(arr[x]+" ");
		System.out.println();
	    }
 		}
 		}

 		for(int x=0;x<a;x++)
		System.out.print(arr[x]+" ");
 	}
 }