# 블로그
# 23.05.1821921

N, X = map(int, input().split())
arr = list(map(int, input().split()))

visit = [sum(arr[:X])]
for i in range(X, N):
    visit.append(visit[-1] - arr[i-X] + arr[i])

ans = max(visit)
print(ans, visit.count(ans), end='\n') if ans != 0 else print("SAD")
