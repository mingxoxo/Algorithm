#include <stdio.h>
#include <string.h>

typedef struct NODE{
	int data;
	struct NtoE *EdgeList;
}NODE;

typedef struct NtoE {
	int edge;
	int connectNode;
	struct NtoE *prev;
	struct NtoE *next;
}NtoE;

void getNtoE(NtoE **n) {
	(*n) = (NtoE *)malloc(sizeof(NtoE));
}

void nodeSet(NODE *str){
	int i;
	NtoE *tmp = NULL;
	for (i = 0; i < 6; i++) {
		str[i].data = i + 1;
		getNtoE(&tmp);
		tmp->edge = 0; tmp->connectNode = 0;
		tmp->prev = NULL; tmp->next = NULL;
		str[i].EdgeList = tmp;
	}
}
void add(NtoE *head, NtoE *tmp, int connectNode) {
	while (head->next != NULL) {
		if (head->next->connectNode >= connectNode) break;
		head = head->next;
	}
	tmp->next = head->next;
	tmp->prev = head;
	if(head->next != NULL) head->next->prev = tmp;
	head->next = tmp;
}

void del(NtoE *n) {
	NtoE *tmp = NULL;
	tmp = n->prev;
	if (n->next != NULL) {
		n->next->prev = tmp;
		tmp->next = n->next;
	}
	else tmp->next = NULL;
	free(n);
}

void makegraph(NODE *str, int i, int j, int k) {
	NtoE *tmp = NULL;
	getNtoE(&tmp);
	tmp->edge = k;
	tmp->connectNode = j;
	tmp->prev = NULL; tmp->next = NULL;
	add((str+i)->EdgeList, tmp, j);
}

void print(NODE node) {
	NtoE *tmp = node.EdgeList;
	tmp = tmp->next;
	while (tmp != NULL) {
		printf(" %d %d", tmp->connectNode, tmp->edge);
		tmp = tmp->next;
	}
	printf("\n");
}

NtoE *findEdge(int a, int b, NODE *str) {
	NtoE *tmp = NULL;
	tmp = str[a - 1].EdgeList->next;
	while (tmp != NULL) {
		if (tmp->connectNode == b) return tmp;
		tmp = tmp->next;
	}
	return NULL;
}
int main() {
	int i, j;
	int node, a, b, w;
	NODE str[6];
	NtoE *tmp = NULL, *tmp2 = NULL;
	char e;
	int st[8][3] = { { 1,2,1 },{ 1,3,1 },{ 1,4,1 },{ 1,6,2 },{ 2,3,1 },{ 3,5,4 },{ 5,5,4 },{ 5,6,3 } };
	nodeSet(str);
	for (i = 0; i < 8; i++) {
		makegraph(str, st[i][0] - 1, st[i][1], st[i][2]);
		if (st[i][0] != st[i][1]) //not same node
			makegraph(str, st[i][1] - 1, st[i][0], st[i][2]);
		
	}
	while (1) {
		scanf("%c", &e); getchar();
		if (e == 'a') {
			scanf("%d", &node);getchar();
			if (node <= 0 || 7 <= node) {
				printf("-1\n"); continue;
			}
			print(str[node - 1]);
		}
		else if (e == 'm') {
			scanf("%d %d %d", &a, &b, &w);getchar();
			if (a <= 0 || 7 <= a || b <= 0 || 7 <= b) {
				printf("-1\n");
				continue;
			}
			tmp = findEdge(a, b, str);
			if (tmp == NULL) {
				if (w != 0) {
					makegraph(str, a - 1, b, w);
					if (a != b) //not same node
						makegraph(str, b - 1, a, w);
				}
			}
			else {
				if (w == 0) {
					del(tmp);
					if (a != b) {//not same node
						tmp2 = findEdge(b, a, str);
						del(tmp2);
					}
				}
				else {
					tmp->connectNode = b;
					tmp->edge = w;
					if (a != b) {//not same node
						tmp2 = findEdge(b, a, str);
						tmp2->connectNode = a;
						tmp2->edge = w;
					}
				}
			}
		}
		else if (e == 'q') break;
	}
}
