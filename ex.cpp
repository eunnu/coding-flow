#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

vector <int> arr;
vector <int> brr;
long long res;

void sola(int a, int b)
{	
	long long tmp = 0;
	for(int i = 0; i < a; i++)
	{
		tmp = tmp + (arr[i] * brr[i + b]);
		
	}
	if(tmp > res) res = tmp;	
}

void solb(int b, int a)
{
	long long tmp = 0;
	for(int i = 0; i < b; i++)
	{
		tmp = tmp + (arr[i + a] * brr[i]);
	}
	if(tmp > res) res = tmp;

}

int main()
{
	int test, T;
	cin >> T;

	for(test = 1; test <= T; test++)
	{
		int a, b;
		cin >> a >> b;

		arr.clear();
		brr.clear();
		res = 0;		

		for(int i = 0; i < a; i++)
		{
			int tmp = 0;
			cin >> tmp;
			arr.push_back(tmp);
		}

		for(int i = 0; i < b; i++)
		{
			int tmp = 0;
			cin >> tmp;
			brr.push_back(tmp);
		}

		if(a == b)
		{
			for(int i = 0; i < a; i++)
			{
				res += (arr[i] * brr[i]);
				
			}
		}
		else
		{
			if(a > b)
			{
				int temp = 0;
				for(int i = 0; i <= (a - b); i++)
				{					
					solb(b, temp);
					temp += 1;					
				}
			} 			 
			else
			{
				int temp = 0;
				for(int i = 0; i <= (b - a); i++)
				{					
					sola(a, temp);
					temp += 1;					
				}
			} 		
			
		}

		cout << "#" << test << " " << res << endl;
	}
	
	return 0;
}