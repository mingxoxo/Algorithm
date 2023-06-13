# 하노이 탑 이동 순서
# 23.06.13
# 재귀
# https://www.acmicpc.net/problem/11729

# 매우 어려움 🥲 아래 동영상으로 코드 작성
# 공부: https://www.youtube.com/watch?v=FYCGV6F1NuY

def hanoi(cnt, start, end, tmp):
    if cnt == 1:
        print(start, end)
        return

    hanoi(cnt - 1, start, tmp, end)
    print(start, end)
    hanoi(cnt - 1, tmp, end, start)


N = int(input())
print(2**N-1)
hanoi(N, 1, 3, 2)


# # 메모리 초과 코드

# import sys
# import copy
# input = sys.stdin.readline

# sys.setrecursionlimit(10**9)


# def recursive(stacks, order, check):
#     global cnt, answer

#     if str(stacks) in check:
#         if check[str(stacks)] < len(order):
#             return

#     check[str(stacks)] = len(order)

#     if not stacks[0] and not stacks[1]:
#         if cnt == -1 or len(order) < cnt:
#             cnt = len(order)
#             answer = copy.deepcopy(order)

#         return

#     for i in range(3):
#         if not stacks[i]:
#             continue
#         for j in range(3):
#             if i == j or (order and order[-1] == (j + 1, i + 1)):
#                 continue
#             if not stacks[j] or stacks[j][-1] > stacks[i][-1]:
#                 stacks[j].append(stacks[i].pop())
#                 order.append((i + 1, j + 1))
#                 recursive(stacks, order, check)
#                 stacks[i].append(stacks[j].pop())
#                 order.pop()

# N = int(input())
# cnt = -1
# answer = []
# recursive([[i for i in reversed(range(N))], [], []], [], dict())
# print(cnt)
# for e in answer:
#     print(*e)
