#멀쩡한 사각형
#https://programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    m = min(w, h)
    while m >= 1:
        if w%m == 0 and h%m == 0:
            break
        m-= 1
    s_w, s_h = w//m, h//m
    
    if s_w == 1 or s_h == 1:
        answer = max(s_w, s_h)
    elif s_w == s_h:
        answer = s_w
    else:
        answer = (s_w//2+s_h//2) * 2
        if (s_w/2 + s_h/2) == int(s_w/2 + s_h/2):
            answer += 1

    return w*h - answer*m
