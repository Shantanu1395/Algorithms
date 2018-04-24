#include<iostream>
#include<vector>
using namespace std;
int main(){
	int n,p,q;
	cin>>n;
	vector<int> arr(n);
	for(int i=0;i<n;i++){
	int n;
	cin>>n;	
	arr.push_back(n);
    }
    for(unsigned i=0;i<n;i++)
    cout<<arr.get(i)<<" ";
    cout<<endl;
    cin>>p>>q;
    int range=q-p;
    vector<int> numrange(range+1);
    for(int i=0;i<=range;i++){
    	numrange.push_back(q+i);
	}
    vector< vector<int> > vec(range+2, vector<int>(n+1));
    for(int i=0;i<=range+1;i++){
    	int m=0;
    	for(int j=0;j<n;j++){
    		vec[i][j]=arr[j]-numrange[i];
    		cout<<vec[i][j]<<" ";
    		m=min(m,vec[i][j]);
		}
		cout<<endl;
		vec[i][n]=m;
	}
	for(int i=0;i<=range;i++){
    	for(int j=0;j<=n;j++){
    	cout<<vec[i][j]<<" ";	
		}
		cout<<endl;
	}
	return 0;
}
