#include<iostream>
#include<string.h>
#include<algorithm>
#include <vector>
using namespace std;

int cal(vector<int>& a){
	vector<vector<int> > L(a.size());
	L[0].push_back(a[0]);
	for(int i=1;i<a.size();i++){
		for(int j=0;j<i;j++){
			if((a[i]>a[j]) && (L[i].size()<L[j].size()+1))
			L[i]=L[j];
		}
		L[i].push_back(a[i]);
	}
	int max=0;
	for(int i=0;i<L.size();i++){
		if(L[i].size()>max)
		max=L[i].size();
	}
	return max;
}

int main(){
	int n,i;
	cin>>n;
	int arr[n];
	for(i=0;i<n;i++)
	cin>>arr[i];
	sort(arr,arr+n);
	vector<int> a(arr,arr+sizeof(arr)/sizeof(arr[0]));
	cout<<cal(a);
	return 0;
}
