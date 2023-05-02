# 에라토스테네스의 체
# 23.05.02
# https://www.acmicpc.net/problem/2960

def order_of_erasing(N):
    sieve = [True] * (N + 1)
    order = []

    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] is True:
            order.append(i)
            for j in range(i + i, N + 1, i):
                if sieve[j] is True:
                    sieve[j] = False
                    order.append(j)

    order.extend([i for i in range(m + 1, N + 1) if sieve[i] is True])
    return order


N, K = map(int, input().split())
print(order_of_erasing(N)[K - 1])
