#include <iostream>
using namespace std;

int connected(int i,int j,int n,int m,int arr[][],bool visited[][]){
	if(i<0 || j<0 || i>n-1 || j>m-1)
		return 0;
	else{
		int a=visited[i-1][j]==false?connected[i-1][j]:0;
		visited[i-1][j]=true;
		int b=visited[i+1][j]==false?connected[i+1][j]:0;
		visited[i+1][j]=true;
		int c=visited[i][j-1]==false?connected[i][j-1]:0;
		visited[i][j-1]=true;
		int d=visited[i][j+1]==false?connected[i][j+1]:0;
		visited[i][j+1]=true;
		int e=visited[i-1][j-1]==false?connected[i-1][j-1]:0;
		visited[i-1][j-1]=true;
		int f=visited[i-1][j+1]==false?connected[i-1][j+1]:0;
		visited[i-1][j+1]=true;
		int g=visited[i+1][j+1]==false?connected[i+1][j+1]:0;
		visited[i+1][j+1]=true;
		int h=visited[i+1][j-1]==false?connected[i+1][j-1]:0;
		visited[i-1][j+1]=true;		
		return a+b+c+d+e+f+g+h;
	}
}

int main(int argc, char const *argv[])
{
	int i,j,n,m,arr[n][m];
	bool visited[n][m]; 
	cin>>n>>m;
	for (i = 0; i < n; i++)
		{
			for ( j = 0; j < m; j++)
				cin>>arr[i][j];
		}
		for (i = 0; i < n; i++)
		{
			for ( j = 0; j < m; j++)
				visited[i][j]=false;
		}	
		cout<<connected(i,j,n,m,arr,visited);
	return 0;
}


