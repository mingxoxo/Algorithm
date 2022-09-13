// 제자리 선택 정렬 (배열ver3)

#include <stdio.h>
#include <stdlib.h>

void selection_sort(int *arr, int N)
{
	int max = 0, tmp = 0;

	for(int i = N - 1; i > 0; i--)
	{
		max = 0;
		for(int j = 1; j <= i; j++)
		{
			if(arr[j] > arr[max])
				max = j;
		}
		tmp = arr[max];
		arr[max] = arr[i];
		arr[i] = tmp;
	}
}

int	main(){
	int N = 0;
	int *arr = NULL;

	scanf("%d", &N);
	arr = (int *)malloc(sizeof(int) * N);
	for(int i = 0; i < N; i++){
		scanf("%d", arr + i);
	}
	selection_sort(arr, N);
	for(int i = 0; i < N; i++){
		printf(" %d", arr[i]);
	}
	free(arr);
	return (0);
}
