// 완전제곱수
// https://www.acmicpc.net/problem/1977

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int M, N;
    
    cin >> M;
    cin >> N;
    
    int start = ceil(sqrt(M));
    int end = floor(sqrt(N));
    
    if (end < start) {
        cout << -1;
        return 0;
    }
    
    long long sum = 0;
    for (int i = start; i <= end; i++){
        sum += pow(i, 2);
    }
    
    cout << sum << endl;
    cout << pow(start, 2) << endl;

    return 0;
}
