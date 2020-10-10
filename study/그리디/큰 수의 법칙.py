#큰수의 법칙
#첫째 줄에 배열의 크기 N, 숫자가 더해지는 수 M, K 초과 금지

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

if first == second:
  answer = m*first
else:
  answer = (m//(k+1))*second + (m - (m//(k+1)))*first

print(answer)
