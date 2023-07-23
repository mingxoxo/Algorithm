# 골드바흐의 추측
# 정수론, 에라토스테네스의 체
# 23.07.23
# https://www.acmicpc.net/problem/9020

# 두 소수의 차이가 가장 작은 것에 대한 코드 작성 참고 
# : https://velog.io/@jieuihong/%EB%B0%B1%EC%A4%80-9020-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1%EC%8B%A4%EB%B2%841-Python

def get_prime_list(n=10000):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int((n + 1) ** 0.5) + 1):
        if sieve is False:
            continue
        for j in range(i * i, n + 1, i):
            sieve[j] = False

    return sieve


def print_goldbach_partition(n, sieve):
    a, b = n // 2, n // 2
    while a:
        if sieve[a] and sieve[b]:
            print(a, b)
            return
        a -= 1
        b += 1


T = int(input())
sieve = get_prime_list()

for _ in range(T):
    n = int(input())
    print_goldbach_partition(n, sieve)
