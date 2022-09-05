// 자료구조 복습
// 연결이진트리를 활용한 트리 탐색 구현
// 무조건 선위순회 순서로 노트의 정보가 주어짐

#include <stdio.h>
#include <stdlib.h>

typedef struct TREE
{
    int         data;
    struct TREE *left;
    struct TREE *right;
}TREE;


TREE *make_new_node(int data)
{
    TREE *node = NULL;
    
    node = (TREE *)malloc(sizeof(TREE));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return (node);
}

void    find_id_node(TREE *node, int data, TREE **id_node)
{
    if (node == NULL)
        return ;
    if (node->data == data)
    {
        *id_node = node;
        return ;
    }
    find_id_node(node->left, data, id_node);
    find_id_node(node->right, data, id_node);
}

void    connect_edge_node(TREE *id_node, int left, int right)
{
    id_node->left = make_new_node(left);
    id_node->right = make_new_node(right);
}

void    search_node(TREE *node, char *str)
{
    while (*str)
    {
        printf(" %d", node->data);
        if (*str == 'L')
            node = node->left;
        else if (*str == 'R')
            node = node->right;
        str++;
    }
    printf(" %d\n", node->data);
}

int main()
{
    int N, s, data, left, right;
    char str[101];
    TREE *root = NULL, *id_node = NULL;
    
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d%d%d", &data, &left, &right);
        if (root == NULL)
        {
            root = make_new_node(data);
        }
        find_id_node(root, data, &id_node);
        connect_edge_node(id_node, left, right);
    }
    scanf("%d", &s);
    for (int i = 0; i < s; i++)
    {
        getchar();
        scanf("%s", str);
        search_node(root, str);
    }
    return 0;
}
