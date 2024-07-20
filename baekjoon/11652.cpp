// 카드
// 24.07.20
// 해시, 정렬
// https://www.acmicpc.net/problem/11652

#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main(void) {

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    string numberCard;
    unordered_map<string, int> cardCntMap;

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> numberCard;

        auto it = cardCntMap.find(numberCard);
        if (it != cardCntMap.end()){
            it->second += 1;
        } else {
            cardCntMap[numberCard] = 1;
        }
    }
    
    long long maxNumberCardKey = 0;
    int maxCnt = 0;

    for (const auto& pair : cardCntMap){
        if (pair.second < maxCnt) continue;

        long long key = stoll(pair.first);
        if (pair.second == maxCnt and maxNumberCardKey < key)
            continue;
        
        maxNumberCardKey = key;
        maxCnt = pair.second;
    }

    cout << maxNumberCardKey;

    return 0;
}
