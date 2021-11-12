#https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow%i != 0:
            continue
        if brown == (yellow//i+2)*(i+2)-(yellow//i)*i:
            answer = [yellow//i+2, i+2]
            break
    return answer
