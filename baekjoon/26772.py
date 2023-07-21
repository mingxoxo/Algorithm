# Poziome serca
# https://www.acmicpc.net/problem/26772

N = int(input())

heart = [" @@@   @@@  ",
         "@   @ @   @ ",
         "@    @    @ ",
         "@         @ ",
         " @       @  ",
         "  @     @   ",
         "   @   @    ",
         "    @ @     ",
         "     @      "]

for line in heart:
    print(line * N)
