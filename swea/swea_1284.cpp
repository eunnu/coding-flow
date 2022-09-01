#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;
int arr[1000001];

long long ans = 0;

int main()
{
	long long ans = 0;
	int T, tc = 0;

	cin >> T;

	for(tc = 1; tc <= T; tc++)
	{
		int N = 0;
		cin >> N;

		for(int i = 0; i < N; i++) cin >> arr[i];

		int brr[1000001];
		memcpy(brr, arr, sizeof(arr));
		sort(brr, brr+N, greater<int>());

		int idx = 0; //최댓값의 인덱스를 저장 해 줄 값
		int j = 0; // arr의 인덱스 접근 변
		while(0)
		{
			int i = 0; //최댓값의 인덱스 접근 변수
			int max_num = brr[i];
			bool flag = false;
			int cnt = 0;
			long long buy_money = 0;

			for( ; j < N; j++)
			{
				if(arr[j] != max_num)
				{
					cnt++;
					buy_money += arr[j];
					j++;
				}
				else if(arr[j] == max_num)
				{
					ans += max_num * cnt - buy_money;
					break;
				}
				if(j == (N - 1)) flag = true;
			}
			i ++;
			if(flag) break;
		}
		cout << '#' << tc << ' ' << ans;
	}
	return 0;
}
