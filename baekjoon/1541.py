#잃어버린 괄호
#그리디 알고리즘
#https://www.acmicpc.net/problem/1541

expression = input().split('-')

for i in range(len(expression)):
    expression[i] = sum(map(int, expression[i].split('+')))
print(-1*sum(expression[1:])+expression[0])


