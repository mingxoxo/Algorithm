#촌수계산
#https://www.acmicpc.net/problem/2644
#BFS_DFS로 푸는 것이 대부분인데 조금 비효율적으로 푼 것 같다.

def relatives(graph, num1, num2):
    result = -1
    num1_list = [num1]
    num2_list = [num2]
    while num1 in graph.keys():
        num1 = graph[num1]
        num1_list.append(num1)

    if num2 in num1_list:
        return num2_list.index(num2) + num1_list.index(num2)

    while num2 in graph.keys():
        num2 = graph[num2]
        num2_list.append(num2)
        if num2 in num1_list:
            result = num2_list.index(num2) + num1_list.index(num2)
            break

    return result


n = int(input()) #전체 사람의 수
num1, num2 = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호

m = int(input()) #부모 자식든 간의 관계의 개수
graph = {}

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node2] = node1

print(relatives(graph, num1, num2))
