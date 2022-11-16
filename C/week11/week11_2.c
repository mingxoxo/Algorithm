// BFS - 인접 행렬

#include <stdio.h>
#include <stdlib.h>

typedef enum label{
    FRESH,
    VISITED,
    TREE,
    CROSS
}LABEL;

typedef struct s_vertex{
    int data;
    LABEL label;
    struct s_vertex *next;
}t_vertex;

typedef struct s_edge{
    LABEL label;
    struct s_vertex *v1;
    struct s_vertex *v2;
    struct s_edge *next;
}t_edge;

typedef struct s_list{
    int level;
    struct s_vertex *v;
    struct s_list *next;
}t_list;

// vertice 초기화, 추가, 탐색 (header X)
t_vertex *init_vertex(int data);
void addLast_vertex(t_vertex **head, int data);
t_vertex *find_vertex(t_vertex *node, int data);

// edge 초기화, 추가, 탐색 (header X)
t_edge *init_edge(t_vertex *v1, t_vertex *v2);
t_edge *addLast_edge(t_edge **head, t_vertex *v1, t_vertex *v2);

// 인접 행렬 초기화, 출력(디버깅 용도)
void init_adjacency_matrix(t_edge ***matrix, int n);
void print_matrix(t_edge ***matrix, int n);

// BFS 실행 시 사용하는 list 초기화, 추가, 삭제
t_list *init_list(t_vertex *v, int level);
void addLast_list(t_list **head, t_vertex *v, int level);
t_vertex *popLeft_list(t_list **head);

void BFS(t_vertex *v, t_edge ***matrix, int n);
t_vertex *opposite_vertex(t_edge *edge, int data);

// 그래프 생성
void makeGraph(t_vertex **vertices, t_edge **edges, t_edge ***matrix, int n, int m);


int main() {
    int n, m, s;
    t_vertex *vertices = NULL; 
    t_edge *edges = NULL;
    t_edge ***matrix;
    
    scanf("%d%d%d", &n, &m, &s);
    matrix = (t_edge ***)malloc(sizeof(t_edge **) * (n + 1));
    for (int i = 1; i < n + 1; i++)
        matrix[i] = (t_edge **)malloc(sizeof(t_edge *) * (n + 1));
    makeGraph(&vertices, &edges, matrix, n, m);
    BFS(find_vertex(vertices, s), matrix, n);
    
    //free
    for (int i = 1; i < n + 1; i++)
        free(matrix[i]);
    free(matrix);
	return (0);
}

t_vertex *init_vertex(int data){
    t_vertex *new = NULL;

    new = (t_vertex *)malloc(sizeof(t_vertex));
    new->data = data;
    new->label = FRESH;
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


t_list *init_list(t_vertex *v, int level){
    t_list *new = NULL;

    new = (t_list *)malloc(sizeof(t_list));
    new->v = v;
    new->level = level;
    new->next = NULL;
    return (new);
}

void addLast_list(t_list **head, t_vertex *v, int level){
    t_list *new = NULL;
    t_list *last = NULL;

    new = init_list(v, level);
    if (*head == NULL){
        *head = new;
        return ;
    }
    last = *head;
    while (last->next)
        last = last->next;
    last->next = new;
}

t_vertex *popLeft_list(t_list **head){
    t_list *delete = NULL;
    t_vertex *v = NULL;
    delete = *head;
    v = delete->v;
    (*head) = delete->next;
    return v;
}


void init_adjacency_matrix(t_edge ***matrix, int n){
    for (int i = 1; i < n + 1; i++){
        for (int j = 1; j < n + 1; j++){
            matrix[i][j] = NULL;
        }
    }
}

t_vertex *opposite_vertex(t_edge *edge, int data){
    if (edge->v1->data == data)
        return edge->v2;
    return edge->v1;
}

void makeGraph(t_vertex **vertices, t_edge **edges, t_edge ***matrix, int n, int m) {
    int vnum1, vnum2;
    t_vertex *v1 = NULL, *v2 = NULL;
    t_edge *new = NULL;
    
    init_adjacency_matrix(matrix, n);
	for (int i = 1; i <= n; i++) {
		addLast_vertex(vertices, i);
	}
    for (int i = 0; i < m; i++) {
        scanf("%d%d", &vnum1, &vnum2);
	    v1 = find_vertex(*vertices, vnum1);
	    v2 = find_vertex(*vertices, vnum2);
		new = addLast_edge(edges, v1, v2);
		matrix[vnum1][vnum2] = new;
		matrix[vnum2][vnum1] = new;
	}
}

void BFS(t_vertex *v, t_edge ***matrix, int n){
    t_vertex *w = NULL;
    t_list *list = NULL;
    int level = 0;

    addLast_list(&list, v, 0);
    v->label = VISITED;
    while (list){
        v = popLeft_list(&list);
        printf("%d\n", v->data);
        for (int i = 1; i <= n; i++){
            if (!(matrix[v->data][i]))
                continue ;
            if (matrix[v->data][i]->label == FRESH){
                w = opposite_vertex(matrix[v->data][i], v->data);
                if (w->label == FRESH){
                    matrix[v->data][i]->label = TREE;
                    w->label = VISITED;
                    addLast_list(&list, w, level + 1);
                }
                else   
                    matrix[v->data][i]->label = CROSS;
            }
        }
        level++;
    }
}

void print_matrix(t_edge ***matrix, int n){
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            if (matrix[i][j] == NULL)
                printf(" -1");
            else if (matrix[i][j]->v1->data == i)
                printf(" %d", matrix[i][j]->v2->data);
            else
                printf(" %d", matrix[i][j]->v1->data);
        }
        printf("\n");
    }
}