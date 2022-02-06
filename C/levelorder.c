#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct NODE {
	int data;
	struct NODE *left;
	struct NODE *right;
}NODE;

typedef struct TREE {
	NODE *data;
	struct TREE *next;
}TREE;

void getNode(NODE **p) {
	(*p) = (NODE *)malloc(sizeof(NODE));
}

void getTree(TREE **p) {
	(*p) = (TREE *)malloc(sizeof(TREE));
}

void edge(NODE *list, NODE *l, NODE *r, int data) {
	list->data = data;
	list->left = l;
	list->right = r;
}

void rootNode(NODE **list) {
	NODE *root = NULL;
	getNode(&root);
	root->left = NULL;
	root->right = NULL;
	(*list) = root;
}

void addNode(NODE **list, int data, int left, int right) {
	NODE *l = NULL, *r = NULL;
	if (left != 0) {
		getNode(&l);
		edge(l, NULL, NULL, left);
	}
	if (right != 0) {
		getNode(&r);
		edge(r, NULL, NULL, right);
	}
	edge((*list), l, r, data);
}

void id(NODE *list, int data, NODE **idlist) {
	if (list == NULL) return;
	if (list->data == data) {
		(*idlist) = list;
		return;
	}
	id(list->left, data, idlist);
	id(list->right, data, idlist);
}

void enqueue(TREE **front, TREE **rear, NODE *data) {
	TREE *tmp = NULL;
	getTree(&tmp);
	tmp->data = data;
	tmp->next = NULL;
	if ((*front) == NULL) (*front) = tmp;
	else (*rear)->next = tmp;
	(*rear) = tmp;
}

void dequeue(TREE **front, TREE **rear, NODE **data) {
	TREE *tmp = NULL;
	tmp = (*front);
	(*front) = (*front)->next;
	if ((*front) == NULL) (*rear) = NULL;
	(*data) = tmp->data;
	free(tmp);
}

void levelorder(NODE *list) {
	TREE *front = NULL, *rear = NULL;
	NODE *node = NULL;
	enqueue(&front, &rear, list);
	while (front != NULL) {
		dequeue(&front, &rear, &node);
		printf(" %d", node->data);
		if(node->left != NULL) 
			enqueue(&front, &rear, node->left);
		if(node->right != NULL) 
			enqueue(&front, &rear, node->right);
	}
}

void main() {
	NODE *root = NULL, *idnode = NULL;
	int n, data, left, right, i;
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%d %d %d", &data, &left, &right);
		if (root == NULL) {
			rootNode(&root);
			addNode(&root, data, left, right);
		}
		else {
			id(root, data, &idnode);
			addNode(&idnode, data, left, right);
		}
	}
	levelorder(root);
}
