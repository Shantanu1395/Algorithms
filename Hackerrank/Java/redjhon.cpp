#include<iostream>
#include<math.h>
#include <bits/stdc++.h>
using namespace std;

int numbers(int n)
{

    bool prime[n+1];
    memset(prime, true, sizeof(prime));
 
    for (int p=2; p*p<=n; p++)
    {
        // If prime[p] is not changed, then it is a prime
        if (prime[p] == true)
        {
            // Update all multiples of p
            for (int i=p*2; i<=n; i += p)
                prime[i] = false;
        }
    }
 
 int count=0;
    // Print all prime numbers
    for (int p=2; p<=n; p++)
       if (prime[p])
          count++;
          return count;
}

int main(){
	int t,n=0,ways=1,i=0;
	int count[50];
	cin>>t;
	while(t--){
		cin>>n;
		for(i=0;i<=n;i++){
		count[i]=1;
		}
		
		for(i=1;i<=n;i++){
			if(i>=4)
			count[i]=(count[i-1]+count[i-4]);
		}
		
		ways=count[n];
		cout<<numbers(ways)<<endl;
	}
	return 0;
}
