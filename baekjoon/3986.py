# 좋은 단어
# 23.07.13
# 스택
# https://www.acmicpc.net/problem/3986

def is_good_word(word):
    stack = []
    
    for c in word:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
 
    return False if stack else True


N = int(input())
result = 0
for _ in range(N):
    word = input();
    result += is_good_word(word)
    
print(result)
