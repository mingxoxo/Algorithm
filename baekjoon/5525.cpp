/*
IOIOI
24.06.24
문자열
https://www.acmicpc.net/problem/5525
*/

#include <iostream>
#include <string>

int main()
{
    int N, M;
    std::cin >> N;
    std::cin >> M;
    
    std::string S;
    
    std::cin >> S;
    
    int i = 0;
    int cnt = 0;
    
    while (i < M){
        int length = 0;
        if (S[i] == 'I'){
            for (int j = i + 1; j < M - 1; j += 2){
                if (S[j] == 'O' && S[j + 1] == 'I'){
                    length += 1;
                } else {
                    break;
                }
            }
            if (N <= length){
                cnt += length - N + 1;
            }
        }
        
        i += length * 2 + 1;
    }
    
    std::cout << cnt;
    return 0;
}
