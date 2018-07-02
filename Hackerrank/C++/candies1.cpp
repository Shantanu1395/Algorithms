#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
	int n,i;
	cin>>n;
	int arr[n],arr1[n],arr2[n];
	fill_n(arr1,n,0);
	fill_n(arr2,n,0);
	for (i = 0; i < n; i++)
		cin>>arr[i];
	int sum=0;
	
	arr1[0]=1;
	arr2[n-1]=1;
	arr2[0]=0;
	arr1[n-1]=0;
	int x=0;
	for (int i = 1; i < n;i++)
	{
		if (arr[i]>arr[i-1]){
			arr1[i]=arr1[i-1]+1;
		}
		else{
			arr1[i]=1;
		}
	}
	for (int i = n-2; i >=0;i--)
	{
		if (arr[i]>arr[i+1]){
			arr2[i]=arr2[i+1]+1;
		}
		else{
			arr2[i]=1;
		}
	}
	
	cout<<"\n";
	for (int i = 0; i < n; i++){
		cout<<arr1[i]<<" ";
	}
	cout<<endl;
	
	
	for (int i = 0; i < n; i++){
		cout<<arr2[i]<<" ";
	}
	cout<<endl;
	
	
	for (int i = 0; i < n; i++){
		arr1[i]=max(arr1[i],arr2[i]);
		sum+=arr1[i];
	}
	cout<<endl;
	cout<<sum;
	return 0;		
}
