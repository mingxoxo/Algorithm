// 사전(key-value)
// 배열 동적할당 ver
// 이진탐색 - 비재귀 ver

#include <stdio.h>
#include <stdlib.h>

int *init_dict(int n){
    int *dict = NULL;

    dict = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
        scanf("%d", dict + i);
    return dict;
}

int findElement(int *dict, int k, int n){
    int l = 0, r = n - 1;
    int mid;

    while (l <= r)
    {
        mid = (l + r)/2;
        if (dict[mid] == k)
            return mid;
        else if (dict[mid] < k)
            l = mid + 1;
        else
            r = mid - 1;
    }
    return l;
}

int main(){
    int n = 0, k = 0, index = 0;
    int *dict = NULL;

    scanf("%d%d", &n, &k);
    dict = init_dict(n);
    index = findElement(dict, k, n);
    printf(" %d", index);
    free(dict);
    return (0);
}
