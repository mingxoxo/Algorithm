// 퀵 정렬 - 유일키 ver

#include <stdio.h>
#include <stdlib.h>

int findPivot(int l, int r);
int inPlacePartition(int *arr, int l, int r, int k);
void inPlaceQuickSort(int *arr, int left, int right);
void swap(int *arr, int i, int j);
void printArray(int *arr, int n);

int main()
{
    int n = 0;
    int *arr = NULL;

    scanf("%d", &n);
    arr = (int *)malloc(sizeof(int) * n);
    for(int i = 0; i < n; i++)
        scanf("%d", arr + i);
    inPlaceQuickSort(arr, 0, n-1);
    printArray(arr, n);
    return (0);
}

int findPivot(int l, int r)
{
    return rand()%(r - l + 1) + l;
}

int inPlacePartition(int *arr, int l, int r, int k)
{
    int i = 0, j = 0, pivot = 0;

    pivot = arr[k];
    swap(arr, k, r);
    i = l;
    j = r - 1;

    while (i <= j)
    {
        while (i <= j && arr[i] <= pivot){
            i++;
        }
        while (i <= j && arr[j] >= pivot){
            j--;
        }
        if (i < j)
            swap(arr, i, j);
    }
    swap(arr, i, r);
    return i;
}

void inPlaceQuickSort(int *arr, int left, int right)
{
    int k;
    int eq;

    if (left >= right)
        return ;
    k = findPivot(left, right);
    eq = inPlacePartition(arr, left, right, k);
    inPlaceQuickSort(arr, left, eq - 1);
    inPlaceQuickSort(arr, eq + 1, right);
}

void printArray(int *arr, int n)
{
    for(int i = 0; i < n; i++)
        printf(" %d", arr[i]);
    printf("\n");
}

void swap(int *arr, int i, int j)
{
    int tmp;

    tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}
