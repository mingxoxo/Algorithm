#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct NODE {
	int data;
	int rank; //rank를 배열의 index의 느낌으로 사용
	struct NODE *prev;
	struct NODE *next;
}NODE;

void getNode(NODE **p) {
	(*p) = (NODE *)malloc(sizeof(NODE));
}

void push(NODE **p, int n, int i) {
	NODE *tmp = NULL, *tmp2 = (*p);
	getNode(&tmp);
	tmp->data = n;
	tmp->rank = i; //index 추가
	tmp->next = NULL;
	if ((*p) == NULL) {
		tmp->prev = NULL;
		(*p) = tmp;
		return;
	}
	while (tmp2->next != NULL && tmp2 != NULL) {
		tmp2 = tmp2->next;
	}
	tmp->prev = tmp2;
	tmp2->next = tmp;
}


void inPlacePartiton(NODE *l, NODE *r, NODE *k, NODE **L, NODE **R) {
	int p, tmp;
	NODE *ltmp = l, *rtmp = r->prev;
  //pivot과 노드 마지막 값을 교체
	p = k->data;
	k->data = r->data;
	r->data = p;
	while (ltmp->rank <= rtmp->rank && rtmp->prev != NULL && ltmp->next != NULL) {
		while (ltmp->rank <= rtmp->rank && ltmp->data <= p && ltmp->next != NULL) ltmp = ltmp->next;
		while (ltmp->rank <= rtmp->rank && rtmp->data >= p && rtmp->prev != NULL) rtmp = rtmp->prev;
		if (ltmp->rank < rtmp->rank) {
			tmp = ltmp->data;
			ltmp->data = rtmp->data;
			rtmp->data = tmp;
		}
	}
  //정렬된 것을 바탕으로 pivot을 위치시켜주고 pivot자리에 있는 값은 마지막으로 보내주기
	tmp = ltmp->data;
	ltmp->data = r->data;
	r->data = tmp;
	(*R) = rtmp;
	(*L) = ltmp;
}

void inPlaceQuickSort(NODE *l, NODE *r) {
	int intk, i;
	NODE *k = l;
	NODE *L = NULL, *R = NULL;
	if (l->rank >= r->rank) return;
	intk = (r->rank - l->rank) / 2; //pivot rank구하기
	if (intk == 0) intk = 1; //예외처리
	for (i = 0; i < intk; i++) k = k->next; //pivot NODE 구하기
	inPlacePartiton(l, r, k , &L, &R);
	if (L->prev != NULL) L = L->prev;
	if (R->next != NULL) R = R->next;
	inPlaceQuickSort(l, L); //첫 노드부터 pivot 기준 전 노드까지 quicksort
	inPlaceQuickSort(R, r); // pivot 노드부터 마지막 노드까지 quicksort
}

void main() {
	NODE *node = NULL, *r = NULL;
	int N = 0, data;
	int i = 0;
	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		scanf("%d", &data);
		push(&node, data, i + 1);
	}
	r = node;
	while (r->next != NULL) r = r->next;

	inPlaceQuickSort(node, r);

	while (node != NULL) {
		printf(" %d", node->data);
		node = node->next;
	}
}
