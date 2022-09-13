/*
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

void insertItem(int key);
int removeMax(void);
void printHeap(void);
void downHeap(int i);
void upHeap(int i);
void swap(int i, int j);

void main(void)
{
    char input = 0;
    int key = 0;

    while (1)
    {
        scanf("%c", &input);
        if (input == 'i')
        {
            scanf("%d", &key);
            insertItem(key);
            printf("0\n");
        }
        else if(input == 'd')
			printf("%d\n", removeMax());
		else if(input == 'p')
			printHeap();
		else if(input == 'q')
			return ;
		getchar();
    }
}

void insertItem(int key)
{
    n++;
    H[n] = key;
    upHeap(n);
}

int removeMax(void)
{
    int key;

    key = H[1];
    H[1] = H[n];
    n--;
    downHeap(1);
    return (key);
}

void printHeap(void)
{
    for(int i = 1; i <= n; i++)
        printf(" %d", H[i]);
    printf("\n");
}

void upHeap(int i)
{
    int parent;
    int tmp;

    parent = i / 2;
    if (i == 1) return;
    if (H[i] < H[parent]) return;

    swap(i, parent);
    upHeap(parent);
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