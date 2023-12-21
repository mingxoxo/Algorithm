# 귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다
# 구현, 시뮬레이션
# https://www.acmicpc.net/problem/6568

import sys
input=sys.stdin.readline

def increment(adder, x):
    return (adder + x) % (2 ** 8)

def binary_to_decimal(binary_number):
    return int(binary_number, 2)

def decimal_to_binary(decimal_number):
    return format(decimal_number, '08b')

while True:
    try:
        pc, adder = 0, 0
        memory = [input().rstrip() for _ in range(32)]
 
        while True:
            cmd, address = memory[pc][:3], binary_to_decimal(memory[pc][3:])
            pc = (pc + 1) % 32
            
            if cmd == '111': #HLT
                break
            if cmd == '011': #NOP
                continue
        
            if cmd == '000': #STA
                memory[address] = decimal_to_binary(adder)
            elif cmd == '001': #LDA
                adder = binary_to_decimal(memory[address])
            elif cmd == '010' and adder == 0: #BEQ
                pc = address
            elif cmd == '100': #DEC
                adder = increment(adder, 255)
            elif cmd == '101': #INC
                adder = increment(adder, 1)
            elif cmd == '110': #JMP
                pc = address % 32
        
        print(decimal_to_binary(adder))
    except:
        break
