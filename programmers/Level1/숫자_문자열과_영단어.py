#https://programmers.co.kr/learn/courses/30/lessons/81301
#문자열의 replace 함수 사용하면 간단하게 구현 가능 
#문자열.replace("검색 문자", "치환 문자", 치환 횟수)

def solution(s):
    number = ["zero", "one", "two", "three", "four", "five","six" ,"seven","eight","nine"]
    answer = 0
    while s:
        if '0' <= s[0] <= '9':
            answer = answer*10 + int(s[0])
            s = s[1:]
        for i in range(len(number)):
            if number[i] == s[:len(number[i])]:
                answer = answer*10 +i
                s = s[len(number[i]):]
                break
    
    return answer
