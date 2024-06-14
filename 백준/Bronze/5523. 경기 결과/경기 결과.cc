#include <iostream>

using namespace std;

int main() {
    long long N = 0, cnt_A = 0, cnt_B = 0;
    cin >> N;

    while (N > 0){
        int A = 0, B = 0;
        cin >> A >> B;
        if(A > B) cnt_A += 1;
        else if (A < B) cnt_B += 1;
        N -= 1;
    }

    cout << cnt_A << " " << cnt_B << endl;

    return 0;
}