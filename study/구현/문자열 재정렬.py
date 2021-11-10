# 문자열 재정렬
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력

str = list(input())
alpha = []
sum = 0

for i in str:
    if i.isalpha():
        alpha.append(i)
    else:
        sum += int(i)

alpha.sort()
if sum != 0:
    alpha.append(str(sum))

print(''.join(alpha))

