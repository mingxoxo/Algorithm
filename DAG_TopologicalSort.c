#include <stdio.h>
#include <string.h>

typedef struct NODE {
	int index;
	char data;
	int indegree;
}NODE;

typedef struct EDGE {
	NODE *node;
	NODE *pointedNode;
}EDGE;

typedef struct TS {
	NODE *data;
	struct TS *next;
}TS;

void getNode(NODE **ver, char e, int index) {
	NODE *tmp = (NODE *)malloc(sizeof(NODE));
	tmp->data = e;
	tmp->index = index;
	tmp->indegree = 0;
	(*ver) = tmp;
}

void getEdge(EDGE* mat[][100], NODE *n1, NODE *n2) {
	int i = 0;
	EDGE *tmp = (EDGE *)malloc(sizeof(EDGE));
	tmp->node = n1;
	tmp->pointedNode = n2;
	while (mat[n1->index][i] != NULL) i++;
	mat[n1->index][i] = tmp;
	(n2->indegree)++;
}

void getTS(TS **t) {
	(*t) = (TS *)malloc(sizeof(TS));
}

NODE *findNode(NODE **ver, char e, int n) {
	for (int i = 0; i < n; i++) {
		if (ver[i]->data == e) return ver[i];
	}
}

void buildGraph(NODE **ver, EDGE* mat[][100], int *n, int *m) {
	int i, j;
	char e, n1, n2;
	NODE *tmp1, *tmp2;
	scanf("%d", n);
	for (i = 0; i < (*n); i++) {
		for (j = 0; j < (*n); j++) {
			mat[i][j] = NULL;
		}
	}
	for (i = 0; i < (*n); i++) {
		getchar();
		scanf("%c", &e);
		getNode(ver + i, e, i);
	}
	scanf("%d", m);
	for (i = 0; i < (*m); i++) {
		getchar();
		scanf("%c %c", &n1, &n2);
		tmp1 = findNode(ver, n1, *n);
		tmp2 = findNode(ver, n2, *n);
		getEdge(mat, tmp1, tmp2);
	}
}

void enqueue(TS **front, TS **rear, TS *v) {
	TS *tmp = NULL;
	getTS(&tmp);
	tmp->data = v;
	tmp->next = NULL;
	if ((*front) == NULL) (*front) = tmp;
	else (*rear)->next = tmp;
	(*rear) = tmp;
}

NODE *dequeue(TS **front, TS **rear) {
	TS *tmp = NULL;
	NODE *data = (*front)->data;
	tmp = (*front);
	(*front) = (*front)->next;
	if ((*front) == NULL) (*rear) = NULL;
	free(tmp);
	return data;
}

void topologicalSort(int *topSort, int n, NODE **ver, EDGE* mat[][100]) {
	int i, t = 1;
	TS *front = NULL, *rear = NULL;
	NODE *tmp = NULL;
	for (i = 0; i < n; i++) {
		if (ver[i]->indegree == 0) enqueue(&front, &rear, ver[i]);
	}
	while (front != NULL) {
		tmp = dequeue(&front, &rear);
		topSort[t] = tmp->data;
		t++;
		for (i = n-1; i >= 0 ; i--) {
			if (mat[tmp->index][i] == NULL) {
				continue;
			}
			if (--(mat[tmp->index][i]->pointedNode->indegree) == 0) {
				enqueue(&front, &rear, mat[tmp->index][i]->pointedNode);
			}
		}
	}
	if (t <= n) topSort[0] = 0;
	else topSort[0] = 1;
}

int main() {
	int n, m, i, j;
	char e, n1, n2;
	NODE *ver[100];
	EDGE* mat[1000][1000];
	
	buildGraph(ver, mat, &n, &m);
	int *topSort = (int *)malloc(sizeof(int) * (n + 1));
	
	topologicalSort(topSort, n, ver, mat);
	if (topSort[0] == 0) printf("0\n");
	else {
		for (i = 1; i <= n; i++) printf("%c ", topSort[i]);
	}
}
