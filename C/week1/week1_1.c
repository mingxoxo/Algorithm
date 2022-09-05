// 자료구조 복습
// 이중연결리스트를 이용하여 영문자 리스트 ADT 구현

#include <stdio.h>
#include <stdlib.h>

typedef struct NODE
{
    char elem;
    struct NODE *prev;
    struct NODE *next;
}NODE;

typedef struct LIST
{
    struct NODE *head;
    struct NODE *tail;
    int         size;
}LIST;

NODE *make_new_node()
{
    NODE *new = NULL;
    
    new = (NODE *)malloc(sizeof(NODE));
    return (new);
}

void init_node(LIST *list)
{
    NODE *head = NULL, *tail = NULL;

    head = make_new_node();
    tail = make_new_node();

    head->elem = 0;
    tail->elem = 0;

    head->prev = NULL;
    head->next = tail;

    tail->prev = head;
    tail->next = NULL;

    list->head = head;
    list->tail = tail;
    list->size = 0;
}

NODE *get_rank_node(NODE *list, int r)
{
    int i = 0;

    while (i < r)
    {
        list = list->next;
        i++;
    }
    return (list);
}

void add(LIST *list, int r, char e)
{
    NODE *node = NULL;
    NODE *new = NULL;

    if (!(0 < r && r <= list->size + 1))
    {
        printf("invalid position\n");
        return ;
    }
    node = get_rank_node(list->head, r);
    new = make_new_node();

    new->elem = e;
    new->prev = node->prev;
    new->next = node;

    node->prev->next = new;
    node->prev = new;

    list->size += 1;
}

void delete(LIST *list, int r)
{ 
    NODE *node = NULL;

    if (!(0 < r && r <= list->size))
    {
        printf("invalid position\n");
        return ;
    }
    node = get_rank_node(list->head, r);

    node->prev->next = node->next;
    node->next->prev = node->prev;

    list->size -= 1;

    free(node);
}

void get(LIST *list, int r)
{
    NODE *node = NULL;

    if (!(0 < r && r <= list->size))
    {
        printf("invalid position\n");
        return ;
    }
    node = get_rank_node(list->head, r);
    printf("%c\n", node->elem);
}

void print(LIST *list)
{
    NODE *node = list->head->next;

    while (node->next)
    {
        printf("%c", node->elem);
        node = node->next;
    }
    printf("\n");
}

int main()
{
    int N, r;
    char op, e;
    LIST *list;
    
    list = (LIST *)malloc(sizeof(LIST));
    init_node(list);
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        getchar();
        scanf("%c", &op);
        if (op == 'A')
        {
            scanf("%d %c", &r, &e);
            add(list, r, e);
        }
        else if (op == 'D') {
			scanf("%d", &r); 
			delete(list, r);
		}
		else if (op == 'G') {
			scanf("%d", &r); 
			get(list, r);
		}
		else if (op == 'P') {
			print(list);
		}
    }
    free(list);
    return (0);
}
