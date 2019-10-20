#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void inplaceInsertionSort(int *arr, int n) {
	int i, j, save;
	for (i = 1; i < n; i++) {
		save = arr[i];
		j = i - 1;
		while (j >= 0 && arr[j] > save) {
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = save;
	}
}

void main() {
	int n, i;
	int *arr = NULL;
	scanf("%d", &n);
	arr = (int)malloc(sizeof(int) * n);
	for (i = 0; i < n; i++) {
		scanf("%d", arr + i);
	}
	inplaceInsertionSort(arr, n);
	for (i = 0; i < n; i++) {
		printf(" %d", arr[i]);
	}
}
