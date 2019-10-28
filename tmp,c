#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct NODE {
	int key;
	struct NODE* parent;
	struct NODE* lChild;
	struct NODE* rChild;
}NODE;

void getNode(NODE **p) {
	(*p) = (NODE*)malloc(sizeof(NODE));
}

NODE* treeSearch(NODE *v, int k) {
	if (v->lChild == NULL && v->rChild == NULL) return v;
	if (k == v->key) return v;
	else if (k < v->key) treeSearch(v->lChild, k);
	else treeSearch(v->rChild, k);

}

NODE *findElement(NODE *root, int k) {
	NODE* w = NULL;
	w = treeSearch(root, k);
	if (w->lChild == NULL && w->rChild == NULL) return NULL;
	else return w;
}

void expandExternal(NODE** z) {
	NODE* l = NULL, * r = NULL;
	getNode(&l);
	getNode(&r);
	l->lChild = NULL; l->rChild = NULL; l->parent = (*z);
	r->lChild = NULL; r->rChild = NULL; r->parent = (*z);
	(*z)->lChild = l, (*z)->rChild = r;
}

void insertion(NODE *root, int k) {
	NODE* w = NULL;
	w = treeSearch(root, k);
	if (w->lChild != NULL || w->rChild != NULL) return;
	else {
		w->key = k;
		expandExternal(&w);
	}
}

void sibling(NODE* w, NODE **zs) {
	if (w->parent == NULL) return;
	if ((w->parent)->lChild = w) (*zs) = (w->parent)->rChild;
	else (*zs) = (w->parent)->lChild;
}
void inOrderSucc(NODE** w) {
	(*w) = (*w)->rChild;
	if ((*w)->lChild == NULL && (*w)->rChild == NULL) return;
	while ((*w)->lChild != NULL || (*w)->rChild != NULL)
		(*w) = (*w)->lChild;
}

void reduceExternal(NODE **root, NODE* z) {
	NODE *w = NULL, *zs = NULL, *g = NULL;
	w = z->parent; //에러
	sibling(z, &zs);
	if (w->parent == NULL) {
		(*root) = zs;
		zs->parent = NULL;
	}
	else {
		g = w->parent;
		zs->parent = g;
		if (w == g->lChild) g->lChild = zs;
		else g->rChild = zs;
	}
	free(z);
	free(w);
	printf("%d\n", zs->key);
}

void removeElement(NODE **root, int k) {
	NODE* w = NULL, *z = NULL, *y = NULL;
	w = treeSearch(*root, k);
	if (w->lChild == NULL && w->rChild == NULL) {
		printf("X"); return;
	}
	z = w->lChild;
	if (z->lChild != NULL || z->rChild != NULL) z = w->rChild;
	printf("66%d66\n" ,(z->parent)->key);
	if (z->lChild == NULL && z->rChild == NULL) reduceExternal(root, z);
	else {
		inOrderSucc(&w);
		z = w->lChild;
		reduceExternal(root, z, w);
	}

}

void preorder (NODE *root) {
	if (root->lChild == NULL && root->rChild == NULL) {
		return;
	}
	else {
		printf(" %d", root->key);
		preorder(root->lChild);
		preorder(root->rChild);
	}
}

int main() {
	NODE* root = NULL;
	char e;
	int data;
	while (1) {
		scanf("%c", &e);
		if (e == 'i') {
			scanf("%d", &data);
			if (root == NULL) {
				getNode(&root);
				root->key = data;
				expandExternal(&root);
			}
			else insertion(root, data);
		}
		else if (e == 'd') {
			scanf("%d", &data);
			removeElement(&root, data);
		}
		else if (e == 'p') {
			preorder(root);
			printf("\n");
		}
		else if (e == 'q') return 0;
	}
}
