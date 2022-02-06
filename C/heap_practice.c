#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int H[100];
int n = 0;

void upHeap(int i){
   int parent = i / 2;
   int tmp;
   if(i == 1) return;
   if(H[parent] > H[i]) return;
   tmp = H[i];
   H[i] = H[parent];
   H[parent] = tmp;
   upHeap(parent);
}

void downHeap(int i, int last){
   int left = i*2;
   int right = i*2 + 1;
   int tmp;
   int max = left;
   if(left > last) return;
   if(right <= last){
      if(H[left] < H[right]) max = right;
   }
   if(H[i] > H[max]) return;
   tmp = H[i];
   H[i] = H[max];
   H[max] = tmp;
   downHeap(max, last);
}

void insertitem(int key){
   n++;
   H[n] = key;
   upHeap(n);
}

int removeMax(){
   int remove = H[1];
   H[1] = H[n];
   n--;
   downHeap(1, n);
   return remove;
}

void printHeap(){
   int i;
   for(i = 1; i <= n; i++){
      printf(" %d", H[i]);
   }
   printf("\n");
}

void rBuildHeap(int i){
   //얘는 이미 key가 다 들어와있는 배열을 받는다고 가정
   if(i >= n) return;
   rBuildHeap(2*i);
   rBuildHeap(2*i+1);
   downHeap(i, n);
}
void buildHeap(int K[], int N){
   int i;
   for(i = 1; i <= N; i++) insertitem(K[i]);
   //key를 하나하나 받는 삽입식에서 배열을 미리 만든 후에
   // rBuildHeap을 돌리는 역할을 한다.
}

void inPlaceHeapSort(int N, int K[]){
   int i, tmp;
   //원래 buildHeap
   buildHeap(K, N);
   for(i = n; i > 1; i--){
      tmp = H[1];
      H[1] = H[i];
      H[i] = tmp;
      downHeap(1, i - 1);
   }
}

void main(){
   int i, N;
   int K[100];
   scanf("%d", &N);
   for(i = 1; i <= N; i++){
      scanf("%d", K + i);
   }
   inPlaceHeapSort(N, K);
   //rBuildHeap(1);
   printHeap();
}
