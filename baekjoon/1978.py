#소수 찾기
#https://www.acmicpc.net/problem/1978

def prime_list(n):
    #참고 : https://ko.wikipedia.org/wiki/에라토스테네스의_체
    #에라토스테네서 체 초기화
    sieve = [True] * (n+1)

    #n의 최대 약수는 sqrt(n) 이하 --> i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]


N = int(input())
num_list = list(map(int, input().split()))

print(len(set(prime_list(max(num_list))) & set(num_list)))
