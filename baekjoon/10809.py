#알파벳 찾기
#https://www.acmicpc.net/problem/10809

alpha_list = [-1 for i in range(26)]

S = input()
for i in range(len(S)):
    index = ord(S[i])-ord('a')
    if alpha_list[index] == -1:
        alpha_list[index] = i

print(*alpha_list)
