#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
    int N, max = 0, b = 0, num = 0, c = 0;
    vector <double> v;

    cin >> N;
    
    double result = 0;

    for (int i = 0; i < N; i++)
    {
        cin >> b;
        result = 0, c = 0;
        v.clear();
        v.resize(b);

        for (int j = 0; j < b; j++)
        {
            cin >> v[j];
            result += v[j];
        }

        result = result / b;

        for (int j = 0; j < b; j++)
        {
            if (v[j] > result) c++;
        }

        result = (double)c * 100 / b;
        printf("%.3lf%%\n", round(result * 1000) / 1000);
        
    }

    return 0;
}