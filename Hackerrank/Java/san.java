import java.util.*;
class sa{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		long n=sc.nextLong();
		long ans[]=new long[1000];
		long i=0,j=0;
		for(i=0;i<n;i++)
		{
			long total=0,right_sum=0;
			long left_sum=0;
			long size=sc.nextLong();
			ArrayList<Long> arr=new ArrayList<Long>();
			loop:{
			for (j=0;j<size ;j++ ) 
			{
				long temp=sc.nextLong();
				arr.add(temp);
				total+=temp;
			}

			for (j=0;j<size ;j++ ) 
			{
				right_sum=total-arr.get((int)j)-left_sum;
				//System.out.println("Left"+left_sum+" Right:"+right_sum);
				if(right_sum==left_sum)
				{
					ans[(int)i]=1;

					//break loop;
				}
				left_sum+=arr.get((int)j);
			}
		    }

		}
		for (i=0;i<n ;i++ )
		{
			if(ans[(int)i]==1)
				System.out.println("YES");
			else
				System.out.println("NO");
		} 
	}
}