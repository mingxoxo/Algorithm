#대소문자 바꾸기
#https://www.acmicpc.net/problem/2744

str = list(input())

for i in range(len(str)):
    if str[i].isupper():
        print(chr(ord(str[i]) - ord('A') + ord('a')), end = '')
    else:
        print(chr(ord(str[i]) - ord('a') + ord('A')), end = '')
