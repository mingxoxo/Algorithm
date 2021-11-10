#1이 될 때까지 

N, K = map(int, input().split())
count = 0

while N>1:
    N = N//K if N%K==0 else N-1
    count+=1

print(count)

## (답안)시간복잡도를 줄이기 위해 아래와 같이 풀 수 있다.
# N, K = map(int, input().split())
# count = 0

# while True:
#     #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     target = (N//K) * K
#     count += N-target
#     N = target

#     #N이 K보다 적을 때 (더 이상 나눌 수 없을 때) 탈출
#     if N < K:
#         break

#     #K로 나누기
#     count += 1
#     N //= K

# count += (N-1)

# print(count)
