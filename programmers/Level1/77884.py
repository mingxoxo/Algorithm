#약수의 개수와 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/77884

def divisor(n):
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0 :
            cnt+=1
    return cnt

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer = answer + i if divisor(i) % 2 == 0 else answer - i
    return answer

#다른 사람의 풀이
#--> 제곱수의 약수 개수는 홀수개이다.
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer
