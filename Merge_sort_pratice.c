#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct NODE {
	int data;
	struct NODE *next;
}NODE;

void getNode(NODE **p) {
	(*p) = (NODE *)malloc(sizeof(NODE));
}

void push(NODE **p, int n) {
	NODE *tmp = NULL;
	getNode(&tmp);
	tmp->data = n;
	tmp->next = (*p);
	(*p) = tmp;
}

int pop(NODE **p) {
	NODE *tmp = NULL;
	int a;
	tmp = (*p);
	a = tmp->data;
	(*p) = (*p)->next;
	free(tmp);
	return a;
}

int top(NODE *p) {
	return p->data;
}

void partiton(NODE *L, NODE **L1, NODE **L2, int n) {
	int i = 0;
	(*L1) = L;
	for (i = 1; i < n / 2; i++)
		L = L->next;
	(*L2) = L->next;
	L->next = NULL;
}

NODE** merge(NODE **L1, NODE **L2) {
	NODE *L = NULL;
	while ((*L1) != NULL && (*L2) != NULL) {
		if (top(*L1) <= top(*L2))
			push(&L, pop(&L1));
		else
			push(&L, pop(&L2));
	}
	while ((*L1) != NULL) 
		push(&L, pop(&L1));
	while ((*L2) != NULL)
		push(&L, pop(&L2));
	return &L;
}

void mergeSort(NODE **L, int n) {
	NODE *L1 = NULL, *L2 = NULL;
	if (n > 1) {
		partiton((*L), &L1, &L2, n);
		mergeSort(&L1, n / 2);
		mergeSort(&L2, n - (n / 2));
		(*L) = *(merge(&L1, &L2));
	}
}

void main() {
	NODE *node = NULL;
	int N = 0, data;
	int i = 0;
	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		scanf("%d", &data);
		push(&node, data);
	}
	mergeSort(&node, N);

	while (node != NULL) {
		printf(" %d", node->data);
		node = node->next;
	}
}//디버깅 
