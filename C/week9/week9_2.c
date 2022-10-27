/* 개방주소법 해시테이블 – 선형조사법
- 해시테이블은 크기가 M인 배열로 동적 할당한다.
- n은 M보다 작은 자연수로 최대 삽입 개수다.
- 입력 키는 중복이 없는 6자리 또는 8자리의 임의의 자연수(학번)다.
- 키 x에 대한 해시함수 h(x) = x % M 을 사용한다. 
- 저장된 키 값이 없는 빈 버켓은 0으로 처리한다. 
*/

#include <stdio.h>
#include <stdlib.h>

int insertion(int *root, int k, int M) {
	int hash;
	for (int i = 0; i < M; i++){
		hash = (k % M + i) % M;
		if (root[hash] == 0) {
			root[hash] = k;
			return hash;
		}
		printf("C");
	}
	return 0;
}

int search(int *root, int k, int M) {
	int hash;
	for (int i = 0; i < M; i++){
		hash = (k % M + i) % M;
		if (root[hash] == k)
            return hash;
	}
	return -1;
}

int main() {
	int *root = NULL;
	int M, N, k, i, n;
	char e;
	scanf("%d %d", &M, &N);
	root = (int *)malloc(sizeof(int) * M);
	for (i = 0; i < M; i++) {
		root[i] = 0;
	}
	while (1) {
		getchar();
		scanf("%c", &e);
		if (e == 'i') {
			scanf("%d", &k);
			printf("%d\n", insertion(root, k, M));
		}
		else if (e == 's') {
			scanf("%d", &k);
			n = search(root, k, M);
			printf("%d", n);
			if (n != -1) 
                printf(" %d", root[n]);
			printf("\n");
		}
		else if (e == 'e') {
			break;
		}
	}
	free(root);
	return 0;
}