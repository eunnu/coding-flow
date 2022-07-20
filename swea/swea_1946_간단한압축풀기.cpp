#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;
int main()
{
	char s[30];
	int n[30];

	int T, test = 0, a;

	cin >> T;
	for(test = 1; test <= T; test++)
	{
		cin >> a;
		for(int i = 0; i < a; i++)
		{
			cin >> s[i] >> n[i];
		}
		cout << "#" << test << endl;
		
		int temp = 0;
		for(int i = 0; i < a; i++)
		{
			for(int j = 0; j < n[i]; j++)
			{
				cout << s[i];
				temp ++;
				if(temp % 10 == 0) cout << endl;
			}
			
		}
		cout << endl;
	}
	
	return 0;
}