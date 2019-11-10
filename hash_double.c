#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int insertion(int *root, int k, int M, int q) {
	int i = 0, hash;
	while (i < M) {
		hash = (k%M+i*(q-(k%q)))%M;
		if (root[hash] == 0) {
			root[hash] = k;
			return hash;
		}
		i++;
		printf("C");
	}
	return 0;
}

int search(int *root, int k, int M, int q) {
	int i = 0, hash;
	while (i < M) {
		hash = (k%M + i) % M;
		if (root[hash] == k) {
			return hash;
		}
		i++;
	}
	return -1;
}

int main() {
	int *root = NULL;
	int M, N, k, i, n, q;
	char e;
	scanf("%d %d %d", &M, &N, &q);
	root = (int *)malloc(sizeof(int) * M);
	for (i = 0; i < M; i++) {
		root[i] = 0;
	}
	while (1) {
		getchar();
		scanf("%c", &e);
		if (e == 'i') {
			scanf("%d", &k);
			printf("%d\n", insertion(root, k, M, q));
		}
		else if (e == 's') {
			scanf("%d", &k);
			n = search(root, k, M, q);
			printf("%d", n);
			if (n != -1) printf(" %d", root[n]);
			printf("\n");
		}
		else if (e == 'p') {
			for (i = 0; i < M; i++) {
				printf(" %d", root[i]);
			}
			printf("\n");
		}
		else if (e == 'e') {
			for (i = 0; i < M; i++) {
				printf(" %d", root[i]);
			}
			printf("\n");
			break;
		}
	}
	free(root);
	return 0;
}
