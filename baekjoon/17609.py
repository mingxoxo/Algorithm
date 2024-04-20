# 회문
# 투포인터
# 24.04.20
# https://www.acmicpc.net/problem/17609


def is_palindrome(word, start, end):
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True


def check_palindrome_type(word: str) -> int:
    start, end = 0, len(string) - 1
    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1
            continue

        if is_palindrome(word, start, end - 1) or is_palindrome(word, start + 1, end):
            return 1
        else:
            return 2

    return 0


T = int(input())
for _ in range(T):
    string = input()
    print(check_palindrome_type(string))
