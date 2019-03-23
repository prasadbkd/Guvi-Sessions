#include <iostream>
using namespace std;

class mystring
{
	public:
	void reverse(char a[]){
		int i,j,t,k;
		i=0;
		j=5;
		char c[7];
		for(k=0;k<7;k++)
		{
			c[k]=a[k];
		}
		while(i<j)
		{
		t=c[i];
		c[i]=c[j];
		c[j]=t;
		i++;
		j--;
			
		}
		printf("%s",c);
	}
	
	
	char* copy(char a[])
	{
		int i;
		char* b = (char*)malloc(10 * sizeof(char));

		for(i=0;i<7;i++)
		{
			b[i]=a[i];
			
		}
		return b;
		//printf("\n%s",b);
	}
	
	
	
	
	
	
};

int main()
{
	mystring m;
	char a[7]="prasad";
	m.reverse(a);
	cout<<"test";
	cout<<m.copy(a);
return 0;
	
}
