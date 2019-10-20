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

void addLast(NODE **p, int data) {
	NODE *tmp = NULL, *tmp2 = (*p);
	getNode(&tmp);
	tmp->data = data;
	tmp->next = NULL;
	if ((*p) == NULL) (*p) = tmp;
	else {
		while (tmp2->next != NULL) 
			tmp2 = tmp2->next;
		tmp2->next = tmp;
	}
}

int removeFirst(NODE **p) {
	NODE *tmp = NULL;
	int data;
	tmp = (*p);
	data = tmp->data;
	(*p) = (*p)->next;
	free(tmp);
	return data;
}

void partition(NODE *p, NODE **L1, NODE **L2, int n) {
	int i;
	(*L1) = p;
	for (i = 1; i < n / 2; i++) {
		p = p->next;
	}
	(*L2) = p->next;
	p->next = NULL;
}

NODE **merge(NODE **L1, NODE **L2) {
	NODE *p = NULL;
	while ((*L1) != NULL && (*L2) != NULL) {
		if ((*L1)->data > (*L2)->data) {
			addLast(&p, removeFirst(L2));
		}
		else if ((*L1)->data < (*L2)->data) {
			addLast(&p, removeFirst(L1));
		}
	}
	while ((*L1) != NULL) {
		addLast(&p, removeFirst(L1));
	}
	while ((*L2) != NULL) {
		addLast(&p, removeFirst(L2));
	}
	return &p;
}

void mergeSort(NODE **p, int n) {
	NODE *L1 = NULL, *L2 = NULL;
	if (n <= 1) return;
	partition(*p, &L1, &L2, n);
	mergeSort(&L1, n / 2);
	mergeSort(&L2, n - n / 2);
	(*p) = *(merge(&L1, &L2));
}

void main() {
	int n, i, data;
	NODE *node = NULL;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &data);
		addLast(&node, data);
	}
	mergeSort(&node, n);
	while (node != NULL) {
		printf(" %d", node->data);
		node = node->next;
	}
}
