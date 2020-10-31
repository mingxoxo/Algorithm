#모든 경우는 86400가지 -> 경우의 수가 작은편
#완전 탐색 유형 : 가능한 경우의 수를 모두 검사해보는 탐색방법, 비효율적인 시간 복잡도를 가지고 있으므로 데이터 개수가 큰 경우 정상적으로 작동하지 않을 수 있다. 일반적으로 전체 데이터 수가 100만개 이하일 때 사용하면 적절하다.

N = int(input())
count = 0

for i in range(N+1):
  if(i//10 == 3 or i%10 == 3):
    count+=60*60
    continue
  for j in range(60):
    if(j//10 == 3 or j%10 == 3):
      count+=60
      continue
    for k in range(60):
      if(k//10 == 3 or k%10 == 3):
        count+=1

print(count)

#답안 예시(문자열 자료형 변환)
#if '3' in str(i) + str(j) + str(k) : count+=1
