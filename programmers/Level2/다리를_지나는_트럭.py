#https://programmers.co.kr/learn/courses/30/lessons/42583
#모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지?
#다리에는 트럭이 최대 bridge_length대 올라갈 수 있다
#다리는 weight 이하까지의 무게를 견딜 수 있다 
#단, 다리에 완전히 오르지 않은 트럭의 무게는 무시

#sum(deque)를 사용하니까 초과 시간 --> sumNum 변수 설정 후 해결
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0 for i in range(bridge_length)])
    sumNum = 0
    while truck_weights :
        sumNum -= queue.popleft()
        if truck_weights[0] + sumNum <= weight :
            answer += 1
            sumNum += truck_weights[0]
            queue.append(truck_weights.pop(0))
        else:
            answer += 1
            queue.append(0)
            
    return answer + bridge_length #마지막으로 건너는 트럭들
