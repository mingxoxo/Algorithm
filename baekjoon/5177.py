#출력 형식이 잘못되었습니다
#https://www.acmicpc.net/problem/5177

#문자 여러개 변경 함수 참고한 사이트
#https://velog.io/@keywookim/Python-translate-%ED%95%9C-%EB%B2%88%EC%97%90-%EC%97%AC%EB%9F%AC-%EB%AC%B8%EC%9E%90-%EC%B9%98%ED%99%98%ED%95%98%EA%B8%B0

K = int(input())

def error_check(s):
    special_code = ['(', ')', ';', '.', ':']
    s = s.strip() # 양쪽 사이드 공백 제거
    s = s.upper() # 대문자 소문자 구분 X
    table = str.maketrans('[{}],', '(());') #괄호 종류 구별 X, 쉼표 세미콜론 구별 X
    s = s.translate(table)
    #공백 크기 관계 없이 공백이 있으면 하나의 크기로 만들어준다.
    s = list(' '.join([i for i in s.split(' ') if i != '']))
    #특수 부호 바로 앞이나 뒤 나오는 공백 삭제
    for i in range(len(s)):
        if s[i] == ' ':
            if s[i-1] in special_code or s[i+1] in special_code:
                s[i] = '_'
    s = ''.join([i for i in s if i != '_'])
    return s

for i in range(K):
    s1 = input()
    s2 = input()
    if error_check(s1) == error_check(s2):
        print("Data Set {}: equal".format(i+1))
    else:
        print("Data Set {}: not equal".format(i + 1))
    print()
