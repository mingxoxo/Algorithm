#https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n): 
        bin_str = bin(arr1[i] | arr2[i]).replace('b', '0')[-n:]
        answer.append(((n-len(bin_str))*'#'+bin_str).replace('1', '#').replace('0', ' '))
        
    return answer
