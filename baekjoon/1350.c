// 진짜 공간
// 24.07.18
// https://www.acmicpc.net/problem/1350

#include <stdio.h>

int main(void) {

    int N, clusterSize;
    long clusterCount = 0;
    int fileSizeArr[50] = {0,};

    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        scanf("%d", fileSizeArr + i);
    }
    scanf("%d", &clusterSize);

    for (int i = 0; i < N; i++){
        clusterCount += fileSizeArr[i] / clusterSize + (int)(fileSizeArr[i] % clusterSize != 0);
    }
    
    printf("%ld", clusterCount * clusterSize);

    return 0;
}
