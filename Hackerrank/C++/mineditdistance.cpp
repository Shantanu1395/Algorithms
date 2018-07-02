#include<iostream>
#include<string.h>
#include<math.h>
using namespace std;

int minedit(string s1,string s2){
	int len1=s1.length(),len2=s2.length();
	int arr[len1+1][len2+1];
	for(int i=0;i<=len1;i++)
	arr[i][0]=i;
	for(int i=0;i<=len2;i++)
	arr[0][i]=i;
	for(int i=1;i<=len1;i++){
		for(int j=1;j<=len2;j++){
		if(s1[i]==s2[j])
		arr[i][j]=arr[i-1][j-1];
		else
			arr[i][j]=min(min(arr[i][j-1],arr[i-1][j-1]),min(arr[i-1][j-1],arr[i-1][j]))+1;
		}
	}
	return arr[len1][len2];
}

int main(){
	string s1,s2;
	cin>>s1>>s2;
	cout<<minedit(s1,s2);
	return 0;
}
