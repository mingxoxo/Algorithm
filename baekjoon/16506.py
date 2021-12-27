#CPU
#https://www.acmicpc.net/problem/16506

opcode = {"ADD": "0000", "SUB": "0001", "MOV": "0010", "AND": "0011", "OR": "0100", "NOT": "0101",
          "MULT": "0110", "LSFTL": "0111", "LSFTR": "1000", "ASFTR": "1001", "RL": "1010", "RR": "1011"}

N = int(input())

for i in range(N):
    code = list(input().split())
    if code[0][-1] == 'C':
        code[0] = opcode[code[0][:-1]] + '10'
        code[3] = bin(int(code[3]))[2:].rjust(4, '0')
    else:
        code[0] = opcode[code[0]] + '00'
        code[3] = bin(int(code[3]))[2:].rjust(3, '0') + '0'
    code[1] = bin(int(code[1]))[2:].rjust(3, '0')
    code[2] = bin(int(code[2]))[2:].rjust(3, '0')
    print(''.join(code))
