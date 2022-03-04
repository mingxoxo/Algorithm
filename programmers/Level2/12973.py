#짝지어 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    words = []
    
    for i in s:
        if words and words[-1] == i:
            words.pop()
        else:
            words.append(i)

    return int(len(words)==0)
