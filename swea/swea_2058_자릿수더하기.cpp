#include <iostream>
#include <algorithm>

using namespace std;
int main()
{
	int N;
	int res = 0;

	cin >> N;

	while(N > 0)
	{
		int a = N % 10;
		res = res + a;
		N = N / 10;
	}

	cout << res;

	return 0;
}