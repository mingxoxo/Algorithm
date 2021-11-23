#https://programmers.co.kr/learn/courses/30/lessons/42586
#progresses -- 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
#speeds -- 각 작업의 개발 속도가 적힌 정수 배열
#각 배포마다 몇개의 기능이 배포되는지 ?

def solution(progresses, speeds):
    answer = []
    
    while progresses:
        cnt = 0
        progresses = list(map(lambda x: progresses[x] + speeds[x], [i for i in range(len(progresses))]))
        while progresses[:1] >= [100]:
            cnt+=1
            del progresses[0]
            del speeds[0]
        if cnt != 0:
            answer.append(cnt)
    return answer
  
#내 풀이는 O(n**2)
#다른사람의 풀이
#zip 함수를 씀과 동시에 반복문을 2개 돌릴 필요 없이 
#-((p-100)//s)를 사용해서 구한다. --> ceil 함수를 쓰지 않기 위해서 -(p-100) 사용
