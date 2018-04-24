#include<iostream>
using namespace std;
int main()
{
	int l,r,i,j,maximum;
	unsigned long *arr=new unsigned long[3200000],k=0;
	cin>>l>>r;
    if(l<=r && r<=1000 && r>=1)
        {
	for(i=l;i<=r;i++)
	{
		for(j=i;j<=r;j++)
		{
		arr[k]=i^j;    
		k++;
	    }
	}			
		 maximum = arr[0];
 
  for (i=0;i<k;i++)
  {
    if (arr[i] > maximum)
    {
       maximum  = arr[i];
    }
  }
 cout<<maximum;
    }
    else 
    return 0;   
	return 0;
}
