#https://programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    make_name = list(map(lambda x: ord(name[x]) - ord('A')
                         if ord(name[x]) - ord('A') < ord('Z') - ord(name[x]) + 1 
                         else ord('Z') - ord(name[x]) + 1, range(len(name))))
    
    #"ABAAAAAAAAABB" --> ['A', 'B', 'AAAAAAAAA', 'BB']로 만든다.
    A_str = []
    A_list = []
    for i in range(len(name)):
        if name[i] == 'A':
            A_str.append('A')
            if i == len(name) - 1:
                A_list.append(len(A_str))
        else:
            if A_str:
                A_list.append(len(A_str))
            A_list.append(0)
            A_str = []
    print(A_list)
    
    l_c = A_list.index(max(A_list))-1 if A_list.index(max(A_list)) != 0 else 0 
    r_c = len(name) - (A_list.index(max(A_list))+max(A_list))
    min_count = min([len(name)-1, l_c*2+r_c, r_c*2+l_c])
    
    print(l_c, r_c)
    
    return sum(make_name)+min_count
