#구명보트
#https://programmers.co.kr/learn/courses/30/lessons/42885
#list로 코드 작성 --> 효율성 테스트케이스 1번 시간초과 --> queue로 작성
#가장 큰 값이 limit//2보다 같거나 작으면 남은 people/2의 반올림한 값이 구명보트의 수 (len과 같은 함수를 써야되다보니 시간이 더 복잡해짐)

from collections import deque

def solution(people, limit):
    answer = 0
    queue = deque(sorted(people))
    while queue:
        if queue[0]+queue[-1] <= limit:
            queue.popleft()
        if queue:
            queue.pop()
        answer += 1    
        
    return answer
  
  #다른 사람의 풀이
  #list의 index를 활용, 짝지어 준 수를 people의 길이만큼 빼준다.
#   def solution(people, limit) :
#     answer = 0
#     people.sort()

#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer
