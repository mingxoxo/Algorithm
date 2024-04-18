# 비밀번호 발음하기
# 24.04.18
# https://www.acmicpc.net/problem/4659

vowels = ['a', 'e', 'i', 'o', 'u']


def is_valid_step1(string: str):
    for char in string:
        if char in vowels: return True
    return False


def is_valid_step2(string: str):
    for i in range(len(string) - 2):
        vowels_cnt = len(set(string[i:i+3]) & set(vowels))
        if vowels_cnt == 0 or vowels_cnt == 3:
            return False
    return True

def is_valid_step3(string: str):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            if string[i] not in ['e', 'o']:
                return False
    return True


while True:
    string = input()
    if string == "end":
        break

    if is_valid_step1(string) and is_valid_step2(string) and is_valid_step3(string):
        print(f'<{string}> is acceptable.')
    else:
        print(f'<{string}> is not acceptable.')
