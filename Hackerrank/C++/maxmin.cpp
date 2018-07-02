#include<iostream>
using namespace std;
int main()
{
	int i;
	unsigned long n,x,*arr=new unsigned long[3200000],max,min;
	cin>>n;
	cin>>x;
	for(i=0;i<n;i++)
	cin>>arr[i];
	max=arr[0];
	min=arr[0];
	for(i=0;i<n;i++)
		{
			if(arr[i]>max)
			arr[i]=max;
		}
		for(i=0;i<n;i++)
		{
			if(arr[i]<min)
			arr[i]=min;
		}
		cout<<max-min;
		
	return 0;
}
