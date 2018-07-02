#include<iostream>
#include<math.h>
using namespace std;
int main(){
	int n,p,count=0;
	cin>>n;
	for(int i=0;i<n;i++){
	cin>>p;
	count=0;
	for(int j=11;j>=0;j--){
		int x=pow(2,j);
		if(p-x>=0){
			count++;
			j++;
			p-=x;
		}
	}
		cout<<count<<endl;
		}
	return 0;
}
