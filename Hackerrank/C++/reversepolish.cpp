#include<iostream>
#include<string>
using namespace std;
char stack[500];
int size=-1,n=0;
string str="";

void push(char x){
	stack[++size]=x;
}

char pop(){
return stack[size--];
}

int main(){
	cin>>n;
	while(n--){
	cin>>str;
		for(int j=0;j<str.length();j++){
			
		if(str[j]>='a' && str[j]<='z')
		cout<<str[j];	
		
		else if(str[j]==')')
			cout<<pop();

		else if(str[j]!='(')
		push(str[j]);
		
		}
		cout<<endl;
	}
	return 0;
}
