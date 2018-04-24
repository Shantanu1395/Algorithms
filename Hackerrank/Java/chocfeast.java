import java.util.*;
class ck{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int temp[]=new int[1000];
		int i=0;
		for (i=0;i<n ;i++ ) {
			int money=sc.nextInt();
			int cost=sc.nextInt();
			int wfc=sc.nextInt();

			int choc=money/cost;
			int wrappers=choc;
			if(wfc==choc)
				choc++;
			else if(wfc>choc)
				choc=choc;
			else if(wfc<choc)
			{
				while(wrappers>=wfc)
				{
				choc+=wrappers/wfc;
				int l=wrappers/wfc;
				wrappers-=(wfc*(wrappers/wfc));
				wrappers+=(l);
				}
			}

			temp[i]=choc;
			
		}

		for(i=0;i<n;i++)
			System.out.println(temp[i]);
	}
}