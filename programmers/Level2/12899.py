#124 나라의 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    order = [4, 1, 2]
    while n > 0:
        answer += str(order[n%3])
        n = n//3 if n%3 != 0 else n//3-1 
    return "".join(reversed(answer))

#다른 사람의 풀이 ( if를 쓰지않고 n-=1로 해결 )
#  while n > 0:
#         n -= 1
#         answer = num[n % 3] + answer
#         n //= 3
