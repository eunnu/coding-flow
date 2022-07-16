#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int area[16][16];
vector<int> die;

bool comp(int a, int b){ return a > b; }

bool sol(int a, int b, int m)
{
	int sum = 0;
	for(int i = a; i < a + m; i++)
	{
		for(int j = b; j < b + m; j++)
		{
			sum += area[i][j];
		}
	}
	die.push_back(sum);
}

int main()
{
	int test_case, T;
	cin >> T;

	for(test_case = 1; test_case <= T; test_case++)
	{
		int n, m;
		cin >> n >> m;

		die.clear();

		for(int i = 0; i < n; i++ )
			for(int j = 0; j < n; j++) cin >> area[i][j];

		for(int i = 0; i < (n - m); i++)
			for(int j = 0; j < (n - m); j++) sol(i, j, m);

		sort(die.begin(), die.end(), comp);

		cout << "#" << test_case << " " << die[0] << endl;
	}
	return 0;
}