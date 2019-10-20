#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void sort(int *a, int *b) {
	int tmp;
	tmp = (*a);
	(*a) = (*b);
	(*b) = tmp;
}

void inplaceSelectionSort(int *arr, int n) {
	int i, j, tmp, max;
	for (i = n - 1; i >= 1; i--) {
		max = i;
		for (j = 0; j <=  i - 1; j++) {
			if (arr[max] < arr[j])
				max = j;
		}
		sort(arr + max, arr + i);
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
	inplaceSelectionSort(arr, n);
	for (i = 0; i < n; i++) {
		printf("%d ", arr[i]);
	}
}
