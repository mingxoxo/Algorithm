/*
NN
24.06.25
https://www.acmicpc.net/problem/11944
*/

#include <iostream>
#include <string>

int main()
{
    int N, M, cnt;
    std::cin >> N >> M;
    
    std::string str = std::to_string(N);
    cnt = str.length() * N;
    if (M < cnt){
        cnt = M;
    }
    
    for (int i = 0; i < cnt; i++){
        std::cout << str[i % str.length()];
    }
    return 0;
}
