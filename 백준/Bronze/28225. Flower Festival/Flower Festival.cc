# include <iostream>

using namespace std;

int main(){
    int N = 0, D = 0;
    int res = 0;

    cin >> N >> D;

    float t = 987654321;

    for(int i = 1; i <= N; i++){
        
        float location = 0, speed = 0;

        cin >> location >> speed;

        if( t > ((D - location) / speed) ){
            t = (D - location) / speed;
            res = i;
        }
    }
    cout << res << endl;
    return 0;
}   