#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct NODE {
	int key;
	struct NODE *next;
}NODE;

void getNode(NODE **p) {
	(*p) = (NODE *)malloc(sizeof(NODE));
}

void insertion(NODE *node, int k) {
	NODE *tmp = NULL;
	getNode(&tmp);
	tmp->key = k;
	tmp->next = node->next;
	node->next = tmp;
}

int find(NODE *node, int k) {
	int i = 1;
	while (node != NULL) {
		if (node->key == k) {
			return i;
		}
		else {
			i++;
			node = node->next;
		}
	}
	return 0;
}

int del(NODE *node, int k) {
	int i = 1;
	NODE *tmp = NULL;
	while (node ->next != NULL) {
		if ((node->next)->key == k) {
			tmp = node->next;
			node->next = tmp->next;
			free(tmp);
			return i;
		}
		else {
			i++;
			node = node->next;
		}
	}
	return 0;
}

void print(NODE *root, int M) {
	int i;
	NODE *tmp = NULL;
	for (i = 0; i < M; i++) {
		if (root[i].next != NULL) {
			tmp = root[i].next;
			while (tmp != NULL) {
				printf(" %d", tmp->key);
				tmp = tmp->next;
			}
			
		}
	}
	printf("\n");
}
int main() {
	NODE *root = NULL;
	int M, k, i;
	char e;
	scanf("%d", &M);
	root = (NODE *)malloc(sizeof(NODE) * M);
	for (i = 0; i < M; i++) {
		root[i].key = 0;
		root[i].next = NULL;
	}
	while (1) {
		getchar();
		scanf("%c", &e);
		if (e == 'i') {
			scanf("%d", &k);
			insertion((root + (k%M)), k);
		}
		else if (e == 's') {
			scanf("%d", &k);
			printf("%d\n", find(root[k%M].next, k));
		}
		else if (e == 'd') {
			scanf("%d", &k);
			printf("%d\n", del(root+(k%M), k));
		}
		else if (e == 'p') {
			print(root, M);
		}
		else if (e == 'e') {
			break;
		}
	}
	free(root);
	return 0;
}
