#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define NOSUCHKEY -1

typedef struct Node{
    int key;
    struct Node *parent;
    struct Node *lChild;
    struct Node *rChild;
}Node;

typedef int bool; 

Node *init_node(void);
Node *treeSearch(Node *node, int k);
void insertItem(Node *node, int k);
int findElement(Node *node, int k);
int removeElement(Node **node, int k);
void preorder(Node *node);

void expandExternal(Node *node, int k);
void reduceExternal(Node **node, Node *z);
Node *find_sibling(Node *z);
Node *inOrderSucc(Node *node);

bool isExternal(Node *node);
bool isInternal(Node *node);


int main(void)
{
    char cmd;
    int key;
    Node *tree = NULL;

    tree = init_node();
    while (1){
        scanf("%c", &cmd); 
        
        if (cmd == 'i'){
            scanf("%d", &key);
            insertItem(tree, key);
        }
        else if (cmd == 'd'){
            scanf("%d", &key); 
            if (key == removeElement(&tree, key))
            	printf("%d\n", key);
			else 
                printf("X\n");
        }
        else if (cmd == 's'){
            scanf("%d", &key); 
            if (key == findElement(tree, key))
            	printf("%d\n", key);
			else 
                printf("X\n");
        }
        else if (cmd == 'p'){
            preorder(tree);
            printf("\n");
        }
        else if (cmd == 'q')
            break;

        getchar();
    }
    return 0;
}

Node *init_node(void){
    Node *node = NULL;

    node = (Node *)malloc(sizeof(Node));
    node->key = 0;
    node->parent = NULL;
    node->lChild = NULL;
    node->rChild = NULL;
    return node;
}

//binary search Node
Node *treeSearch(Node *node, int k){
    if (isExternal(node))
        return node;
    if (k == node->key)
        return node;
    else if (k < node->key)
        return treeSearch(node->lChild, k);
    else
        return treeSearch(node->rChild, k);
}

void insertItem(Node *node, int k){
    Node *w = NULL;
    
    w = treeSearch(node, k);
    if (isInternal(w))
        return ;
    expandExternal(w, k);
}

void expandExternal(Node *node, int k){
    node->key = k;
    node->lChild = init_node();
    node->rChild = init_node();
    node->lChild->parent = node;
    node->rChild->parent = node;
}

int findElement(Node *node, int k){
    Node *find = NULL;
    
    find = treeSearch(node, k);
    if (isExternal(find))
        return k + NOSUCHKEY;
    return k;
}

int removeElement(Node **node, int k){
    int e;
    Node *w = NULL, *y = NULL, *z = NULL;
    
    w = treeSearch(*node, k);
    if (isExternal(w))
        return k + NOSUCHKEY;
    e = w->key;
    z = w->lChild; 
    if (!(isExternal(z))) //lChild가 있을 경우
        z = w->rChild; 
    if (isExternal(z)) //rChild가 없을 경우
        reduceExternal(node, z);
    else{
        y = inOrderSucc(w);
        z = y->lChild;
        w->key = y->key;
        reduceExternal(node, z);
    }
    return e;
}

void reduceExternal(Node **node, Node *z){
    Node *w = NULL, *zs = NULL;

    w = z->parent;
    zs = find_sibling(z);
    if (w->parent == NULL){
        (*node) = zs;
        if (zs)
            zs->parent = NULL;
    }
    else {
		zs->parent = w->parent;
		if ((w->parent)->lChild == w) 
            (w->parent)->lChild = zs;
		else 
            (w->parent)->rChild = zs;
	}
    free(z);    
    free(w);
}

Node *inOrderSucc(Node *node){
    node = node->rChild;

    while (node->lChild && !isExternal(node->lChild))
        node = node->lChild;
    return node;
}

Node *find_sibling(Node *z) {
	if (z->parent == NULL) 
        return NULL;
	if ((z->parent)->lChild == z) 
        return (z->parent)->rChild; 
    return (z->parent)->lChild;
}

void preorder(Node *node) {
	if (isExternal(node))
        return ;
	printf(" %d", node->key);
	preorder(node->lChild);
	preorder(node->rChild);
}

bool isExternal(Node *node){
    if (node->lChild == NULL && node->rChild == NULL)
        return TRUE;
    return FALSE;
}

bool isInternal(Node *node){
    if (node->lChild || node->rChild)
        return TRUE;
    return FALSE;
}
