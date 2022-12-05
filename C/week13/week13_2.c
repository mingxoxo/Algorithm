// 최소신장트리
// Kruskal
// 인접행렬 버전
// sack number로 sack이 구분되었다고 가정

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

# define NONE -1

typedef struct NODE {
	int data;
	int sack;
	int distance;
}NODE;

typedef struct EDGE {
	int weight;
	NODE *node;
	NODE *pointedNode;
}EDGE;

typedef struct Queue {
	EDGE *data;
	struct Queue *prev;
	struct Queue *next;
}Q;

typedef struct Tree{
	int size;
	int weight;
}T;

void getQ(Q **t) {
	(*t) = (Q *)malloc(sizeof(Q));
}

void getNode(NODE **ver, int data) {
	NODE *tmp = (NODE *)malloc(sizeof(NODE));
	tmp->data = data;
	tmp->sack = -1;
	tmp->distance = -1;
	(*ver) = tmp;
}

void getEdge(EDGE* mat[][100], NODE *n1, NODE *n2, int w) {
	EDGE *tmp = (EDGE *)malloc(sizeof(EDGE));
	tmp->weight = w;
	tmp->node = n1;
	tmp->pointedNode = n2;
	mat[n1->data - 1][n2->data - 1] = tmp;
}

NODE *findNode(NODE **ver, int data, int n) {
	for (int i = 0; i < n; i++) {
		if (ver[i]->data == data) return ver[i];
	}
	return NULL;
}

void buildGraph(NODE **ver, EDGE* mat[][100], int *n, int *m) {
	int i, j;
	int n1, n2, w;
	NODE *v1, *v2;
	scanf("%d %d", n, m);
    
    //EDGE init
	for (i = 0; i < (*n); i++) {
		for (j = 0; j < (*n); j++) {
			mat[i][j] = NULL;
		}
	}
    //NODE init(0번째에 1번 저장)
	for (i = 0; i < (*n); i++) {
		getNode(ver + i, i + 1);
	}

    //ver1, ver2, weight input
	for (i = 0; i < (*m); i++) {
		scanf("%d %d %d", &n1, &n2, &w);
		v1 = findNode(ver, n1, *n);
		v2 = findNode(ver, n2, *n);
		getEdge(mat, v1, v2, w);
		getEdge(mat, v2, v1, w);
	}
}

void enqueue(Q **front, Q **rear, EDGE *edge) {
	Q *tmp = NULL;
	getQ(&tmp);
	tmp->data = edge;
	tmp->next = NULL;
	if ((*front) == NULL) {
		(*front) = tmp;
		tmp->prev = NULL;
	}
	else {
		(*rear)->next = tmp;
		tmp->prev = (*rear);
	}
	(*rear) = tmp;
}

EDGE *removeMin(Q **front, Q **rear) {
	Q *min = (*front), *tmp = (*front)->next;
	EDGE *m = NULL;
	while (tmp != NULL) {
		if (tmp->data->weight < min->data->weight) {
			min = tmp;
		}
		tmp = tmp->next;
	}
	if (min->next != NULL) min->next->prev = min->prev;
	else (*rear) = (*rear)->prev;
	if (min->prev != NULL) min->prev->next = min->next;
	else (*front) = (*front)->next;
	m = min->data;
	free(min);
	return m;
}

int KruskalMST(NODE **ver, EDGE* mat[][100], int n) {
	EDGE *minEdge = NULL;
	Q *front = NULL, *rear = NULL;
	T mst;
	int sack_number;

	// sack init
	for (int i = 0; i < n; i++){
		ver[i]->sack = i + 1;
	}

	// queue init
	for (int i = 0; i < n; i++){
		for (int j = i; j < n; j++){
			if (mat[i][j] == NULL)
				continue;
			enqueue(&front, &rear, mat[i][j]);
		}
	}
	// //T init
	mst.size = 0;
	mst.weight = 0;

	while (mst.size < n - 1){
		minEdge = removeMin(&front, &rear);
		if (minEdge->node->sack == minEdge->pointedNode->sack)
			continue;
		mst.size++;
		printf(" %d", minEdge->weight);
		mst.weight += minEdge->weight;
		sack_number = minEdge->pointedNode->sack;
		for (int i = 0; i < n; i++){
			if (ver[i]->sack == sack_number)
				ver[i]->sack = minEdge->node->sack;
		}
	}
	return mst.weight;
}

int main() {
	int n, m, i, j, total_weight = 0;
	NODE *ver[100];
	EDGE* mat[100][100];

	buildGraph(ver, mat, &n, &m);
	total_weight = KruskalMST(ver, mat, n);
	printf("\n%d", total_weight);
}
