# K-세준수
# 수학
# 24.09.07
# https://www.acmicpc.net/problem/1418

def get_max_prime_list(n):
    n = n + 1
    max_prime = [i for i in range(n)]
    
    for i in range(2, n):
        if max_prime[i] == i:
            for j in range(i+i, n, i):
                max_prime[j] = i
    
    return max_prime



N = int(input())
K = int(input())

max_prime_list = get_max_prime_list(N)
print(len([1 for i in range(1, N + 1) if max_prime_list[i] <= K]))
