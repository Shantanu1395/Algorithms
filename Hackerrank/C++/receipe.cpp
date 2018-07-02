#include<iostream>
using namespace std;
int arr[51],gcd=0,tempgcd=1;

int cal_gcd(int a,int b){
	return b==0?a:cal_gcd(b,a%b);
}

int cal_totalgcd(int n){
	tempgcd=arr[0];
	for(int i=0;i<n;i++)
	tempgcd=cal_gcd(tempgcd,arr[i]);
	return tempgcd;
}

int main(){
	int t;
	cin>>t;
	while(t--){
		int n;
		gcd=1;
		cin>>n;
		for(int i=0;i<n;i++)
		cin>>arr[i];
		gcd=(cal_totalgcd(n));
		for(int i=0;i<n;i++)
		cout<<arr[i]/gcd<<" ";
		cout<<endl;
	}
	return 0;
}
