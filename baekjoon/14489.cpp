// 치킨 두 마리 (...)
// https://www.acmicpc.net/problem/14489

#include <iostream>

using namespace std;

int main()
{
    long long A, B, C;
    cin >> A >> B;
    cin >> C;
    
    long long result = A + B < C * 2 ? A + B : A + B - 2 * C;
    cout << result << endl;
    
    return 0;
}
