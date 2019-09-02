#include<stdio.h>
#include <string.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int product(int a, int b) {
	if (b == 1) return a;
	else return product(a, b - 1) + a;
}

int modulo(int a, int b) {
	if (a < b) return a;
	else return modulo(a - b, b);
}

int quotient(int a, int b) {
	if (a < b) return 0;
	else return quotient(a - b, b) + 1;
}

void main() {
	char str[10], str1[10], str2[10];
	while (1) {
		gets(str);
		if (strcmp(str, "product") == 0) {
			scanf("%s %s", str1, str2);
			printf("%d\n", product(atoi(str1), atoi(str2)));
		}
		else if (strcmp(str, "modulo") == 0) {
			scanf("%s %s", str1, str2);
			printf("%d\n", modulo(atoi(str1), atoi(str2)));
		}
		else if (strcmp(str, "quotient") == 0) {
			scanf("%s %s", str1, str2);
			printf("%d\n", quotient(atoi(str1), atoi(str2)));
		}
	}
}