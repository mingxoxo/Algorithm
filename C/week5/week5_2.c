// 퀵정렬 - 중복키 ver

/* 네델란드 국기 알고리즘 사용
https://www.techiedelight.com/ko/quicksort-using-dutch-national-flag-algorithm/
https://velog.io/@corone_hi/63.-Sort-Colors
https://www.geeksforgeeks.org/3-way-quicksort-dutch-national-flag/
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct EQUAL{
    int left;
    int right;
}EQ;

int findPivot(int l, int r);
EQ inPlacePartition(int *arr, int l, int r, int k);
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

EQ inPlacePartition(int *arr, int start, int end, int k)
{
    EQ equal;
    int mid = start;
    int pivot = arr[k];

    while (mid <= end)
    {
        if (arr[mid] < pivot){
            swap(arr, start, mid);
            start += 1;
            mid += 1;
        }
        else if (arr[mid] > pivot){
            swap(arr, end, mid);
            end -= 1;
        }
        else
            mid += 1;
    }
    equal.left = start;
    equal.right = mid - 1;
    return equal;
}

void inPlaceQuickSort(int *arr, int left, int right)
{
    int k;
    EQ equal;

    if (left >= right)
        return ;
    k = findPivot(left, right);
    equal = inPlacePartition(arr, left, right, k);
    inPlaceQuickSort(arr, left, equal.left - 1);
    inPlaceQuickSort(arr, equal.right + 1, right);
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
