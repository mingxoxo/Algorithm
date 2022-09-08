// 제자리 삽입 정렬 (배열ver3)

#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int *arr, int N)
{
	int i = 0, j = 0, save = 0;

	for (i = 1; i < N; i++)
	{
		save = arr[i];
		j = i - 1;
		while (j >= 0 && arr[j] > save)
		{
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = save;
	}
}

int main()
{
	int N = 0;
	int *arr = NULL;

	scanf("%d", &N);
	arr = (int *)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", arr + i);
	}
	insertion_sort(arr, N);
	for (int i = 0; i < N; i++)
	{
		printf(" %d", arr[i]);
	}
	free(arr);
	return (0);
}
