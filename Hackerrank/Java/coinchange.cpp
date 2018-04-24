#include<iostream>
#include<math.h>
#include<algorithm>
using namespace std;
int main(){
	int n,i,j,coins[n+1],sum;
	cin>>n;
	coins[0]=0;
	for(i=1;i<=n;i++)
	cin>>coins[i];
	sort(coins+1,coins+n+1);
	cin>>sum;
	int arr[n+1][sum+1];
	for(i=0;i<=n;i++)
	arr[i][0]=0;
	
	for(i=0;i<=n;i++){
		for(j=0;j<=sum;j++){
			if(i==0)
				arr[i][j]=j;
			else{
				if(j>=coins[i])
				arr[i][j]=min(arr[i-1][j],arr[i][j-coins[i]]+1);
				else
				arr[i][j]=arr[i-1][j];
		    }
		}
	}
	for(i=0;i<=n;i++){
		for(j=0;j<=sum;j++){
			cout<<arr[i][j]<<" ";
		}
		cout<<endl;
	}
	cout<<arr[n][sum];
	
	return 0;
}
