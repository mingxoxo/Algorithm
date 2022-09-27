#include <stdio.h>
#include <stdlib.h>


typedef struct NODE
{
    int         data;
    struct NODE *next;
}NODE;

typedef struct LIST
{
    struct NODE *head;
    int         size;
}LIST;

LIST *init_list(NODE *head, int n);
NODE *make_new_node(int data);

void push(LIST **L, int data);
int pop(LIST **L);
int top(LIST *L);

LIST *partition_list(LIST *L, LIST **L2, int k);
LIST *merge(LIST *L1, LIST *L2);
LIST *mergeSort(LIST *L);


int main()
{
    int n = 0, data = 0;
    LIST *L = NULL;
    NODE *tmp = NULL;
    
    scanf("%d", &n);
    L = init_list(NULL, 0);
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &data);
        push(&L, data);
    }
    L = mergeSort(L);
    print_node(L);
    return (0);
}

LIST *init_list(NODE *head, int n)
{
    LIST *L = NULL;

    L = (LIST *)malloc(sizeof(LIST));
    L->head = head;
    L->size = n;
    return (L);
}

NODE *make_new_node(int data)
{
    NODE *new = NULL;
    new = (NODE *)malloc(sizeof(NODE));
    new->data = data;
    new->next = NULL;
    return (new);
}

void push(LIST **L, int data)
{
    NODE *new = NULL;
    NODE *last_node = NULL;

    new = make_new_node(data);
    (*L)->size += 1;
    if ((*L)->head == NULL){
        (*L)->head = new;
        return ;
    }
    last_node = (*L)->head;
    while (last_node->next)
        last_node = last_node->next;
    last_node->next = new;
}

int pop(LIST **L)
{
    int data;
	NODE *d_node = NULL;
	
    (*L)->size -= 1;
    d_node = (*L)->head;
    data = (*L)->head->data;
	(*L)->head = (*L)->head->next;
	free(d_node);
	return data;
}

int top(LIST *L)
{
	return L->head->data;
}

LIST *partition_list(LIST *L, LIST **L2, int k)
{
    NODE *node = L->head;

    for (int i = 1; i < k ; i++)
        node = node->next;
    *L2 = init_list(node->next, L->size - k);

    node->next = NULL;
    L->size = k;

    return L;
}

LIST *merge(LIST *L1, LIST *L2)
{
	LIST *L = NULL;
    NODE *tmp = NULL;

    L = init_list(NULL, 0);
	while (L1->head && L2->head) {
		if (top(L1) <= top(L2))
			push(&L, pop(&L1));
		else
			push(&L, pop(&L2));
	}
	while (L1->head)
		push(&L, pop(&L1));
	while (L2->head)
		push(&L, pop(&L2));
    free(L1);
    free(L2);
	return L;
}

LIST *mergeSort(LIST *L)
{
    LIST *L1 = NULL;
    LIST *L2 = NULL;

    if (L->size > 1)
    {
        L1 = partition_list(L, &L2, (L->size)/2);
        L1 = mergeSort(L1);
        L2 = mergeSort(L2);
        L = merge(L1, L2);
    }
    return L;
}

void print_node(LIST *L)
{
    NODE *node = L->head;

    while (node)
    {
        printf(" %d", node->data);
        node = node->next;
    }
    printf("\n");
}
