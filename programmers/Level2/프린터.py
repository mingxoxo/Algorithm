#https://programmers.co.kr/learn/courses/30/lessons/42587
#중요도가 높은 문서를 먼저 인쇄하는 프린터 개발
#1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
#2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
#3. 그렇지 않으면 J를 인쇄합니다.
def solution(priorities, location):
    answer = 0
    while priorities:
        if priorities[0] >= max(priorities):
            answer+=1
            if location == 0:
                return answer
        else:
            priorities.append(priorities[0])
        del priorities[0]
        location = (location+len(priorities)-1)%len(priorities)
        
        
#다른사람의 풀이
#key와 element로 풀어서 key와 location 비교
#any라는 함수를 사용하여 큰 값이 존재하는지 확인

#queue =  [(i,p) for i,p in enumerate(priorities)]
#cur = queue.pop(0)
#if any(cur[1] < q[1] for q in queue):
   #queue.append(cur)
