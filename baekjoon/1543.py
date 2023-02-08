# 문서 검색
# 23.02.08
# 문자열 / 브루트포스
# https://www.acmicpc.net/problem/1543

docs = input()
word = input()

cnt = 0
check = 0
word_len = len(word)
while check != -1:
    check = docs.find(word, check)
    if check != -1:
        cnt += 1
        check += word_len

print(cnt)
