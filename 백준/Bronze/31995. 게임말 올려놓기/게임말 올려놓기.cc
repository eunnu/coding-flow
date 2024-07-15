#include <stdint.h>
#include <iostream>

using namespace std;

int N, M;

int main(){
	int result = 0;
	cin >> N;
	cin >> M;

	result = (N-1)*2*(M-1);
	if (result < 0) result = 0;
	cout << result << endl;

	return 0;
}