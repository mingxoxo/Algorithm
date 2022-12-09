// BellmanFordShortestPaths

#include <stdio.h>
#include <stdlib.h>

#define INF 2147483647

typedef struct s_vertex{
    int data;
    int distance;
    struct s_vertex *next;
}t_vertex;

typedef struct s_edge{
	int weight;
    struct s_vertex *v1;
    struct s_vertex *v2;
    struct s_edge *next;
}t_edge;

int n, m, s;

// vertex 초기화, 추가, 탐색 (header X)
t_vertex *init_vertex(int data);
t_vertex *addLast_vertex(t_vertex **head, int data);
t_vertex *find_vertex(t_vertex *node, int data);

// edge 초기화, 추가, 탐색 (header X)
t_edge *init_edge(t_vertex *v1, t_vertex *v2, int w);
t_edge *addLast_edge(t_edge **head, t_vertex *v1, t_vertex *v2, int w);
t_edge *find_edge(t_edge *node, t_vertex *v1, t_vertex *v2);

// 그래프 생성, cmd_a, cmd_d
void makeGraph(t_vertex **vertices, t_edge **edges);
void BellmanFordShortestPaths(t_vertex *vertices, t_vertex *ver, t_edge *edges);

int main() {
    t_vertex *vertices = NULL; 
    t_edge *edges = NULL;

    scanf("%d%d%d", &n, &m, &s);
    makeGraph(&vertices, &edges);
	BellmanFordShortestPaths(vertices, find_vertex(vertices, s), edges);
	return (0);
}

void makeGraph(t_vertex **vertices, t_edge **edges) {
    int vnum1, vnum2, weight;
    t_vertex *v1 = NULL, *v2 = NULL, *newv = NULL;
    t_edge *new = NULL;
    
	for (int i = 1; i <= n; i++) {
		newv = addLast_vertex(vertices, i);
	}
	
	for (int i = 0; i < m; i++) {
        scanf("%d%d%d", &vnum1, &vnum2, &weight);
	    v1 = find_vertex(*vertices, vnum1);
	    v2 = find_vertex(*vertices, vnum2);
		new = addLast_edge(edges, v1, v2, weight);
	}
}

void BellmanFordShortestPaths(t_vertex *vertices, t_vertex *ver, t_edge *edges){
    t_edge *e;
    t_vertex *u, *z, *tmp;

	ver->distance = 0;
    for (int i = 0; i < n - 1; i++){
        e = edges;
        while (e)
        {
            u = e->v1;
            z = e->v2;
            if (u->distance == INF){
                e = e->next;
                continue;
            }
            if (u->distance + e->weight < z->distance)
                z->distance = u->distance + e->weight;
            e = e->next;
        }
    }

    tmp = vertices;
	while (tmp){
		if (tmp != ver && tmp->distance != INF)
			printf(" %d %d\n", tmp->data, tmp->distance);
		tmp = tmp->next;
	}
}

t_vertex *init_vertex(int data){
    t_vertex *new = NULL;

    new = (t_vertex *)malloc(sizeof(t_vertex));
    new->data = data;
	new->distance = INF;
    new->next = NULL;
    return (new);
}

t_vertex *addLast_vertex(t_vertex **head, int data)
{
    t_vertex *new = NULL;
    t_vertex *last = NULL;

    new = init_vertex(data);
    if (*head == NULL){
        *head = new;
        return new;
    }
    last = *head;
    while (last->next)
        last = last->next;
    last->next = new;
	return new;
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


t_edge *init_edge(t_vertex *v1, t_vertex *v2, int weight){
    t_edge *new = NULL;

    new = (t_edge *)malloc(sizeof(t_edge));
	new->weight = weight;
    new->v1 = v1;
    new->v2 = v2;
    new->next = NULL;
    return (new);
}

t_edge *addLast_edge(t_edge **head, t_vertex *v1, t_vertex *v2, int weight)
{
    t_edge *new = NULL;
    t_edge *last = NULL;

    new = init_edge(v1, v2, weight);
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
