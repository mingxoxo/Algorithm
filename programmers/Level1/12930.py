#이상한 문자 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = []
    for st in list(s.split(" ")): #공백이 연속되면 연속된 공백을 살려야 함 --> split안에 (" ") 필요
        answer.append(''.join([st[i].upper() if i%2 == 0 else st[i].lower() for i in range(len(st))]))
    return ' '.join(answer)
  
  #다른 사람의 풀이
  #return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
