#include <iostream>

using namespace std;

int main()
{
	int A, B;

	cin >> A >> B;

	if(A == 1)
	{
		if(B == 2) cout << "B" << endl;
		else cout << "A" << endl;
	}

	else if(A == 2)
	{
		if(B == 3) cout << "B" << endl;
		else cout << "A" << endl;
	}

	else
	{
		if(B == 1) cout << "B" << endl;
		else cout << "A" << endl;
	}
}