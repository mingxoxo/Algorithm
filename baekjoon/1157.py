#단어 공부
#https://www.acmicpc.net/problem/1157

cnt_list = [0 for i in range(26)]
word = input()
for i in word.upper():
    cnt_list[ord(i)-ord('A')] += 1

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(chr(cnt_list.index(max(cnt_list)) + ord('A')))
