/* 개방주소법 해시테이블 – 이중 해싱
- 해시테이블은 크기가 M인 배열로 동적 할당한다(종료 시 해제).
- n은 M보다 작은 자연수로 최대 삽입 개수다. 
- 입력 키는 중복이 없는 2자리 이상의 자연수다. 
- 키 x에 대한 첫 번째 해시함수 h(x) = x % M, 두 번째 해시함수 h‘(x) = q – (x % q) 를 사용한다. q는 M보다 조금 작은 소수로 입력으로 주어진다.
- 저장된 키가 없는 빈 버켓은 0으로 처리한다. 
*/

#include <stdio.h>
#include <stdlib.h>

int insertion(int *root, int k, int M, int q) {
	int hash;
	for (int i = 0; i < M; i++){
		hash = (k % M + i * (q - (k % q))) % M;
		if (root[hash] == 0) {
			root[hash] = k;
			return hash;
		}
		printf("C");
	}
	return 0;
}

int search(int *root, int k, int M, int q) {
	int hash;
	for (int i = 0; i < M; i++){
		hash = (k % M + i * (q - (k % q))) % M;
		if (root[hash] == k)
            return hash;
	}
	return -1;
}

void print_hash(int *hash, int M){
	for (int i = 0; i < M; i++){
		printf(" %d", hash[i]);
	}
	printf("\n");
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
			if (n != -1) 
                printf(" %d", root[n]);
			printf("\n");
		}
		else if (e == 'p')
			print_hash(root, M);
		else if (e == 'e') {
			print_hash(root, M);
			break;
		}
	}
	free(root);
	return 0;
}