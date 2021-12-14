#https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    
    level_1 = new_id.lower()
    level_2 = ''.join( x for x in level_1 if x.isalpha() or x.isdigit() or x in ['-', '_', '.'] )
    level_3 = level_2
    
    for i in range(14, 1, -1):
        level_3 = level_3.replace('.'*i, '.')
    level_4 = level_3
    
    if level_4[0:1] == '.':
        level_4 = level_4[1:]
    if level_4[-1:0] == '.':
        level_4 = level_4[:-1]
    level_5 = level_4
    if not level_5:
        level_5 = "a"
    level_6 = level_5[:15]
    if level_6[-1] == '.':
        level_6 = level_6[:-1]
    answer = level_6
    if len(level_6) <= 2:
        answer = level_6 + (3 - len(level_6)) * level_6[-1]

    print(answer)
    
    return answer
