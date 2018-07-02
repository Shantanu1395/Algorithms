#include<iostream>
#include<math.h>
using namespace std;
int main(){
	int rodlen;
	cin>>rodlen;
	int n=rodlen-1;
	int rodlenarr[n+1];
	
	for(int i=1;i<=n;i++)
	cin>>rodlenarr[i];
	
	int arr[n+1][rodlen+1];
	
	for(int i=0;i<n;i++)
	arr[i][0]=0;
	
	for(int i=1;i<=rodlen;i++)
	arr[0][i]=i*rodlenarr[1];
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=rodlen;j++){
			if(j>=i){
				arr[i][j]=max(arr[i][j-i]+rodlenarr[i],arr[i-1][j]);
			}
			else
			arr[i][j]=arr[i-1][j];
		}
	}
	for(int i=1;i<=n;i++){
		for(int j=0;j<=rodlen;j++)
		cout<<arr[i][j]<<" ";
		cout<<endl;
	}
	cout<<arr[n][n+1];
	return 0;
}
