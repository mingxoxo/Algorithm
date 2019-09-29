#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct NODE {
	int data;
	struct NODE *prev;
	struct NODE *next;
}NODE;

void getNode(NODE **p) {
	(*p) = (NODE *)malloc(sizeof(NODE));
}

void add_front(NODE **front, NODE **rear, int data) {
	NODE *tmp = NULL;
	getNode(&tmp);
	tmp->data = data;
	tmp->prev = NULL;
	tmp->next = (*front);
	if ((*front) == NULL) (*rear) = tmp;
	else {
		(*front)->prev = tmp;
	}
	(*front) = tmp;
}

void add_rear(NODE **front, NODE **rear, int data) {
	NODE *tmp = NULL;
	getNode(&tmp);
	tmp->data = data;
	tmp->next = NULL;
	tmp->prev = (*rear);
	if ((*rear) == NULL) (*front) = tmp;
	else {
		(*rear)->next = tmp;
	}
	(*rear) = tmp;
}

void del_front(NODE **front, NODE **rear) {
	NODE *tmp = NULL;
	tmp = (*front);
	if ((*front) == NULL) {
		printf("underflow");
		exit(1);
	}
	(*front) = (*front)->next;
	if ((*front) == NULL) (*rear) = NULL;
	else {
		(*front)->prev = NULL;
	}
	free(tmp);
}

void del_rear(NODE **front, NODE **rear) {
	NODE *tmp = NULL;
	tmp = (*rear);
	if ((*rear) == NULL) {
		printf("underflow");
		exit(1);
	}
	(*rear) = (*rear)->prev;
	if ((*rear) == NULL) (*front) = NULL;
	else {
		(*rear)->next = NULL;
	}
	free(tmp);
}

void change(int data, char chan[]) {
	int i = 0;
	char tmp;
	while (data > 0) {
		chan[i] = (char)(data % 10) + '0';
		data = data / 10;
		i++;
	}
	chan[i] = '\0';
	for (i = 0; i < strlen(chan) / 2; i++) {
		tmp = chan[i];
		chan[i] = chan[strlen(chan) - i - 1];
		chan[strlen(chan) - i - 1] = tmp;
	}
}

void print(NODE *front) {
	char chan[100];
	int sum = 0;
	while (front != NULL) {
		sum += front->data;
		change(front->data, chan);
		printf("%s ", chan);
		front = front->next;
	}
	change(sum, chan);
	printf("**%s**\n", chan);
}

void intdatachange(char data[], char intdata[]) {
	int i = 0, j = 0;
	for (i = 0; i < strlen(data); i++) {
		if ('0' <= data[i] && data[i] <= '9') {
			intdata[j] = data[i];
			j++;
		}
	}
	intdata[j] = '\0';
}
void main() {
	NODE *front = NULL, *rear = NULL;
	char data[100], N[100], str[100], intdata[100];
	int i = 0;
	scanf("%s", N); getchar();
	for (i = 0; i < atoi(N); i++) {
		scanf("%s", str); getchar();
		if (strcmp(str, "AF") == 0) {
			scanf("%s", data); getchar();
			intdatachange(data, intdata);
			add_front(&front, &rear, atoi(intdata));
		}
		else if (strcmp(str, "AR") == 0) {
			scanf("%s", data); getchar();
			intdatachange(data, intdata);
			add_rear(&front, &rear, atoi(intdata));
		}
		else if (strcmp(str, "DF") == 0) {
			del_front(&front, &rear);
		}
		else if (strcmp(str, "DR") == 0) {
			del_rear(&front, &rear);
		}
		else if (strcmp(str, "P") == 0) {
			print(front);
		}
	}
}

//25697 5769