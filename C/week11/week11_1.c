// DFS - 인접 리스트

#include <stdio.h>
#include <stdlib.h>

typedef enum label{
    FRESH,
    VISITED,
    TREE,
    BACK
}LABEL;

typedef struct s_vertex{
    int data;
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

// vertex 초기화, 추가, 탐색 (header X)
t_vertex *init_vertex(int data);
void addLast_vertex(t_vertex **head, int data);
t_vertex *find_vertex(t_vertex *node, int data);

// edge 초기화, 추가, 탐색 (header X)
t_edge *init_edge(t_vertex *v1, t_vertex *v2);
t_edge *addLast_edge(t_edge **head, t_vertex *v1, t_vertex *v2);
t_edge *find_edge(t_edge *node, t_vertex *v1, t_vertex *v2);

// NtoE 초기화, 추가 (header O)
// NtoE는 추가할 때 node number 오름차순 정렬
t_NtoE *init_NtoE(t_edge *edge);
void add_NtoE(t_NtoE *head, t_edge *edge, int data, int check);

// 그래프 생성, cmd_a, cmd_d
void makeGraph(t_vertex **vertices, t_edge **edges, int n, int m);
void rDFS(t_vertex *v);

int main() {
	int n, m, s;
    t_vertex *vertices = NULL; 
    t_edge *edges = NULL;
    
    scanf("%d%d%d", &n, &m, &s);
    makeGraph(&vertices, &edges, n, m);
	rDFS(find_vertex(vertices, s));
	return (0);
}

t_vertex *init_vertex(int data){
    t_vertex *new = NULL;

    new = (t_vertex *)malloc(sizeof(t_vertex));
    new->data = data;
    new->label = FRESH;
    new->ntoe = (t_NtoE *)malloc(sizeof(t_NtoE));
    new->ntoe->edge = NULL;
    new->ntoe->next = NULL;
    new->next = NULL;
    return (new);
}

void addLast_vertex(t_vertex **head, int data)
{
    t_vertex *new = NULL;
    t_vertex *last = NULL;

    new = init_vertex(data);
    if (*head == NULL){
        *head = new;
        return ;
    }
    last = *head;
    while (last->next)
        last = last->next;
    last->next = new;
}

t_vertex *find_vertex(t_vertex *node, int data){
    while (node)
	{
	    if (data == node->data)
	        return (node);
	    node = node->next;
	}
	return (NULL);
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

void add_NtoE(t_NtoE *head, t_edge *edge, int data, int check)
{
    t_NtoE *new = NULL;
    t_NtoE *prev = NULL;
    t_edge *p_edge = NULL;

    new = init_NtoE(edge);
    prev = head;
    while (prev->next){
        p_edge = prev->next->edge;
        if (p_edge->v1->data == data){
            if (p_edge->v2->data > check)
                break;
        }
        else if (p_edge->v2->data == data){
            if (p_edge->v1->data > check)
                break;
        }
        prev = prev->next;
    }
    new->next = prev->next;
    prev->next = new;
}

t_vertex *opposite_vertex(t_edge *edge, int data){
    if (edge->v1->data == data)
        return edge->v2;
    return edge->v1;
}


void makeGraph(t_vertex **vertices, t_edge **edges, int n, int m) {
    int vnum1, vnum2;
    t_vertex *v1 = NULL, *v2 = NULL;
    t_edge *new = NULL;
    
	for (int i = 1; i <= n; i++) {
		addLast_vertex(vertices, i);
	}
	
	for (int i = 0; i < m; i++) {
        scanf("%d%d", &vnum1, &vnum2);
	    v1 = find_vertex(*vertices, vnum1);
	    v2 = find_vertex(*vertices, vnum2);
		new = addLast_edge(edges, v1, v2);
		add_NtoE(v1->ntoe, new, v1->data, v2->data);
		if (vnum1 != vnum2)
		    add_NtoE(v2->ntoe, new, v2->data, v1->data);
	}
}

void rDFS(t_vertex *v){
    t_vertex *w = NULL;
    t_NtoE *ntoe = NULL;
    
    printf("%d\n", v->data);
    v->label = VISITED;
    ntoe = v->ntoe->next;
    while (ntoe){
        if (ntoe->edge->label == FRESH){
            w = opposite_vertex(ntoe->edge, v->data);
            if (w->label == FRESH){
                ntoe->edge->label = TREE;
                rDFS(w);
            }
            else   
                ntoe->edge->label = BACK;
        }
        ntoe = ntoe->next;
    }
}