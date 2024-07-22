// Fly me to the Alpha Centauri
// 24.07.22
// 수학
// https://www.acmicpc.net/problem/1011

#include <iostream>

using namespace std;

int minimumJumpsToTarget(int start, int target) {
    int result = 0;
    int stepNumber = 1;
    int changeFlag = 0;

    int totalDistance = target - start;
    while (0 < totalDistance) {
        totalDistance -= stepNumber;
        result++;
        stepNumber += changeFlag;
        changeFlag = (changeFlag + 1) % 2;
    }

    return result;
}

int main(void) {

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T, x, y;

    cin >> T;
    for (int i = 0; i < T; i++){
        cin >> x >> y;
        cout << minimumJumpsToTarget(x, y) << "\n";
    }
    
    return 0;
}
