#include <iostream>

using namespace std;

int main()
{
    int train[4][2];
    for(int i = 0; i < 4; i++) cin >> train[i][0] >> train[i][1];

    int human = 0;
    int res = 0;
    for(int i = 0; i < 4; i++)
    {
        human = human + train[i][1] - train[i][0];
        if(res < human) res = human;
    }
    cout << res << endl;

    return 0;
}