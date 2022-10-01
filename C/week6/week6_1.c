// 사전(key-value)
// 배열 동적할당 ver
// 이진탐색 - 재귀 ver

#include <stdio.h>
#include <stdlib.h>

int *init_dict(int n){
    int *dict = NULL;

    dict = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
        scanf("%d", dict + i);
    return dict;
}

int rFindElement(int *dict, int k, int l, int r){
    int mid;

    if (l > r)
        return r;
    mid = (l + r)/2;
    if (dict[mid] == k)
        return mid;
    else if (dict[mid] > k)
        return rFindElement(dict, k, l, mid - 1);
    else
        return rFindElement(dict, k, mid + 1, r);
}

int main(){
    int n = 0, k = 0, index = 0;
    int *dict = NULL;

    scanf("%d%d", &n, &k);
    dict = init_dict(n);
    index = rFindElement(dict, k, 0, n - 1);
    printf(" %d", index);
    free(dict);
    return (0);
}
