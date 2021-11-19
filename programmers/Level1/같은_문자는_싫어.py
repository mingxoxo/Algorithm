def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if answer[-1] == arr[i]:
            continue
        answer.append(arr[i])
    return answer
  
  #다른 사람의 풀이
  #if a[-1:] == [i]: continue --> 리스트 슬라이싱으로 리스트와 리스트 비교
