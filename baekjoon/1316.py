
#그룹 단어 체커
#https://www.acmicpc.net/problem/1316

N = int(input())
sum = 0

for i in range(N):
    word = input()
    word_list = []
    while word:
        word_list.append(word[0])
        word = word.lstrip(word[0])
    if len(word_list) == len(set(word_list)):
        sum += 1
print(sum)

