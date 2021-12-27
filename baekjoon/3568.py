#iSharp
#https://www.acmicpc.net/problem/3568

str = list(input().replace(',', '').replace(';', '').split())

for i in range(1, len(str)):
    idx = len(str[i])
    for j in range(len(str[i])):
        if not str[i][j].isalpha():
            idx = j
            break
    print(str[0]+''.join(reversed(str[i][idx:])).replace('][', '[]'), str[i][:idx]+';')
