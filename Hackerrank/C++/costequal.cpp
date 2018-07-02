#include<iostream>
#include<string.h>
#include<math.h>
using namespace std;

int compute(string s1,string s2){
	int arr[s1.length()+1][s2.length()+1];
	for(int i=0;i<=s1.length();i++){
		for(int j=0;j<=s2.length();j++){
		if(i==0 || j==0)
		arr[i][j]=0;
		else if(s1[i-1]==s2[j-1])
		arr[i][j]=arr[i-1][j-1]+1;
		else
		arr[i][j]=max(arr[i-1][j],arr[i][j-1]);
 		}
    }
	return arr[s1.length()][s2.length()];     
}	

int main(){
	string s1,s2;
	int cs1,cs2,lcs=0;
	cin>>s1>>s2>>cs1>>cs2;
	lcs=compute(s1,s2);
	cout<<lcs<<" ";
	cout<<cs1*(s1.length()-lcs)+cs2*(s2.length()-lcs);
	return 0;
	}
