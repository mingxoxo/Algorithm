#꿀 따기
#https://www.acmicpc.net/problem/21758
#그리디 알고리즘, 누적 합, 많은 조건 분기

N = int(input())
honey_list = list(map(int, input().split()))

honey_sum = sum(honey_list)
honey_leftsum = honey_sum - honey_list[0]
honey_rightsum = honey_list[0]

answer = 0

for i in range(1, N-1):
    honey_leftsum -= honey_list[i]
    answer = max(answer, honey_sum - honey_list[0] + honey_leftsum - honey_list[i])
    answer = max(answer, honey_sum - honey_list[N-1] + honey_rightsum - honey_list[i])
    honey_rightsum += honey_list[i]


if len(honey_list) == 3:
    answer = max(2*honey_list[1], answer)

print(answer)

