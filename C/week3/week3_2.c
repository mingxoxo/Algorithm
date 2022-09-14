/*
 * 상향식 힙 생성
1) 키가 한꺼번에 주어짐 - 차례로 초기 배열에 저장
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

void rBuildHeap(int i);
void downHeap(int i);
void swap(int i, int j);
void printHeap(void);

int main(void)
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
        scanf("%d", H + i);
    rBuildHeap(1);
    printHeap();
    return (0);
}

void rBuildHeap(int i)
{
    if (i > n) return;
    rBuildHeap(i * 2);
    rBuildHeap(i * 2 + 1);
    downHeap(i);
}

void downHeap(int i)
{
    int left, right;
    int greater;

    left = i * 2;
    right = i * 2 + 1;

    if (left > n) return;
    greater = left;
    if (right <= n)
    {
        if (H[greater] < H[right])
            greater = right;
    }
    
    if (H[i] >= H[greater]) return;

    swap(i, greater);
    downHeap(greater);
}

void swap(int i, int j)
{
    int tmp;

    tmp = H[i];
    H[i] = H[j];
    H[j] = tmp;
}

void printHeap(void)
{
    for(int i = 1; i <= n; i++)
        printf(" %d", H[i]);
    printf("\n");
}