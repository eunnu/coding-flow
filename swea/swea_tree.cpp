#include <string>
#include <iostream>

using namespace std;
string make_bin(int num){
	string ans;
	int target = num;

	while(target) {
	int left = target % 2;
	ans = to_string(left) + ans;
	target /= 2;
	}

	return ans;
}

int main(void){
	int T = 0;
	cin >> T;
	int dist_left, dist_right, total_dist = 0;
	
	for(int test_case = 1; test_case <= T; test_case++)
	{
		int N, V = 0;
		cin >> N >> V;
		string nn, vv;
		nn = make_bin(N);
		vv = make_bin(V);

		string a;
		string b;

		if(nn.size() > 1 && vv.size() > 1){
			for(int i = 0; i < 2; i++)
			{
				a += nn[i];
				b += vv[i];
			}
		}

			if(a == "10"){
				dist_left = nn.size() - 1;
				dist_right = nn.size() - 2;
			}
			else{
				dist_left = nn.size() - 1;
				dist_right = nn.size() - 1;
			}

			if(b == "10"){
				total_dist = vv.size() - 1 + dist_right;
			}
			else{
				total_dist = vv.size() - 1 + dist_left;
			}
			cout << "#" << test_case << " " << total_dist << endl;
	}	
	return 0;
}