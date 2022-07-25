#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T, test_case;
	cin >> T;

	for(test_case = 1; test_case <= T; test_case++)
	{
		int N;
		cin >> N;

		int arr[10001] = {0,};
		long long sum = 0;
		long long mid = 0;
		int cnt = 0;

		for(int i = 0; i < N ; i++) 
		{
			int num = 0;
			cin >> num;
			sum += num;
			arr[i] = num;
		}

		mid = sum / N;
		sort(arr, arr+N);

		for(int i = 0; i < N; i++)
		{
			if(arr[i] > mid) break;
			else if(arr[i] <= mid) cnt++;
		}

		cout << '#' << test_case << " " << cnt << endl;

	}
	return 0;
}