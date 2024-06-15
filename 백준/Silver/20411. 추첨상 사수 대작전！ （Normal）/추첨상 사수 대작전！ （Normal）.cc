#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;
int m = 0 , seed = 0 , x1 = 0 , x2 = 0 ;
int a = 0, c = 0;

int main()
{
    cin >> m >> seed >> x1 >> x2;
    for (a = 0; a < m; a++)
    {
        for (c = 0; c < m && ((long long)(seed - x1)*a + x2 - x1) % m == 0; c++)
        {
            if ((x1 + x2) % m == (a*(long long)(seed + x1) + 2 * c) % m)
            {
                cout << a << " " << c;
                return 0;
            }
        }
    }
    return 0;
}