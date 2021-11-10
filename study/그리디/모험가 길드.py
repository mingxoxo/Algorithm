#모험가 길드
#여행을 떠날 수 있는 그룹 수의 최댓값 구하기
#모든 모험가를 특정한 그룹에 넣을 필요는 없다.
#내가 짠 코드는 모임 수 리스트를 삭제하면서 진행

N = int(input())
S = list(map(int, input().split()))
S.sort() #내림차순이 아닌 오름차순이 정답 ( 최대값이기 때문 )
result = 0
count = 0

while S:
    teamNumber = S[0]
    del S[0]
    count += 1
    if teamNumber >= len(S):
        break
    result += 1
    while S:
        if count < S[0]:
            break
        del S[0]
        count += 1
    count = 0

print(result)

#답안 코드 --> 간단하고 원 리스트를 해치지 않으며 작성됨
N = int(input())
S = list(map(int, input().split()))
S.sort()

result = 0
count = 0

for i in S:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
