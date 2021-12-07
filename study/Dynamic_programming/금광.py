import numpy as np

def max_gold(gold_list, n, m):
    miner = [[0]*(n+2) for _ in range(m+2)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            miner[i][j] = max(max(miner[i-1][j-1:j+2])+gold_list[i-1][j-1], miner[i][j-1])
    return max(miner[m])


T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    gold_list = []
    test_case = list(map(int, input().split()))
    for j in range(n):
        gold_list.append(test_case[j*m:j*m+m])
    print(max_gold(list(np.array(gold_list).T), n, m))
