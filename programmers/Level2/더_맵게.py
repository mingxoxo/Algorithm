#https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        min_value = heapq.heappop(scoville)
        if scoville :
            heapq.heappush(scoville, heapq.heappop(scoville) * 2 + min_value)
            answer += 1
        else:
            return -1
    return answer
