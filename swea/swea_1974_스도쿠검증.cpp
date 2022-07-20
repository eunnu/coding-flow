#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

int puzzle[10][10];
int test_case, T;


int low_x()
{
	bool temp = true;
    bool visited[10];
	for(int i = 0; i < 9; i++)
	{
		 memset(visited, 0, sizeof(visited));
		for(int j = 0; j < 9; j++)
		{
			int num = puzzle[i][j];
			if(visited[num])
			{
				temp = false;
				break;
			}
			else visited[num] = true;
		}
        if(!temp) break;
	}
	return temp;
}

int low_y()
{
	bool temp = true;
    bool visited[10];
	for(int i = 0; i < 9; i++)
	{
		 memset(visited, 0, sizeof(visited));
		for(int j = 0; j < 9; j++)
		{             
			int num = puzzle[j][i];
			if(visited[num])
			{
				temp = false;
				break;
			}
			else visited[num] = true;
		}
         if(!temp) break;
	}
	return temp;
}

int area(int a, int b)
{
	bool temp = true;
	bool visited[10];
    memset(visited, 0, sizeof(visited));
	for(int i = a; i < a + 3; i++)
	{
		for(int j = b; j < b + 3; j++)
		{
			int num = puzzle[i][j];
            //cout << num << " " << visited[num] << endl;
			if(visited[num])
			{
				temp = false;
				break;
			}
			else visited[num] = true;
		}
         if(!temp) break;
	}
	return temp;
}

int main()
{
	cin >> T;

	for(test_case = 1; test_case <= T; test_case++)
	{
		for(int i = 0; i < 9; i++)
			for(int j = 0; j < 9; j++) cin >> puzzle[i][j];

		bool res_x = false, res_y = false, res_area = false;
		bool res = false;

		res_x = low_x();
		res_y = low_y();

       for(int i = 0; i < 7; i = i + 3)
       {
           for(int j = 0; j < 7; j = j + 3)
           {
               res_area = area(i, j);
               if(!res_area) break;
           }
            if(!res_area) break;
       }

		if(res_x && res_y && res_area) res = true;
		cout << "#" << test_case << " " << res << endl;

	}
	return 0;
}
