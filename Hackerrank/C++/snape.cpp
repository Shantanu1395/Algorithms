#include<iostream>
#include<math.h>
#include <stdio.h>
#include <string.h> 
using namespace std;
string str="";
int a=0,b=0;
int main(){
	int n;
	cin>>n;
	while(n--){
		cin>>a>>b;
		cout<<a%b<<endl;
	}
	return 0;
}
