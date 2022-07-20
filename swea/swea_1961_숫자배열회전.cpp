#include <iostream>

using namespace std;

int arr[8][8];
int arr_90[8][8];
int arr_180[8][8];
int arr_270[8][8];

int test_case, T;

bool area_90(int n)
{
	for(int i = 0; i < n; i++)
	{	
		int k = 0;
		for(int j = (n - 1); j >= 0; j--)
		{
			arr_90[i][k] = arr[j][i];
			k++;
		}
	}
}

bool area_180(int n)
{
	int k = 0;
	for(int i = (n - 1); i >= 0; i--)
	{
		int l = 0;
		for(int j = (n - 1); j >= 0; j--)
		{
			arr_180[k][l] = arr[i][j];
			l++;
		}
		k++;
	}

}

bool area_270(int n)
{
	int k = 0;
	for(int i = (n - 1); i >= 0; i--)
	{
		for(int j = 0; j < n; j++)
		{
			arr_270[k][j] = arr[j][i];
		}
		k++;
	}

}

int main()
{
	cin >> T;

	for(test_case = 1; test_case <= T; test_case++)
	{
		int n = 0;
		cin >> n;

		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++) cin >> arr[i][j];

		cout << "#" << test_case << endl;

		area_90(n);
		area_180(n);
		area_270(n);

		for(int i = 0; i < n; i++)
		{
			int j = 0, k = 0, l = 0;
			while(j < n)
			{
				cout << arr_90[i][j];
				j++;
			}
			cout << " ";
			while(k < n)
			{
				cout << arr_180[i][k];
				k++;
			}
			cout << " ";
			while(l < n)
			{
				cout << arr_270[i][l];
				l++;
			}
			cout << endl;
		}

	}

	return 0;
}
