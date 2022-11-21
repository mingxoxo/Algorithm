// 방향 그래프
// 위상순서 찾기 - 진입차수 이용
// 인접리스트 구현

#include <stdio.h>
#include <stdlib.h>

# define NONDAG 'N'
# define DAG 'Y'

typedef enum label{
    FRESH,
    VISITED,
    TREE,
    BACK
}LABEL;

typedef struct s_vertex{
    int num;
    int indegree;
    char data;
    LABEL label;
    struct s_NtoE *ntoe;
    struct s_vertex *next;
}t_vertex;

typedef struct s_NtoE{
    struct s_edge *edge;
    struct s_NtoE *next;
}t_NtoE;

typedef struct s_edge{
    LABEL label;
    struct s_vertex *v1;
    struct s_vertex *v2;
    struct s_edge *next;
}t_edge;

typedef struct s_node{
    struct s_vertex *v;
    struct s_node *next;
}t_node;

// vertex 초기화, 추가, 탐색 (header X)
t_vertex *init_vertex(char data, int num);
void addLast_vertex(t_vertex **head, char , int num);
t_vertex *find_vertex(t_vertex *node, char data);
t_vertex *opposite_vertex(t_edge *edge, char data);

// edge 초기화, 추가, 탐색 (header X)
t_edge *init_edge(t_vertex *v1, t_vertex *v2);
t_edge *addLast_edge(t_edge **head, t_vertex *v1, t_vertex *v2);
t_edge *find_edge(t_edge *node, t_vertex *v1, t_vertex *v2);

// NtoE 초기화, 추가 (header O)
t_NtoE *init_NtoE(t_edge *edge);
void add_NtoE(t_NtoE *head, t_edge *edge, char data);

// queue
t_node *init_node(t_vertex *v);
void enqueue(t_node **queue, t_vertex *v);
t_vertex *dequeue(t_node **queue);

void topologicalSort(t_vertex *head, char *topOrder, int n);

void print_indegree(t_vertex *ver);
void print_NtoE(t_vertex *head, char data);

int main() {
	int n, m;
    char v, vname1, vname2;
    t_vertex *vertices = NULL, *v1 = NULL, *v2 = NULL;
    t_edge *edges = NULL, *new = NULL;
    char *topOrder = NULL;

    scanf("%d", &n); getchar();
	for (int i = 1; i <= n; i++) {
        scanf("%c", &v); getchar();
		addLast_vertex(&vertices, v, i);
	}
	
    scanf("%d", &m); getchar();
	for (int i = 0; i < m; i++) {
        scanf("%c %c", &vname1, &vname2); getchar();
	    v1 = find_vertex(vertices, vname1);
	    v2 = find_vertex(vertices, vname2);
		new = addLast_edge(&edges, v1, v2);
		add_NtoE(v1->ntoe, new, v1->data);
        v2->indegree++;
    }
    topOrder = (char *)malloc(sizeof(char) * (n + 1));
    topologicalSort(vertices, topOrder, n);
    if (topOrder[0] == NONDAG)
        printf("0\n");
    else{
        for (int i = 1; i <=n; i++)
            printf(" %c", topOrder[i]);
        printf("\n");
    }
	return (0);
}

void topologicalSort(t_vertex *head, char *topOrder, int n)
{
    int order = 1;
    t_node *queue = NULL;
    t_vertex *ver, *w;
    t_NtoE *ntoe;

    ver = head;
    while (ver){
        if (ver->indegree == 0)
            enqueue(&queue, ver);
        ver = ver->next;
    }

    while (queue){
        ver = dequeue(&queue);
        topOrder[order] = ver->data;
        order++;
        ntoe = ver->ntoe->next;
        while(ntoe){
            w = opposite_vertex(ntoe->edge, ver->data);
            w->indegree--;
            if (w->indegree == 0)
                enqueue(&queue, w);
            ntoe = ntoe->next;
        }
    }
    if (order <= n)
        topOrder[0] = NONDAG;
    else
        topOrder[0] = DAG;
}

t_vertex *init_vertex(char data, int num){
    t_vertex *new = NULL;

    new = (t_vertex *)malloc(sizeof(t_vertex));
    new->num = num;
    new->data = data;
    new->indegree = 0;
    new->label = FRESH;
    new->ntoe = (t_NtoE *)malloc(sizeof(t_NtoE));
    new->ntoe->edge = NULL;
    new->ntoe->next = NULL;
    new->next = NULL;
    return (new);
}

void addLast_vertex(t_vertex **head, char data, int num)
{
    t_vertex *new = NULL;
    t_vertex *last = NULL;

    new = init_vertex(data, num);
    if (*head == NULL){
        *head = new;
        return ;
    }
    last = *head;
    while (last->next)
        last = last->next;
    last->next = new;
}

t_vertex *find_vertex(t_vertex *node, char data){
    while (node)
	{
	    if (data == node->data)
	        return (node);
	    node = node->next;
	}
	return (NULL);
}

t_vertex *opposite_vertex(t_edge *edge, char data){
    if (edge->v1->data == data)
        return edge->v2;
    return edge->v1;
}


t_edge *init_edge(t_vertex *v1, t_vertex *v2){
    t_edge *new = NULL;

    new = (t_edge *)malloc(sizeof(t_edge));
    new->label = FRESH;
    new->v1 = v1;
    new->v2 = v2;
    new->next = NULL;
    return (new);
}

t_edge *addLast_edge(t_edge **head, t_vertex *v1, t_vertex *v2)
{
    t_edge *new = NULL;
    t_edge *last = NULL;

    new = init_edge(v1, v2);
    if (*head == NULL){
        *head = new;
        return (new);
    }
    last = *head;
    while (last->next)
        last = last->next;
    last->next = new;
    return (new);
}

t_edge *find_edge(t_edge *node, t_vertex *v1, t_vertex *v2){
    while (node)
	{
	    if (node->v1 == v1 && node->v2 == v2)
	        return (node);
	    if (node->v2 == v1 && node->v1 == v2)
	        return (node);
	    node = node->next;
	}
	return (NULL);
}


t_NtoE *init_NtoE(t_edge *edge){
    t_NtoE *new = NULL;

    new = (t_NtoE *)malloc(sizeof(t_NtoE));
    new->edge = edge;
    new->next = NULL;
    return (new);
}

void add_NtoE(t_NtoE *head, t_edge *edge, char data)
{
    t_NtoE *new = NULL;
    t_NtoE *prev = NULL;
    t_edge *p_edge = NULL;

    new = init_NtoE(edge);
    prev = head;
    new->next = prev->next;
    prev->next = new;
}

t_node *init_node(t_vertex *v){
    t_node *new = NULL;

    new = (t_node *)malloc(sizeof(t_node));
    new->v = v;
    new->next = NULL;
    return (new);
}

void enqueue(t_node **queue, t_vertex *v){
    t_node *new = NULL;
    t_node *last = NULL;

    new = init_node(v);
    if (*queue == NULL){
        *queue = new;
        return ;
    }
    last = *queue;
    while (last->next)
        last = last->next;
    last->next = new;
}

t_vertex *dequeue(t_node **queue){
    t_node *delete = NULL;
    t_vertex *v = NULL;
    delete = *queue;
    v = delete->v;
    (*queue) = delete->next;
    return v;
}

void print_indegree(t_vertex *ver){
    while (ver){
        printf(" %c %d\n", ver->data, ver->indegree);
        ver = ver->next;
    }
}

void print_NtoE(t_vertex *head, char data){
    t_NtoE *ntoe = NULL;
    t_vertex *v = find_vertex(head, data);
    
    if (v == NULL){
        printf("-1\n");
        return ;
    }
    
    ntoe = v->ntoe->next;
    while (ntoe){
        if (ntoe->edge->v1->data == data)
            printf(" %c", ntoe->edge->v2->data);
        else if (ntoe->edge->v2->data == data)
            printf(" %c", ntoe->edge->v1->data);
        ntoe = ntoe->next;
    }
    printf("\n");
}
