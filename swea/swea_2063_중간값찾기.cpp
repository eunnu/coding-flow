#include <iostream>
#include <algorithm>

int arr[200];

using namespace std;
int main()
{
	int N;

	cin >> N;
	for(int i = 0; i < N; i++) cin >> arr[i];

	sort(arr, arr+N);

	int a = N/2;
	cout << arr[a] << endl;

	return 0;
}