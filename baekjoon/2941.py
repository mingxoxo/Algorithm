word = input()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

#replace를 반환한 것을 변수에 저장해주어야 한다.
for i in alpha:
    word = word.replace(i, '_')

print(len(word))
