#문자열 압축
#https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for i in range(1, round(len(s)/2)+1):
        alpha_list = []
        for j in range(i, len(s)+i, i):
            alpha_list.append(s[j-i:j])
    
        cnt, tmp = 0, 1
        for j in range(len(alpha_list)):
            if j + 1 != len(alpha_list) and alpha_list[j] == alpha_list[j+1]:
                tmp += 1
                continue  
            tmp = len(str(tmp)) if tmp > 1 else 0
            cnt += len(alpha_list[j]) + tmp
            tmp = 1

        answer = min(answer, cnt)

    return answer
