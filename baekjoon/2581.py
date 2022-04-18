#소수
#https://www.acmicpc.net/problem/2581
#에라토스테네스의 체 복습 ( 시간복잡도 O(NloglogN)이라고 함 )

def prime_check(M, N):
    prime = [True] * (N+1)
    last = N**(1/2)

    for i in range(2, int(last) + 1):
        if prime[i] == True:
            for j in range(i+i, N+1, i):
                prime[j] = False
    M = 2 if M == 1 else M
    return [i for i in range(M, N+1) if prime[i] == True]



M = int(input())
N = int(input())

prime_list = prime_check(M, N)
if prime_list:
    print(sum(prime_list))
    print(prime_list[0])
else:
    print("-1")
