// week 3_2 재귀 ver.
/*
 * 힙 정렬
 * 1단계 : 힙 생성 - 초기 리스트로부터 최대힙 생성
 * 2단계 : 힙 정렬 - 생성된 최대힙으로부터 오름차순 정렬 수행
 * O(nlogn)
1) 순차힙구현 - 배열을 이용한 순차트리 형식으로 합을 저장
2) 최대힙 구현 - 삭제 작업 시 최대값 삭제
3) 연산 효율을 위해 배열 인덱스 0 위치는 사용하지 않고 비워둠
4) (key, elem)에서 key만 저장
5) key는 중복이 없는 1 이상의 정수로 전제
6) 공간복잡도 - O(1)
7) 힙 최대 항목 수 < 100으로 전제
*/ 

#include <stdio.h>

int H[100];
int n;

void inPlaceHeapSort();
void printArray(void); //printHeap과 동일
void rBuildHeap(int i);
void downHeap(int i, int total);
void swap(int i, int j);

int main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
        scanf("%d", H + i);
    inPlaceHeapSort();
    printArray();
    return (0);
}

void inPlaceHeapSort()
{
    rBuildHeap(1); //1단계
    for(int i = n; i >= 2; i--)
    {
        swap(1, i);
        downHeap(1, i - 1);
    }
}

void printArray(void)
{
    for(int i = 1; i <= n; i++)
        printf(" %d", H[i]);
    printf("\n");
}

void rBuildHeap(int i)
{
    if (i > n) return;
    rBuildHeap(i * 2);
    rBuildHeap(i * 2 + 1);
    downHeap(i, n);
}

void downHeap(int i, int total)
{
    int left, right;
    int greater;

    left = i * 2;
    right = i * 2 + 1;

    if (left > total) return;
    greater = left;
    if (right <= total)
    {
        if (H[greater] < H[right])
            greater = right;
    }
    
    if (H[i] >= H[greater]) return;

    swap(i, greater);
    downHeap(greater, total);
}

void swap(int i, int j)
{
    int tmp;

    tmp = H[i];
    H[i] = H[j];
    H[j] = tmp;
}
