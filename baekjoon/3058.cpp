// 짝수를 찾아라
// https://www.acmicpc.net/problem/3058

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++){
        vector<int> nums;
        int input;
        for (int j=0; j < 7; j++){
            cin >> input;
            if (input % 2 == 0) nums.push_back(input);
        }
        
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int min = *min_element(nums.begin(), nums.end());
        cout << sum << " " << min << endl;
    }

    return 0;
}
