#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands)
{
    vector<int> answer;
    vector<int> stk;
    for (int i = 0; i < commands.size(); i++)
    {
        cout << i << endl;
        for (int j = commands[i][0] - 1; j < commands[i][1]; j++)
        {
            stk.push_back(array[j]);
        }
        sort(stk.begin(), stk.end());
        answer.push_back(stk[commands[i][2] - 1]);
        vector<int> tmp;
        stk = tmp;
    }
    return answer;
}