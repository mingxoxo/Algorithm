#import time
#start = time.time()
S = list(map(int, input()))
result = S[0]


for i in range(1, len(S)):
    if result <= 1 or S[i] <= 1:
        result += S[i]
    else:
        result *= S[i]

print(result)

#print(time.time() - start)
