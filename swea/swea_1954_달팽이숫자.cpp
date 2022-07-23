#include <iostream>
#include <algorithm>
#include <memory>

using namespace std;


int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
	int T, test_case;
	cin >> T;

	for(test_case = 1; test_case <= T; test_case++)
	{
		int arr[10][10] = {0, };
		int n = 0;

		cin >> n;
		
		int snail = n*n; // while문의 조건 -> 마지막 숫자의 크기
		arr[0][0] = 1; // 시작위치
		int cnt = 2; // 1을 이미 넣고 시작하기 때문에 2
		int x = 0, y = 0;

		int dir = 0; // 회전을 해주기 위한 변수
		while(cnt <= snail)
		{
			int nx = x + dx[dir];
			int ny = y + dy[dir];

			if(nx < 0 || ny < 0 || nx >= n || ny >= n || arr[ny][nx])
			{				
				dir += 1;
				if(dir == 4) dir = 0;
				continue;
			}			
			arr[ny][nx] = cnt;
			cnt++;
			x = nx;
			y = ny;
		}

		cout << '#' << test_case << endl;

		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				cout << arr[i][j] << " ";
			}
			cout << endl;
		}	
	}
	return 0;
}