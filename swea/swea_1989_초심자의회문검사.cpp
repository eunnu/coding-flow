#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;
int main()
{
	char s[10];

	int T, test = 0;

	cin >> T;
	for(test = 1; test <= T; test++)
	{
		cin >> s;

		int a = strlen(s);

		bool temp = true;
		for(int i = 0; i <= a / 2; i++)
		{
			if(s[i] != s[a - i - 1])
			{
				temp = false;
				break;
			}
		}

		cout << "#" << test << " " << temp << endl;

	}
	
	return 0;
}