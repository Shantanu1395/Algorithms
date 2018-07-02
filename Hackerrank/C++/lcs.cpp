#include<iostream>
#include<string.h>
#include<math.h>
using namespace std;
int compute(int s1[],int s2[],int m,int n){
	int len1=m;
	int len2=n;
	int arr[len1+1][len2+1];
	for(int i=0;i<=len1;i++){
		for(int j=0;j<=len2;j++){
		if(i==0 || j==0)
		arr[i][j]=0;
		else if(s1[i-1]==s2[j-1])
		arr[i][j]=arr[i-1][j-1]+1;
		else
		arr[i][j]=max(arr[i-1][j],arr[i][j-1]);
 		}
    }
    
	return arr[len1][len2];     
}

int main(){
	int m,n,i;
	cin>>m>>n;
	int arr1[m],arr2[n];
	for(i=0;i<m;i++)
	cin>>arr1[i];
	for(i=0;i<n;i++)
	cin>>arr2[i];
	cout<<compute(arr1,arr2,m,n);
	return 0;
}	
