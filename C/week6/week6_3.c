// 이진탐색 응용
// 사전(key-value)
// 배열 동적할당 ver
// 이진탐색 - 비재귀 ver

#include <stdlib.h>
#include <stdio.h>

int findElement(int a, int b, int n, char *info){
    int mid;

    for (int i = 0; i < n; i++)
    {
        if (a == b)
            return a;
        mid = (a + b) / 2;
        if (info[i] == 'Y')
            a = mid + 1;
        else if (info[i] == 'N')
            b = mid;
    }
    return a;
}

int main()
{
    int a, b, n, k;
    char *info = NULL;

    scanf("%d%d%d", &a, &b, &n);
    info = (char *)malloc(sizeof(char) * (n + 1));
    scanf("%s", info);

    k = findElement(a, b, n, info);
    printf("%d", k);
    return (0);
}
