#퍼즐 조각 채우기
#https://programmers.co.kr/learn/courses/30/lessons/84021

import copy
from collections import deque

def bfs(arr, n, option):
    visited = copy.deepcopy(arr)
    block = []

    while True:
        for i in range(n):
            if option in visited[i]:
                queue = deque([(i, visited[i].index(option))])
                break
    
        if not queue: 
            return block
        
        location = []
        
        while queue:
            node = queue.popleft()
            location.append(node)
            visited[node[0]][node[1]] = -1
            for i, j in [[0, 1], [-1, 0], [1, 0], [0, -1]]: 
                if n > node[0]+i >= 0 and n > node[1]+j >= 0:
                     if visited[node[0] + i][node[1] + j] == option:
                        visited[node[0]+i][node[1]+j] = -1
                        queue.append((node[0] + i, node[1] + j))
        block.append(sorted(location))

def block_rotation(block_list, n):
    rotation_list = []
    for block in block_list:
        tmp = []
        for location in block:
            tmp.append((location[1],n-location[0]-1))
        rotation_list.append(sorted(tmp))
    return rotation_list
    
def solution(game_board, table):
    answer = 0
    
    block_1 = bfs(game_board, len(game_board), 0)
    block_2 = bfs(table, len(table), 1)
    
    for i in range(4):
        remove_block1 = []
        remove_block2 = []
        for block in block_2:
            for board in block_1:
                if len(block) == len(board):
                    x, y = block[0][0]-board[0][0], block[0][1]-board[0][1]            
                    cnt = 1
                    for i in range(1, len(block)):
                        if x == block[i][0]-board[i][0] and y == block[i][1]-board[i][1]:
                            cnt+=1
                    if len(block) == cnt:
                        answer += len(block)
                        remove_block1.append(board)
                        remove_block2.append(block)
                        break
                        
            block_1 = [x for x in block_1 if x not in remove_block1]
            block_2 = [x for x in block_2 if x not in remove_block2]
        block_1 = block_rotation(block_1, len(game_board))
    return answer
