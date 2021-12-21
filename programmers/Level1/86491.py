#최소직사각형
#https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    w = h = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        w = max(w, sizes[i][0])
        h = max(h, sizes[i][1])
    print(list(max(x) for x in sizes))

    return w*h
  
 
#다른사람의 풀이
#--> 내가 짠 코드를 한 줄로 짠 것
#def solution(sizes):
#    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
