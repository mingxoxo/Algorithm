#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int arr[];

void upHeap(int k) {//maxheap
	int parent;
	if (k == 1) return;
	parent = k / 2;
	if (arr[parent] > arr[k]) return;
	swap(arr[parent] , arr[k]);
	upHeap(k / 2);
}

void downHeap(int k, int last) {
	int left = 2*k;
	int right = 2 * k + 1;
	int greater;
	if (left > last) return;
	greater = left;
	if (right < last) {
		if (arr[greater] < arr[right]) swap();
	}
	if (arr[greater] < arr[k]) return;
	swap(arr[greater] , arr[k]);
	downHeap(greater, last);
}

void rBuildHeap(int k, int last) {
	if (k > last) return;
	rBuildHeap(2 * k, last);
	rBuildHeap(2 * k + 1, last);
	downHeap(k, last);
}


void main() {
	
}
