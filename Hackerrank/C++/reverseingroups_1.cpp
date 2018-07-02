#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;
int arr[100],n=0,k=0,x=0;
int main(){
	cin>>n>>k;
	for(int i=0;i<n;i++){
	cin>>x;
	arr[(i+k-1)%(k+1)]=x;
    }
	
	
	for(int i=0;i<n;i++)
	cout<<arr[i]<<" ";
	return 0;
}
