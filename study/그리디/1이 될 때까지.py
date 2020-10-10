#1이 될 때까지

n, k = map(int, input().split())

count = 0

while True:
  if(n == 1):
    break

  if(n%k == 0):
    n = n/k
  else :
    n -= 1
  count += 1

print(count)
