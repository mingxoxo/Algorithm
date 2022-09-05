// 선택 정렬 (배열ver2)

#include <stdio.h>
#include <stdlib.h>

int	main(){
	int N = 0, max = 0, tmp = 0;
	int *str = NULL;

	scanf("%d", &N);
	str = (int *)malloc(sizeof(int) * N);
	for(int i = 0; i < N; i++){
		scanf("%d", str + i);
	}
	for(int i = N - 1; i > 0; i--)
	{
		max = 0;
		for(int j = 1; j <= i; j++)
		{
			if(str[j] > str[max])
				max = j;
		}
		tmp = str[max];
		str[max] = str[i];
		str[i] = tmp;

	}
	for(int i = 0; i < N; i++){
		printf(" %d", str[i]);
	}
	free(str);
	return (0);
}
