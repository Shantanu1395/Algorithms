#include<iostream>
using namespace std;
int main()
{
	int n,i,arr[10],h;
	cin>>n;
	for(i=0;i<n;i++)
		{
			cin>>arr[i];
		}
		for(i=0;i<n;i++)
			{
				h=1;
				for(int j=1;j<=arr[i];j++)
				{
						if((j)%2==1)
						h++;
						else
						h*=2;
			    }
			    cout<<h<<endl;
			}
	return 0;
}
