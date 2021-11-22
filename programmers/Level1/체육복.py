#https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
#처음에 정렬을 해주지 않아서 틀림

def solution(n, lost, reserve):
    intersect = set(lost) & set(reserve)
    lost = sorted(list(set(lost) - intersect))
    reserve = sorted(list(set(reserve) - intersect), reverse=True)
    while reserve:
        try:
            extra = reserve.pop()
            lost.remove(extra - 1)
            continue
        except:
            pass
        try:
            lost.remove(extra + 1)
        except:
            pass
    answer = n - len(lost)

    return answer
  
  #다른 사람의 풀이
  
  #try except를 사용하지 않고 in을 사용해서 리스트에 그 값이 있으면 지워줄 수 있음
  #if extra - 1 in lost
  #elif extra + 1 in lost
  
  #교집합을 제거해줄 때도 in 사용가능
  #_reserve = [r for r in reserve if r not in lost]
