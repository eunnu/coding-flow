#include <iostream>

using namespace std;

bool word[16][16];
int res;

int low_x(int n, int k)
{
	for(int i = 0; i < n; i++)
	{
		int tmp = 0;
		bool check = false;

		for(int j = 0; j < n; j++)
		{
			if(word[i][j] && !check)
			{	
				check = true;
				tmp++;
			}
			else if(word[i][j] && check)
			{								
				tmp++;
				if(tmp == k) res++;
				else if(tmp > k)
				{
					res = res - 1;
					tmp = 0;
					continue;
				} 							
			}
			else if(check && !word[i][j])
			{
				tmp = 0;
				check = false;				
			}			
		}
	}
}

int low_y(int n, int k)
{
	for(int i = 0; i < n; i++)
	{
		int tmp = 0;
		bool check = false;

		for(int j = 0; j < n; j++)
		{
			if(word[j][i] && !check)
			{	
				check = true;
				tmp++;				
			}
			else if(word[j][i] && check)
			{								
				tmp++;
				if(tmp == k) res++;
				else if(tmp > k)
				{
					res = res - 1;
					tmp = 0;
					continue;
				}				
			}
			else if(check && !word[j][i])
			{
				tmp = 0;
				check = false;				
			}			
		}		
	}
}

int main()
{
	int test_case, T;
	
	cin >> T;

	for(test_case = 1; test_case <= T; test_case++)
	{
		int n, k;
		res = 0;

		cin >> n >> k;

		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				cin >> word[i][j];

		low_x(n, k);
		low_y(n, k);

		cout << "#" << test_case << " " << res << endl;

	}

	return 0;
}