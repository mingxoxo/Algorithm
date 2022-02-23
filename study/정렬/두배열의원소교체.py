#최대 100,000개까지 입력 가능 --> O(NlogN)을 보장하는 정렬 알고리즘 사용 필요
#처음에 비교하지 않고 답을 구하려고 하였으나 A에 들어있는 값이 B의 가장 큰 값보다 클 수 있기 때문에
#비교 후 값을 바꿔주어야 한다.

N, K = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort(reverse = True)

for i in range(K):
    if A_list[i] < B_list[i]:
        A_list[i], B_list[i] = B_list[i], A_list[i]
    else:
        break

print(sum(A_list))
