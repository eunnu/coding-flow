#include <stdint.h>
#include <iostream>

using namespace std;

int characters[5] = {0, };
int result = 0;

int main(){
	for(int i = 0; i < 5; i++){
		cin >> characters[i];
		if(i >= 1){
			if(characters[0] - characters[i] <= 1000) result += 1;
 		}
	}

	cout << result << endl;

	return 0;
}

