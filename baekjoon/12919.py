# A와 B 2
# 재귀
# 24.02.13
# https://www.acmicpc.net/problem/12919

def backtracking(T):
    global S
    
    if len(S) == len(T):
        return (S == T)
    
    result = False
    if T[-1] == 'A':
        result |= backtracking(T[:-1])
    if T[0] == 'B':
        result |= backtracking(T[::-1][:-1])
    
    return result
    
    

S, T = input(), input()
print(int(backtracking(T)))
