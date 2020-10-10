#숫자 카드 게임
#입력 N(행의 개수) * M(열의 개수)

n, m = map(int, input().split())

card = []

for _ in range(n):
  array_list = list(map(int, input().split())) 
  card.append(array_list)

mincard = []
for i in card :
  mincard.append(min(i))

print(max(mincard))
