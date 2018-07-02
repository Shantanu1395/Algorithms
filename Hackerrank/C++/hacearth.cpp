#include<iostream>
#include<string.h>
#include<string>
using namespace std;
int main(){
	int n,i,j;
	string s;
	cin>>n;
	for(i=0;i<n;i++){
		int a;
		cin>>a;
		s=to_string(a);
		cout<<s;
		int flag=0;
		for(j=0;j<s.length()-1;j++){
			if(a%29==0 && (s[i]=='2' && s[i+1]=='1'))
			flag=1;
		}
		if(flag==0)
		cout<<"The streak lives still in our heart!\n";
		else
		cout<<"The streak is broken!\n";
	}
	return 0;
}
