#include<iostream>
using namespace std;
int main(){
	int t,n=4;
	while(1){
		cin>>n;
		if(n==0)break;
		int arr[n],flag=0;
		for(int i=0;i<n;i++)
		cin>>arr[i];
		for(int i=0;i<n;i++){
		if(i+1!=arr[arr[i]-1]){
		flag=1;
		break;
	    }
		}
		if(flag==1)
		cout<<"not ambiguous\n";
		else
		cout<<"ambiguous\n";		
	}
	return 0;
}
