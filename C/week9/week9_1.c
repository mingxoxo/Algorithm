/* 분리연쇄법 해시테이블

키 x에 대한 해시함수 h(x) = x % M 을 사용
삽입 시 충돌이 발생하는 경우, 해당 버켓 리스트의 맨 앞에 삽입
탐색 또는 삭제할 때,
1. 키가 존재하면 리스트에서 해당 키가 저장된 순위(1부터 시작)를 인쇄
2. 없다면 0을 인쇄
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int key;
    struct Node *next;
}NODE;


NODE **initBucketArray(int M);
NODE *getNode(int x);
void insertItem(NODE *ht[], int x, int M);
int removeElement(NODE *ht[], int x, int M);
int findElement(NODE *ht[], int x, int M);
void printElemnet(NODE *ht[], int M);


int main(void)
{
    char cmd;
    int M, x;
    NODE **ht = NULL; //hash table

    scanf("%d", &M); 
    ht = initBucketArray(M);
    while (1){
        getchar();
        scanf("%c", &cmd); 
        
        if (cmd == 'i'){
            scanf("%d", &x);
            insertItem(ht, x, M);
        }
        else if (cmd == 'd'){
            scanf("%d", &x); 
            printf("%d\n", removeElement(ht, x, M));
        }
        else if (cmd == 's'){
            scanf("%d", &x); 
            printf("%d\n", findElement(ht, x, M));
        }
        else if (cmd == 'p')
            printElemnet(ht, M);
        else if (cmd == 'e')
            break;
    }
    return 0;
}

NODE **initBucketArray(int M){
    NODE **ht = NULL; 

    ht = (NODE **)malloc(sizeof(NODE *) * M);
    for (int i = 0; i < M; i++)
        ht[i] = NULL;
    return ht;
}

NODE *getNode(int x){
    NODE *new = NULL;

    new = (NODE *)malloc(sizeof(NODE));
    new->key = x;
    new->next = NULL;
    return new;
}

void insertItem(NODE *ht[], int x, int M){
    NODE *new = NULL;
    int hx = x % M;

    new = getNode(x);
    new->next = ht[hx];
    ht[hx] = new;
}

int removeElement(NODE *ht[], int x, int M){
    int cnt = 0;
    int hx = x % M;
    NODE *node = ht[hx], *prev = NULL;

    while (node)
    {
        cnt += 1;
        if (node->key == x)
        {
            if (cnt == 1)
                ht[hx] = node->next;
            else
                prev->next = node->next;
            free(node);
            return cnt;
        }
        prev = node;
        node = node->next;
    }
    return 0;
}

int findElement(NODE *ht[], int x, int M){
    int cnt = 0;
    NODE *node = ht[x % M];

    while (node)
    {
        cnt += 1;
        if (node->key == x)
            return cnt;
        node = node->next;
    }
    return 0;
}

void printElemnet(NODE *ht[], int M){
    NODE *node = NULL;

    for (int i = 0; i < M; i++)
    {
        node = ht[i];
        while (node){
            printf(" %d", node->key);
            node = node->next;
        }
    }
    printf("\n");
}
