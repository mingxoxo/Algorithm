// 삽입 정렬 (배열ver)

#include <stdio.h>
#include <stdlib.h>

int	main(){
	int N = 0, save = 0, j = 0;
	int *arr = NULL;

	scanf("%d", &N);
	arr = (int *)malloc(sizeof(int) * N);
	for(int i = 0; i < N; i++){
		scanf("%d", arr + i);
	}
	for(int i = 1; i < N; i++){
		save = arr[i];
		j = i - 1;
		while (j >= 0 && arr[j] > save){
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = save;
	}
	for(int i = 0; i < N; i++){
		printf(" %d", arr[i]);
	}
	free(arr);
	return (0);
}
