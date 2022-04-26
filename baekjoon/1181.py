#단어 정렬
#https://www.acmicpc.net/problem/1181

N = int(input())

word_list = set()
for i in range(N):
    word_list.add(input())

for i in sorted(list(word_list), key = lambda x : (len(x), x)):
    print(i)
