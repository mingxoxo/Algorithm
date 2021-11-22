#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(arr[commands[i][2]-1])
    return answer
  
  #다른사람의 풀이
  #return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
