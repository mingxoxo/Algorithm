#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct NODE {
	int data;
	struct NtoE *EdgeList;
	//struct NODE *next;
}NODE;

typedef struct EDGE {
	NODE *v1;
	NODE *v2;
	int data;
	struct EDGE *next;
}EDGE;

typedef struct NtoE {
	struct EDGE *point;
	struct NtoE *next;
}NtoE;

void getNode(NODE **node) {
	(*node) = (NODE *)malloc(sizeof(NODE));
}

void getEdge(EDGE **edge) {
	(*edge) = (EDGE *)malloc(sizeof(EDGE));
}

void getNtoE(NtoE **n) {
	(*n) = (NtoE *)malloc(sizeof(NtoE));
}

void add(NtoE *head, NtoE *tmp, int data) {
	int d;
	if(tmp->point->v1->data == data) d = tmp->point->v2->data;
	else d = tmp->point->v1->data;
	while (head->next != NULL) {
		if(head->next->point->v1->data == data){
			if(head->next->point->v2->data >= d) break;
		}
		else if(head->next->point->v2->data == data){
			if(head->next->point->v1->data >= d) break;
		}
		head = head->next;
	}
	tmp->next = head->next;
	head->next = tmp;
}

void connectNtoE(NtoE *head, EDGE *edge, int data) {
	NtoE *tmp = NULL;
	getNtoE(&tmp);
	tmp->point = edge;
	tmp->next = NULL;
	add(head, tmp, data);
}

void addEdge(EDGE **edge, int *st, NODE *str) {
	EDGE *tmp = NULL;
	EDGE *t = NULL;
	getEdge(&tmp);
	tmp->data = st[0];
	tmp->v1 = &(str[st[1] - 1]);
	tmp->v2 = &(str[st[2] - 1]);
	tmp->next = NULL;
	if ((*edge) == NULL) {
		(*edge) = tmp;
	}
	else {
		t = (*edge);
		while (t->next != NULL) t = t->next;
		t->next = tmp;
	}
}

void makeGraph(NODE *str, EDGE **edge) {
	int i;
	NtoE *tmp = NULL;
	EDGE *e = NULL;
	int st[8][3] = { { 1,1,2 },{ 1,1,3 },{ 1,1,4 },{ 2,1,6 },{ 1,2,3 },{ 4,3,5 },{ 4,5,5 },{ 3,5,6 } };
	for (i = 0; i < 6; i++) {
		str[i].data = i + 1;
		getNtoE(&tmp);
		tmp->point = NULL;
		tmp->next = NULL;
		str[i].EdgeList = tmp;
	}
	for (i = 0; i < 8; i++) {
		addEdge(edge, st[i], str);
	}
	e = (*edge);
	for (i = 0; i < 8; i++) {
		connectNtoE(e->v1->EdgeList, e, e->v1->data);
		if(st[i][1] != st[i][2])
			connectNtoE(e->v2->EdgeList, e, e->v2->data);
		e = e->next;
	}
}

void print(NODE node) {
	NtoE *tmp = node.EdgeList;
	tmp = tmp->next;
	while (tmp != NULL) {
		if(tmp->point->v1->data == node.data && tmp->point->v2->data == node.data)
			printf(" %d %d", tmp->point->v2->data, tmp->point->data);
		else if (tmp->point->v1->data == node.data) 
			printf(" %d %d", tmp->point->v2->data, tmp->point->data);
		else 
			printf(" %d %d", tmp->point->v1->data, tmp->point->data);
		tmp = tmp->next;
	}
	printf("\n");
}

EDGE *findEdge(int a, int b, NODE *str) {
	NtoE *tmp = NULL;
	EDGE *e = NULL;
	tmp = str[a - 1].EdgeList->next;
	while (tmp != NULL) {
		e = tmp->point;
		if (e ->v1->data == a) {
			if (e->v2 == NULL || e->v2->data == b )
				return e;
		}
		else if (e->v2->data == a) {
			if (e->v1->data == b)
				return e;
		}
		tmp = tmp->next;
	}
	return NULL;
}

void push(EDGE **edge, NODE *str, int a, int b, int w) {
	EDGE *tmp = NULL , *e = NULL;
	int st[3] = { w, a, b };
	addEdge(edge, st, str);
	e = (*edge);
	while (e->next != NULL)e = e->next;
	connectNtoE(e->v1->EdgeList, e, a);
	if(a != b)
		connectNtoE(e->v2->EdgeList, e, b);
}

void pop(EDGE *e, EDGE **edge, int a, int b, NODE *str) {
	EDGE *tmp = NULL;
	NtoE *tmp2 = NULL, *tmp3 = NULL;
	tmp = (*edge);
	while (tmp != NULL) {
		if (tmp == e) {
			(*edge) = tmp->next;
		}
		if (tmp->next == e) {
			tmp->next = e->next;
			break;
		}
		tmp = tmp->next;
	}
	tmp2 = e->v1->EdgeList;
	while (tmp2 ->next!= NULL) {
		if (tmp2->next->point == e) {
			tmp3 = tmp2->next;
			break;
		}
		tmp2 = tmp2->next;
	}
	tmp2->next = tmp3->next;
	free(tmp3);
	tmp2 = e->v2->EdgeList;
	if(a != b){
		while (tmp2->next != NULL) {
			if (tmp2->next->point == e) {
				tmp3 = tmp2->next;
				break;
			}
			tmp2 = tmp2->next;
		}
		tmp2->next = tmp3->next;
		free(tmp3);
	}
	free(e);
}
void main() {
	NODE str[6];
	EDGE *edge = NULL;
	EDGE *tmp = NULL;
	char e;
	int node, a, b, w;
	makeGraph(str, &edge);
	while (1) {
		scanf("%c", &e); getchar();
		if (e == 'a') {
			scanf("%d", &node);getchar();
			if (node <= 0 || 7 <= node) {
				printf("-1\n"); continue;
			}
			print(str[node-1]);
		}
		else if (e == 'm') {
			scanf("%d %d %d", &a, &b, &w);getchar();
			if (a <= 0 || 7 <= a || b <= 0 || 7 <= b) {
				printf("-1\n");
				continue;
			}
			tmp = findEdge(a, b, str);
			if (tmp == NULL) {
				if (w != 0) push(&edge, str,a, b ,w);
			}
			else {
				if (w == 0) pop(tmp, &edge, a, b, str);
				else tmp->data = w;
			}
		}
		else if (e == 'q') break;
	}
}
