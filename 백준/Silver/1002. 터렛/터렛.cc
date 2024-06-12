#include <stdio.h>
#include <math.h>
#include <iostream>

using namespace std;

int main()
{
    int T = 0;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int x1 = 0, y1 = 0, r1 = 0, x2 = 0, y2 = 0, r2 = 0;
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        double distance =sqrt((pow(x1-x2, 2)) + pow(y1-y2, 2));
        
        if (distance == 0){
            if (r1 == r2) cout << -1 << endl;
            else cout << 0 << endl;
        }
        else {
            if(abs(r1-r2) < distance && distance < r1 + r2) cout << 2 << endl;
            else if (distance == r1 + r2 || abs(r1 - r2) == distance) cout << 1 << endl;
            else cout << 0 << endl;
        }

    }
    return 0;
}